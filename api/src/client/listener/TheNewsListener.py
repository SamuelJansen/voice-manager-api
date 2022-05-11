from python_helper import log
from python_framework import HttpStatus, FlaskUtil
from queue_manager_api import MessageListener, MessageListenerMethod, MessageDto

from dto import AudioSpeakDto
from ApiKeyContext import ApiKeyContext
from config import TheNewsQueueConfig


@MessageListener(
    timeout = TheNewsQueueConfig.CREATE_TODAY_NEWS_VOICE_LISTENER_TIMEOUT
    , muteLogs = False
    , logRequest = True
    , logResponse = True
)
class TheNewsListener:

    @MessageListenerMethod(url = '/listener/speech/audio',
        requestClass = [[AudioSpeakDto.AudioSpeakRequestDto]],
        apiKeyRequired=[ApiKeyContext.ADMIN, ApiKeyContext.USER, ApiKeyContext.API],
        runInAThread = True
        # , logRequest = True
        # , logResponse = True
    )
    def acceptAudioSpeakList(self, dtoList):
        return self.service.theNews.buildAll(dtoList), HttpStatus.ACCEPTED
