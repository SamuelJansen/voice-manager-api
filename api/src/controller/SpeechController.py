from python_framework import Controller, ControllerMethod, HttpStatus

from dto import SpeakDto
from ApiKeyContext import ApiKeyContext

@Controller(url = '/speech', tag='Speech', description='Speech controller')
class SpeechController:

    @ControllerMethod(url = '/',
        requestClass = [[SpeakDto.SpeakRequestDto]],
        responseClass = [[SpeakDto.SpeakResponseDto]],
        apiKeyRequired=[ApiKeyContext.ADMIN, ApiKeyContext.USER, ApiKeyContext.API]
        , logRequest = True
        , logResponse = True
    )
    def post(self, dtoList):
        return self.service.speech.speech(dtoList), HttpStatus.CREATED
