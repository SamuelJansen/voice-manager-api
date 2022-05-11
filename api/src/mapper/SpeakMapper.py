from python_framework import Mapper, MapperMethod

import Speak
import SpeakDto

@Mapper()
class SpeakMapper:

    @MapperMethod(requestClass=[[SpeakDto.SpeakRequestDto]], responseClass=[[Speak.Speak]])
    def fromRequestDtoListToModelList(self, dtoList, modelList) :
        return modelList

    @MapperMethod(requestClass=[[Speak.Speak]], responseClass=[[SpeakDto.SpeakResponseDto]])
    def fromModelListToResponseDtoList(self, modelList, dtoList) :
        return dtoList

    @MapperMethod(requestClass=[SpeakDto.SpeakRequestDto], responseClass=[Speak.Speak])
    def fromRequestDtoToModel(self, dto, model) :
        return model

    @MapperMethod(requestClass=[Speak.Speak], responseClass=[SpeakDto.SpeakResponseDto])
    def fromModelToResponseDto(self, model, dto) :
        return dto
