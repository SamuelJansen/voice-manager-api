from python_helper import Constant as c
from python_helper import EnvironmentHelper, ObjectHelper, RandomHelper, StringHelper, log
from python_framework import Service, ServiceMethod, EnumItem

from config import SpeechConfig
from enumeration.SpeakStatus import SpeakStatus
from converter.static import SpeakConverterStatic
from dto import SpeakDto, AudioSpeakDto
import Speak


@Service()
class SpeakService:

    @ServiceMethod(requestClass=[[SpeakDto.SpeakRequestDto]])
    def speakAll(self, dtoList):
        responseDtoList = []
        try:
            speechCacheList = self.getSpeechCacheList()
            newSpeakList = []
            for dto in dtoList:
                nameAndExtension = f'{dto.name}{c.DOT}{dto.extension}'
                if nameAndExtension in speechCacheList and self.repository.speak.existsByName(dto.name):
                    model = self.repository.speak.findByName(dto.name)
                    responseDtoList.append(self.speakFromCache(model, dto.muted))
                else:
                    responseDto = self.client.speak.speak(dto)
                    responseDtoList.append(responseDto)
                    if SpeakStatus.SUCCESS == responseDto.status and not self.repository.speak.existsByName(responseDto.name):
                        newSpeakList.append(responseDto)
            self.saveAll(newSpeakList)
        except Exception as exception:
            log.failure(self.speakAll, 'Not possible to speak properly', exception, muteStackTrace=True)
            raise exception
        return responseDtoList

    @ServiceMethod(requestClass=[[SpeakDto.SpeakResponseDto]])
    def saveAll(self, dtoList):
        return self.repository.speak.saveAll([
            Speak.Speak(
                key = dto.key,
                text = dto.text,
                voice = dto.voice,
                path = dto.path,
                name = dto.name,
                extension = dto.extension,
                duration = dto.duration,
                staticUrl = dto.staticUrl,
                staticFileCreatedAt = dto.staticFileCreatedAt,
                status = dto.status
            ) for dto in dtoList
        ])

    @ServiceMethod(requestClass=[Speak.Speak, bool])
    def speakFromCache(self, model, muted):
        return self.client.speak.speakFromCache(model, muted=muted)

    @ServiceMethod()
    def getSpeechCacheList(self):
        return EnvironmentHelper.listDirectoryContent(
            SpeechConfig.PLAY_HT_STATIC_FILE_PATH
        )

    @ServiceMethod(requestClass=[str])
    def simpleSpeak(self, text):
        return self.speakAll([SpeakDto.SpeakRequestDto(text=text)])

    @ServiceMethod(requestClass=[str])
    def getConstantNameAsSpeech(self, enumName):
        return StringHelper.join(self.getConstantNameAsSpeechList(enumName), character=c.SPACE)

    @ServiceMethod(requestClass=[str])
    def getConstantNameAsSpeechList(self, enumName):
        return [] if ObjectHelper.isNone(enumName) else enumName.lower().split(c.UNDERSCORE)

    @ServiceMethod()
    def checkAndHandelAudioBuffer(self):
        return self.client.speak.playBuffer()

    @ServiceMethod(requestClass=[str])
    def findAudioByKey(self, key):
        return self.mapper.speak.fromModelToResponseDto(self.repository.speak.findByKey(key))

    @ServiceMethod(requestClass=[[AudioSpeakDto.AudioSpeakRequestDto]])
    def buildAll(self, dtoList):
        existingModelList = self.repository.speak.findAllByNameIn([dto.name for dto in dtoList])
        existingNameList = [
            model.name
            for model in existingModelList
        ]
        newRequestDtoList = []
        for dto in dtoList:
            if dto.name not in [
                *existingNameList,
                *[
                    newRequestDto.name
                    for newRequestDto in newRequestDtoList
                ]
            ]:
                newRequestDtoList.append(
                    SpeakConverterStatic.toRequestDto(
                        SpeakDto.SpeakRequestDto(
                            text = dto.text,
                            voice = dto.voice,
                            name = dto.name,
                            muted = True
                        )
                    )
                )
        responseDtoSet = self.mapper.audioSpeak.fromSpeakResponseDtoListToResponseDtoList([
            *self.mapper.audioSpeak.fromModelListToResponseDtoList(existingModelList),
            *[
                dto
                for dto in self.service.speak.speakAll(newRequestDtoList)
            ]
        ])
        responseDtoList = [
            responseDto
            for dto in dtoList
            for responseDto in responseDtoSet
            if dto.name == responseDto.name
        ]
        assert len(dtoList) == len(responseDtoList), f'Inconsistent result. dtoList: {[dto.name for dto in dtoList]}, responseDtoList: {[dto.name for dto in responseDtoList]}, responseDtoSet: {[dto.name for dto in responseDtoSet]}. Request length: {len(dtoList)}, response length: {len(responseDtoList)}, response set length: {len(responseDtoSet)}'
        return responseDtoList
