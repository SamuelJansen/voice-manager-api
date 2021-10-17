from python_helper import Constant as c
from python_helper import ObjectHelper, StringHelper, EnvironmentHelper
from python_framework import ConverterStatic

from config import SpeechConfig
from domain import SpeechConstants

def fullAudioPathAndNameAndExtension(audioData) :
    path = f'{audioData.path}' if ObjectHelper.isNotNone(audioData.path) and StringHelper.isNotBlank(audioData.path) else c.BLANK
    osSeparator = f'{EnvironmentHelper.OS_SEPARATOR}' if StringHelper.isNotBlank(path) else c.BLANK
    return f'{path}{osSeparator}{audioData.name}.{audioData.extension}'

def getValidName(originalName) :
    if ObjectHelper.isNotNone(originalName) :
        return StringHelper.join([character for character in originalName if character in SpeechConstants.VALID_CHARACTER_SET], character=c.BLANK)

def toRequestDto(dto) :
    dto.extension = ConverterStatic.getValueOrDefault(dto.extension, 'mp3')
    dto.path = ConverterStatic.getValueOrDefault(dto.path, SpeechConfig.SPEECH_STATIC_FILE_PATH)
    if ObjectHelper.isNone(dto.name) and ObjectHelper.isNotNone(dto.text) :
        dto.name = getValidName(dto.text.lower())
    dto.voice = getVoiceOrDefault(dto.voice)

def getVoiceOrDefault(givenVoice: str):
    return ConverterStatic.getValueOrDefault(givenVoice, SpeechConstants.DEFAULT_VOICE)
