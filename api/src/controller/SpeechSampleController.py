from python_framework import Controller, ControllerMethod, HttpStatus

from dto import SpeakDto, SampleSpeakDto
from ApiKeyContext import ApiKeyContext

@Controller(url='/speech/sample', responseHeaders={'Access-Control-Allow-Origin': '*'}, tag='SpeechSample', description='Sample speech controller')
class SpeechSampleController:

    @ControllerMethod(url = '/',
        requestClass = [[SampleSpeakDto.SampleSpeakRequestDto]],
        responseClass = [[SpeakDto.SpeakResponseDto]],
        apiKeyRequired=[ApiKeyContext.FREE_TIER]
        , logRequest = True
        , logResponse = True
    )
    def post(self, dtoList):
        return self.service.speech.sampleSpeech(dtoList), HttpStatus.CREATED
