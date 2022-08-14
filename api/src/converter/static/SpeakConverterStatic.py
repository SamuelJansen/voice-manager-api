from python_helper import Constant as c
from python_helper import ObjectHelper, StringHelper, EnvironmentHelper
from python_framework import ConverterStatic

from config import SpeechConfig
from constant import SpeechConstant, AudioDataConstant


def filterOutInvalidNameCharacteres(name):
    return StringHelper.join([character for character in name.lower() if character in SpeechConstant.VALID_CHARACTER_SET], character=c.BLANK)


def toLowerCaseWithoutSpaces(text):
    if ObjectHelper.isNeitherNoneNorBlank(text):
        return text.lower().replace(c.SPACE, c.BLANK)

def getNamePrefix(dto):
    return getValidName(f'{c.BLANK if ObjectHelper.isNone(dto.voice) else dto.voice}')

def fullAudioPathAndNameAndExtension(audioData):
    path = f'{audioData.path}' if ObjectHelper.isNotNone(audioData.path) and StringHelper.isNotBlank(audioData.path) else c.BLANK
    osSeparator = f'{EnvironmentHelper.OS_SEPARATOR}' if StringHelper.isNotBlank(path) else c.BLANK
    return f'{path}{osSeparator}{audioData.name}.{audioData.extension}'

def getValidName(originalName):
    if ObjectHelper.isNotNone(originalName):
        return filterOutInvalidNameCharacteres(toLowerCaseWithoutSpaces(originalName))
    return c.BLANK

def getDefaultValidName(dto, originalName=None):
    namePrefix = getNamePrefix(dto)
    dto.name = getValidName(dto.name)
    if ObjectHelper.isNeitherNoneNorBlank(dto.name):
        return dto.name if dto.name.startswith(namePrefix) else f'{namePrefix}{dto.name}'
    return f'{namePrefix}{getValidName(dto.text)}'

def toRequestDto(dto):
    return enrichAndReturnIt(dto)

def toResponseDto(dto):
    return enrichAndReturnIt(dto)

def enrichAndReturnIt(dto):
    dto.extension = ConverterStatic.getValueOrDefault(dto.extension, AudioDataConstant.DEFAULT_AUDIO_TYPE)
    dto.path = ConverterStatic.getValueOrDefault(dto.path, SpeechConfig.PLAY_HT_STATIC_FILE_PATH)
    dto.voice = getVoiceOrDefault(dto.voice)
    dto.name = getDefaultValidName(dto, originalName=dto.name)
    return dto

def getVoiceOrDefault(givenVoice: str):
    return ConverterStatic.getValueOrDefault(givenVoice, SpeechConstant.DEFAULT_VOICE)
