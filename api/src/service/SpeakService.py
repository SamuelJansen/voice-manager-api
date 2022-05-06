from python_helper import Constant as c
from python_helper import EnvironmentHelper, ObjectHelper, RandomHelper, StringHelper, log
from python_framework import Service, ServiceMethod, EnumItem

import Speak

from config import SpeechConfig
from dto import SpeakDto
from converter.static import SpeakConverterStatic

@Service()
class SpeakService :

    @ServiceMethod(requestClass=[[SpeakDto.SpeakRequestDto]])
    def speakAll(self, dtoList) :
        responseDtoList = []
        try :
            speechCacheList = self.getSpeechCacheList()
            newSpeakList = []
            for dto in dtoList :
                nameAndExtension = f'{dto.name}{c.DOT}{dto.extension}'
                if nameAndExtension in speechCacheList and self.repository.speak.existsByName(dto.name):
                    model = self.repository.speak.findByName(dto.name)
                    responseDtoList.append(self.speakFromCache(model, dto.muted))
                else :
                    responseDtoList.append(self.client.speak.speak(dto))
                    newSpeakList.append(responseDtoList[-1])
            self.saveAll(newSpeakList)
        except Exception as exception :
            log.failure(self.speakAll, 'Not possible to speak properly', exception, muteStackTrace=True)
            raise exception
        return responseDtoList

    @ServiceMethod(requestClass=[[SpeakDto.SpeakResponseDto]])
    def saveAll(self, speakResponseDto):
        return self.repository.speak.saveAll([
            Speak.Speak(
                key = response.key,
                text = response.text,
                voice = response.voice,
                path = response.path,
                name = response.name,
                extension = response.extension,
                staticFileCreatedAt = response.staticFileCreatedAt,
                staticUrl = response.staticUrl,
                duration = response.duration
            ) for response in speakResponseDto
        ])

    @ServiceMethod(requestClass=[Speak.Speak, bool])
    def speakFromCache(self, model, muted) :
        return self.client.speak.speakFromCache(model, muted=muted)

    @ServiceMethod()
    def getSpeechCacheList(self) :
        return EnvironmentHelper.listDirectoryContent(
            SpeechConfig.PLAY_HT_STATIC_FILE_PATH
        )

    @ServiceMethod(requestClass=[str])
    def simpleSpeak(self, text) :
        return self.speakAll([SpeakDto.SpeakRequestDto(text=text)])

    @ServiceMethod(requestClass=[str])
    def getConstantNameAsSpeech(self, enumName) :
        return StringHelper.join(self.getConstantNameAsSpeechList(enumName), character=c.SPACE)

    @ServiceMethod(requestClass=[str])
    def getConstantNameAsSpeechList(self, enumName) :
        return [] if ObjectHelper.isNone(enumName) else enumName.lower().split(c.UNDERSCORE)

    @ServiceMethod()
    def checkAndHandelAudioBuffer(self) :
        return self.client.speak.playBuffer()
