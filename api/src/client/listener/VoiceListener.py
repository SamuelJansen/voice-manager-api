from python_helper import log
from python_framework import HttpStatus, FlaskUtil
from queue_manager_api import MessageListener, MessageListenerMethod, MessageDto

from dto import SpeakDto
from ApiKeyContext import ApiKeyContext
from config import VoiceQueueConfig


@MessageListener(
    timeout = VoiceQueueConfig.LISTENER_TIMEOUT
    , muteLogs = False
    , logRequest = True
    , logResponse = True
)
class VoiceListener:

    @MessageListenerMethod(url = '/listener/speech',
        requestClass = [[SpeakDto.SpeakRequestDto]],
        responseClass = [[SpeakDto.SpeakResponseDto]],
        apiKeyRequired=[ApiKeyContext.ADMIN, ApiKeyContext.USER, ApiKeyContext.USER],
        runInAThread = True
        # , logRequest = True
        # , logResponse = True
    )
    def acceptSpeakAll(self, dtoList):
        return self.service.speech.speech(dtoList), HttpStatus.ACCEPTED
