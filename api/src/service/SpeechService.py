from python_framework import Service, ServiceMethod

from dto import SpeakDto

@Service()
class SpeechService :

    @ServiceMethod(requestClass=[[SpeakDto.SpeakRequestDto]])
    def speech(self, dtoList) :
        return self.service.speak.speakAll(dtoList)
