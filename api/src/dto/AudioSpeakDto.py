from converter.static import AudioSpeakConverterStatic


class AudioSpeakRequestDto:
    def __init__(self,
        text = None,
        voice = None,
        path = None,
        name = None,
        extension = None
    ):
        self.text = text
        self.voice = voice
        self.path = path
        self.name = AudioSpeakConverterStatic.getDefaultValidName(self)
        self.extension = extension
        AudioSpeakConverterStatic.toRequestDto(self)

class AudioSpeakResponseDto:
    def __init__(self,
        key = None,
        text = None,
        voice = None,
        path = None,
        name = None,
        extension = None,
        duration = None
    ):
        self.key = key
        self.text = text
        self.voice = voice
        self.path = path
        self.name = name
        self.extension = extension
        self.duration = duration
