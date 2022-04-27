from globals import getGlobalsInstance
globalsInstance = getGlobalsInstance()


LISTENER_TIMEOUT = globalsInstance.getSetting('queue.queue-manager-api.voice-manager-api.listener.timeout')
