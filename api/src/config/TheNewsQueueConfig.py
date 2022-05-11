from globals import getGlobalsInstance
globalsInstance = getGlobalsInstance()


PERSIST_TODAY_NEWS_VOICE_QUEUE_KEY = globalsInstance.getSetting('queue-manager-api.the-news-api.persist-today-news-voice.queue-key')

PERSIST_TODAY_NEWS_VOICE_EMITTER_BASE_URL = globalsInstance.getSetting('queue-manager-api.base-url')
PERSIST_TODAY_NEWS_VOICE_EMITTER_API_KEY = globalsInstance.getSetting('queue-manager-api.api-key')
PERSIST_TODAY_NEWS_VOICE_EMITTER_TIMEOUT = globalsInstance.getSetting('queue-manager-api.the-news-api.persist-today-news-voice.emitter.timeout')

CREATE_TODAY_NEWS_VOICE_LISTENER_TIMEOUT = globalsInstance.getSetting('queue-manager-api.the-news-api.persist-today-news-voice.listener.timeout')
