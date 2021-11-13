from python_framework import Converter, ConverterMethod, EnumItem

from dto import SampleSpeakDto, SpeakDto


@Converter()
class SpeakConverter:

    @ConverterMethod(requestClass=[[SampleSpeakDto.SampleSpeakRequestDto], EnumItem])
    def fromSampleDtoListToDtoList(self, sampleDtoList, voice):
        return [
            SpeakDto.SpeakRequestDto(
                text = sampleDto.text,
                voice = voice,
                muted = True
            ) for sampleDto in sampleDtoList
        ]
