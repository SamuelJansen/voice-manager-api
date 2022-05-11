from python_framework import Service, ServiceMethod, ApiKeyManager

from dto import AudioSpeakDto, SampleSpeakDto, AiVoiceApiDto, SpeakDto
from Voice import Voice

@Service()
class SpeechService :

    @ServiceMethod(requestClass=[[SpeakDto.SpeakRequestDto]])
    def speech(self, dtoList):
        return self.service.speak.speakAll(dtoList)

    @ServiceMethod(requestClass=[[SampleSpeakDto.SampleSpeakRequestDto]])
    def sampleSpeech(self, dtoList):
        currentApiKey = ApiKeyManager.getContextData(dataClass=AiVoiceApiDto.ApiKeyDataDto)
        model = self.service.sampleSpeak.findOrCreate(currentApiKey)
        self.validator.sampleSpeak.validateAvailableTries(model, dtoList)
        responseDtoList = self.service.speak.speakAll(
            self.converter.speak.fromSampleDtoListToDtoList(dtoList, Voice.CAROLINA)
        )
        self.service.sampleSpeak.decreaseAvailableTries(model, dtoList)
        return responseDtoList, {
            'RateLimit-Limit': model.maximunTries,
            'RateLimit-Remaining': model.remainingTries,
            'RateLimit-Reset': False
        }

    @ServiceMethod(requestClass=[[AudioSpeakDto.AudioSpeakRequestDto]])
    def buildAll(self, dtoList):
        return self.service.speak.buildAll(dtoList)
