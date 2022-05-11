from python_framework import Serializer, HttpStatus, JwtConstant
from queue_manager_api import MessageEmitter, MessageEmitterMethod

from config import TheNewsQueueConfig
import AudioSpeakDto


@MessageEmitter(
    url = TheNewsQueueConfig.PERSIST_TODAY_NEWS_VOICE_EMITTER_BASE_URL,
    timeout = TheNewsQueueConfig.PERSIST_TODAY_NEWS_VOICE_EMITTER_TIMEOUT,
    headers = {
        'Content-Type': 'application/json',
        JwtConstant.DEFAULT_JWT_API_KEY_HEADER_NAME: f'Bearer {TheNewsQueueConfig.PERSIST_TODAY_NEWS_VOICE_EMITTER_API_KEY}'
    }
    , muteLogs = False
    , logRequest = True
    , logResponse = True
)
class TheNewsEmitter:

    @MessageEmitterMethod(
        url = '/message/emitter',
        queueKey = TheNewsQueueConfig.PERSIST_TODAY_NEWS_VOICE_QUEUE_KEY,
        requestClass=[[AudioSpeakDto.AudioSpeakResponseDto]]
        , logRequest = True
        , logResponse = True
    )
    def todayNews(self, dtoList):
        return self.emit(body=dtoList)
