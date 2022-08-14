from converter.static import SpeakConverterStatic


def fullAudioPathAndNameAndExtension(audioData) :
    return SpeakConverterStatic.fullAudioPathAndNameAndExtension(audioData)

def getValidName(originalName):
    return SpeakConverterStatic.getValidName(originalName)

def getDefaultValidName(dto, originalName=None):
    return SpeakConverterStatic.getDefaultValidName(dto, originalName=originalName)

def toRequestDto(dto):
    return SpeakConverterStatic.toRequestDto(dto)

def toResponseDto(dto):
    return SpeakConverterStatic.toResponseDto(dto)

def getVoiceOrDefault(givenVoice: str):
    return SpeakConverterStatic.getVoiceOrDefault(givenVoice)
