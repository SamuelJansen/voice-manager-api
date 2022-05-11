from globals import getGlobalsInstance
globalsInstance = getGlobalsInstance()


SPEAK_ALL_QUEUE_KEY = globalsInstance.getSetting('queue-manager-api.voice-manager-api.speak-all.queue-key')

SPEAK_ALL_EMITTER_BASE_URL = globalsInstance.getSetting('queue-manager-api.base-url')
SPEAK_ALL_EMITTER_API_KEY = globalsInstance.getSetting('queue-manager-api.api-key')
SPEAK_ALL_EMITTER_TIMEOUT = globalsInstance.getSetting('queue-manager-api.voice-manager-api.speak-all.emitter.timeout')

SPEAK_ALL_LISTENER_TIMEOUT = globalsInstance.getSetting('queue-manager-api.voice-manager-api.speak-all.listener.timeout')
