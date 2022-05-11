from converter.static import SpeakConverterStatic


def fullAudioPathAndNameAndExtension(audioData) :
    return SpeakConverterStatic.fullAudioPathAndNameAndExtension(audioData)

def getValidName(originalName):
    return SpeakConverterStatic.getValidName(originalName)

def toRequestDto(dto) :
    return SpeakConverterStatic.toRequestDto(dto)

def getVoiceOrDefault(givenVoice: str):
    return SpeakConverterStatic.getVoiceOrDefault(givenVoice)
