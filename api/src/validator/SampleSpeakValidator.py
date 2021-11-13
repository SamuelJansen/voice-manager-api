from python_helper import ObjectHelper, DateTimeHelper
from python_framework import Validator, ValidatorMethod, GlobalException, HttpStatus, EnumItem, ApiKeyManager

from dto import SampleSpeakDto
import SampleSpeak

@Validator()
class SampleSpeakValidator:

    @ValidatorMethod(requestClass=[SampleSpeak.SampleSpeak, [SampleSpeakDto.SampleSpeakRequestDto]])
    def validateAvailableTries(self, model, dtoList):
        if 0 >= model.remainingTries - len(dtoList):
            raise GlobalException(
                message = f'This request exceeds the free tier of {model.accountKey} account',
                logMessage = f'''The {model.accountKey} apiKey has {model.remainingTries} available tries from a total of {model.maximunTries}, but is exceeding it's free tier trying to consume {len(dtoList)}''',
                status = HttpStatus.TOO_MANY_REQUESTS
            )
