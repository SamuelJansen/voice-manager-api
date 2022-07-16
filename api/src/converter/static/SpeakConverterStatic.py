from python_helper import Constant as c
from python_helper import ObjectHelper, StringHelper, EnvironmentHelper
from python_framework import ConverterStatic

from config import SpeechConfig
from constant import SpeechConstant, AudioDataConstant

def toLowerCaseWithoutSpaces(text):
    if ObjectHelper.isNeitherNoneNorBlank(text):
        return text.lower().replace(c.SPACE, c.BLANK)

def getNamePrefix(dto):
    return toLowerCaseWithoutSpaces(f'{c.BLANK if ObjectHelper.isNone(dto.voice) else dto.voice}{c.DASH}')

def fullAudioPathAndNameAndExtension(audioData):
    path = f'{audioData.path}' if ObjectHelper.isNotNone(audioData.path) and StringHelper.isNotBlank(audioData.path) else c.BLANK
    osSeparator = f'{EnvironmentHelper.OS_SEPARATOR}' if StringHelper.isNotBlank(path) else c.BLANK
    return f'{path}{osSeparator}{audioData.name}.{audioData.extension}'

def getValidName(originalName):
    if ObjectHelper.isNotNone(originalName):
        return toLowerCaseWithoutSpaces(StringHelper.join([character for character in originalName.lower() if character in SpeechConstant.VALID_CHARACTER_SET], character=c.BLANK))
    return c.BLANK

def getDefaultValidName(dto, originalName=None):
    namePrefix = getNamePrefix(dto)
    originalName = getValidName(originalName)
    if ObjectHelper.isNeitherNoneNorBlank(originalName):
        return originalName if originalName.startswith(namePrefix) else f'{namePrefix}{originalName}'
    return f'{namePrefix}{toLowerCaseWithoutSpaces(dto.text)}'

def toRequestDto(dto):
    dto.extension = ConverterStatic.getValueOrDefault(dto.extension, AudioDataConstant.DEFAULT_AUDIO_TYPE)
    dto.path = ConverterStatic.getValueOrDefault(dto.path, SpeechConfig.PLAY_HT_STATIC_FILE_PATH)
    dto.voice = getVoiceOrDefault(dto.voice)
    if ObjectHelper.isNone(dto.name) and ObjectHelper.isNotNone(dto.text):
        dto.name = getValidName(f'{dto.voice if ObjectHelper.isNotNone(dto.voice) else c.BLANK}{c.DASH}{dto.text}'.lower().replace(c.SPACE, c.BLANK))
    return dto

def getVoiceOrDefault(givenVoice: str):
    return ConverterStatic.getValueOrDefault(givenVoice, SpeechConstant.DEFAULT_VOICE)
