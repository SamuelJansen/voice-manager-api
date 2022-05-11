from python_framework import Service, ServiceMethod, ApiKeyManager

from dto import AudioSpeakDto


@Service()
class TheNewsService :

    @ServiceMethod(requestClass=[[AudioSpeakDto.AudioSpeakRequestDto]])
    def buildAll(self, dtoList):
        return self.emitter.theNews.todayNews(self.service.speak.buildAll(dtoList))
