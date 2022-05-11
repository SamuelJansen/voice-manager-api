from python_framework import Mapper, MapperMethod

import Speak
import AudioSpeakDto, SpeakDto

@Mapper()
class AudioSpeakMapper:

    @MapperMethod(requestClass=[[AudioSpeakDto.AudioSpeakRequestDto]], responseClass=[[Speak.Speak]])
    def fromRequestDtoListToModelList(self, dtoList, modelList) :
        return modelList

    @MapperMethod(requestClass=[[Speak.Speak]], responseClass=[[AudioSpeakDto.AudioSpeakResponseDto]])
    def fromModelListToResponseDtoList(self, modelList, dtoList) :
        return dtoList

    @MapperMethod(requestClass=[AudioSpeakDto.AudioSpeakRequestDto], responseClass=[Speak.Speak])
    def fromRequestDtoToModel(self, dto, model) :
        return model

    @MapperMethod(requestClass=[Speak.Speak], responseClass=[AudioSpeakDto.AudioSpeakResponseDto])
    def fromModelToResponseDto(self, model, dto) :
        return dto

    @MapperMethod(requestClass=[[SpeakDto.SpeakResponseDto]], responseClass=[[AudioSpeakDto.AudioSpeakResponseDto]])
    def fromSpeakResponseDtoListToResponseDtoList(self, speakDtoList, dtoList):
        return dtoList

    @MapperMethod(requestClass=[SpeakDto.SpeakResponseDto], responseClass=[AudioSpeakDto.AudioSpeakResponseDto])
    def fromSpeakResponseDtoToResponseDto(self, speakDto, dto):
        return dto
