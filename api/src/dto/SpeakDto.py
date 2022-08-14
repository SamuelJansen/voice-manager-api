from python_helper import ObjectHelper
from converter.static import SpeakConverterStatic

class SpeakRequestDto:
    def __init__(self,
        text = None,
        voice = None,
        path = None,
        name = None,
        extension = None,
        muted = None
    ):
        self.text = text
        self.voice = voice
        self.path = path
        self.name = name
        self.extension = extension
        self.muted = muted if ObjectHelper.isNotNone(muted) else False
        SpeakConverterStatic.toRequestDto(self)

class SpeakResponseDto:
    def __init__(self,
        key = None,
        text = None,
        voice = None,
        path = None,
        name = None,
        extension = None,
        staticFileCreatedAt = None,
        staticUrl = None,
        duration = None,
        status = None
    ):
        self.key = key
        self.text = text
        self.voice = voice
        self.path = path
        self.name = name
        self.extension = extension
        self.staticFileCreatedAt = staticFileCreatedAt
        self.staticUrl = staticUrl
        self.duration = duration
        self.status = status
