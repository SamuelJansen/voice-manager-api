from python_framework import Service, ServiceMethod, ConverterStatic, GlobalException

from dto import SpeakDto, AiVoiceApiDto
import SampleSpeak


@Service()
class SampleSpeakService :

    @ServiceMethod(requestClass=[AiVoiceApiDto.ApiKeyDataDto])
    def findOrCreate(self, currentApiKey):
        if self.notExistsByAccountKey(currentApiKey.accountKey):
            return self.create(currentApiKey)
        else:
            return self.findByAccountKey(currentApiKey.accountKey)

    @ServiceMethod(requestClass=[SampleSpeak.SampleSpeak, [SpeakDto.SpeakRequestDto]])
    def decreaseAvailableTries(self, model, dtoList) :
        model.remainingTries -= len(dtoList)
        return self.repository.sampleSpeak.save(model)

    @ServiceMethod(requestClass=[str])
    def findByAccountKey(self, accountKey):
        return self.repository.sampleSpeak.findByAccountKey(accountKey)

    @ServiceMethod(requestClass=[AiVoiceApiDto.ApiKeyDataDto])
    def create(self, currentApiKey):
        return self.repository.sampleSpeak.save(SampleSpeak.SampleSpeak(
            accountKey = currentApiKey.accountKey,
            maximunTries = currentApiKey.maximunTries,
            remainingTries = currentApiKey.maximunTries
        ))

    @ServiceMethod(requestClass=[str])
    def notExistsByAccountKey(self, accountKey):
        return self.repository.sampleSpeak.notExistsByAccountKey(accountKey)

    def getAvailableTries(self, currentApiKey):
        return ConverterStatic.getValueOrDefault(currentApiKey, dict()).get('data', dict()).get('remainingTries')

    def getAccountKey(self, currentApiKey):
        return ConverterStatic.getValueOrDefault(currentApiKey, dict()).get('data', dict()).get('accountKey')
