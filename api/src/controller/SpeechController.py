from python_framework import Controller, ControllerMethod, HttpStatus

from dto import SpeakDto

@Controller(url = '/speech', tag='Speech', description='Speech controller')
class SpeechController:

    @ControllerMethod(url = '/',
        requestClass = [[SpeakDto.SpeakRequestDto]],
        responseClass = [[SpeakDto.SpeakResponseDto]]
    )
    def post(self, dtoList):
        return self.service.speech.speech(dtoList), HttpStatus.CREATED
