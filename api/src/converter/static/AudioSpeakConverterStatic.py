from converter.static import SpeakConverterStatic


def fullAudioPathAndNameAndExtension(audioData) :
    return SpeakConverterStatic.fullAudioPathAndNameAndExtension(audioData)

def getValidName(originalName):
    return SpeakConverterStatic.getValidName(originalName)

def getDefaultValidName(dto):
    return SpeakConverterStatic.getDefaultValidName(dto)

def toRequestDto(dto) :
    return SpeakConverterStatic.toRequestDto(dto)

def getVoiceOrDefault(givenVoice: str):
    return SpeakConverterStatic.getVoiceOrDefault(givenVoice)
