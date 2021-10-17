import json, time
import requests
import urllib.request as urllibRequests
from python_helper import log, ReflectionHelper

from python_helper import ObjectHelper, log
from python_framework import SimpleClient, SimpleClientMethod

import Speak

from domain import SpeechConstants
from util import SoundUtil
from config import SpeechClientConfig
from dto import SpeakDto
from converter.static import SpeakConverterStatic

DEFAULT_SPEAKING_MESSAGE_DTO = SpeakDto.SpeakRequestDto(text=SpeechConstants.DEFAULT_VOICE_SERVICE_IS_OFFLINE_MESSAGE)
DEFAULT_SPEAKING_MESSAGE = Speak.Speak(
    text=DEFAULT_SPEAKING_MESSAGE_DTO.text,
    voice=SpeechConstants.DEFAULT_VOICE,
    name=DEFAULT_SPEAKING_MESSAGE_DTO.name,
    extension=DEFAULT_SPEAKING_MESSAGE_DTO.extension,
    path=DEFAULT_SPEAKING_MESSAGE_DTO.path,
    duration=1.5
)

DEFAULT_HEADERS = {
  'Content-Type': 'application/json',
  'Accept-Encoding': None
}

class SoundHandler:
    def __init__(self):
        self.playing = False
        self.buffer = []

    def addToBuffer(self, audioPath: str, duration: float):
        self.buffer.append({
            'audioPath': audioPath,
            'duration': duration
        })

    def playBuffer(self):
        if 0 < len(self.buffer) and self.isNotPlaying():
            self.playing = True
            audio = self.buffer.pop(0)
            SoundUtil.speakFromCache(audio['audioPath'], audio['duration'])

    def play(self, audioPath: str, duration: float):
        self.buffer.insert(0, {
            'audioPath': audioPath,
            'duration': duration
        })

    def store(self, audioPath: str, mp3file: any):
        SoundUtil.persistSound(audioPath, mp3file)

    def isPlaying(self):
        isPlaying = self.playing and SoundUtil.isPlaying()
        if not isPlaying:
            self.playing = False
        return isPlaying

    def isNotPlaying(self):
        isNotPlaying = not self.isPlaying()
        if not isNotPlaying:
            self.playing = True
        return isNotPlaying


@SimpleClient()
class SpeakClient :

    soundHandler = SoundHandler()

    @SimpleClientMethod(requestClass=[SpeakDto.SpeakRequestDto])
    def speak(self, dto):
        try :
            requestBody = {
                "userId": SpeechClientConfig.USER_ID,
                "ssml": f"<speak><p>{dto.text}</p></speak>",
                "voice": dto.voice,
                "narrationStyle": "regular",
                "globalSpeed": "100%",
                "globalVolume": "+0dB",
                "pronunciations": [],
                "platform": "dashboard"
                ###- , "method": "binary" ###- Adding this, the content type becomes 'Content-Type': 'audio/mpeg'
            }
            duration = len(dto.text.split()) * 0.058 + 1.54525318
            duration *= (1 + duration/30 - duration/300)
            response = requests.post(f'{SpeechClientConfig.SPEECH_BASE_URL}/transcribe', headers=DEFAULT_HEADERS, json=requestBody)
            try :
                responseBody = response.json()
                # requestBody['method'] = "binary"
                # duration = float(requests.post(f'{SpeechClientConfig.SPEECH_BASE_URL}/transcribe', headers=DEFAULT_HEADERS, json=requestBody).headers.get('Content-Length'))/6176.8125
            except Exception as exception :
                # log.prettyPython(self.speak, 'response error', ReflectionHelper.getItNaked(response), logLevel=log.DEBUG)
                log.failure(self.speak, f'Not possible to parse response as json. Original response as text: {response.text}. Response status code: {response.status_code}. Text request: {dto.text}', exception)
                return self.speakFromCache(DEFAULT_SPEAKING_MESSAGE, muted=dto.muted)
            if ObjectHelper.isNotNone(responseBody) and 399 < response.status_code :
                return self.speakFromCache(DEFAULT_SPEAKING_MESSAGE, muted=dto.muted)
            log.prettyPython(self.speak, 'Static file response', responseBody, logLevel=log.DEBUG)
            mp3file = urllibRequests.urlopen(responseBody['file'])
            audioPath = SpeakConverterStatic.fullAudioPathAndNameAndExtension(dto)
            self.save(audioPath, mp3file)
            self.play(audioPath, responseBody.get('duration', duration), dto.muted)
            return SpeakDto.SpeakResponseDto(
                key = responseBody.get('hash', f'has not present - {time.time()}'),
                text = dto.text,
                voice = dto.voice,
                path = dto.path,
                name = dto.name,
                extension = dto.extension,
                staticFileCreatedAt = responseBody.get('created_at', time.time()),
                staticUrl = responseBody.get('file'),
                duration = responseBody.get('duration', duration)
            )
        except Exception as exception :
            log.error(self.speak, f'Not possible to speak "{dto.text}" properly', exception)
            return SpeakDto.SpeakResponseDto(
                text = dto.text,
                voice = dto.voice,
                path = dto.path,
                name = dto.name,
                extension = dto.extension
            )

    @SimpleClientMethod()
    def speakFromCache(self, model: Speak.Speak, muted: bool = False) :
        if not muted:
            self.play(SpeakConverterStatic.fullAudioPathAndNameAndExtension(model), model.duration, muted)
        return SpeakDto.SpeakResponseDto(
            key = model.key,
            text = model.text,
            voice = model.voice,
            path = model.path,
            name = model.name,
            extension = model.extension,
            staticFileCreatedAt = model.staticFileCreatedAt,
            staticUrl = model.staticUrl,
            duration = model.duration
        )

    @SimpleClientMethod()
    def save(self, audioPath: str, mp3file: any):
        return self.soundHandler.store(audioPath, mp3file)

    @SimpleClientMethod()
    def play(self, audioPath: str, duration: str, muted: bool):
        if not muted:
            try:
                self.soundHandler.addToBuffer(audioPath, duration)
            except Exception as exception:
                log.failure(self.play, f'Not possible to play "{audioPath}"', exception=exception, muteStackTrace=True)
                try:
                    self.speakFromCache(DEFAULT_SPEAKING_MESSAGE, muted=dto.muted)
                except Exception as innerException:
                    log.failure(self.play, f'Not possible to play default message', exception=innerException, muteStackTrace=True)

    @SimpleClientMethod()
    def playBuffer(self):
        self.soundHandler.playBuffer()
