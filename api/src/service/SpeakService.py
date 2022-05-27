from python_helper import Constant as c
from python_helper import EnvironmentHelper, ObjectHelper, RandomHelper, StringHelper, log
from python_framework import Service, ServiceMethod, EnumItem

from config import SpeechConfig
from enumeration.SpeakStatus import SpeakStatus
from converter.static import SpeakConverterStatic
from dto import SpeakDto, AudioSpeakDto
import Speak


@Service()
class SpeakService :

    @ServiceMethod(requestClass=[[SpeakDto.SpeakRequestDto]])
    def speakAll(self, dtoList) :
        responseDtoList = []
        try :
            speechCacheList = self.getSpeechCacheList()
            newSpeakList = []
            for dto in dtoList :
                nameAndExtension = f'{dto.name}{c.DOT}{dto.extension}'
                if nameAndExtension in speechCacheList and self.repository.speak.existsByName(dto.name):
                    model = self.repository.speak.findByName(dto.name)
                    responseDtoList.append(self.speakFromCache(model, dto.muted))
                else :
                    responseDtoList.append(self.client.speak.speak(dto))
                    newSpeakList.append(responseDtoList[-1])
            self.saveAll(newSpeakList)
        except Exception as exception :
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
    def speakFromCache(self, model, muted) :
        return self.client.speak.speakFromCache(model, muted=muted)

    @ServiceMethod()
    def getSpeechCacheList(self) :
        return EnvironmentHelper.listDirectoryContent(
            SpeechConfig.PLAY_HT_STATIC_FILE_PATH
        )

    @ServiceMethod(requestClass=[str])
    def simpleSpeak(self, text) :
        return self.speakAll([SpeakDto.SpeakRequestDto(text=text)])

    @ServiceMethod(requestClass=[str])
    def getConstantNameAsSpeech(self, enumName) :
        return StringHelper.join(self.getConstantNameAsSpeechList(enumName), character=c.SPACE)

    @ServiceMethod(requestClass=[str])
    def getConstantNameAsSpeechList(self, enumName) :
        return [] if ObjectHelper.isNone(enumName) else enumName.lower().split(c.UNDERSCORE)

    @ServiceMethod()
    def checkAndHandelAudioBuffer(self) :
        return self.client.speak.playBuffer()

    @ServiceMethod(requestClass=[str])
    def findAudioByKey(self, key):
        return self.mapper.speak.fromModelToResponseDto(self.repository.speak.findByKey(key))

    @ServiceMethod(requestClass=[[AudioSpeakDto.AudioSpeakRequestDto]])
    def buildAll(self, dtoList):
        existingModelList = self.repository.speak.findAllByNameIn([dto.name for dto in dtoList])
        responseDtoList = set(self.mapper.audioSpeak.fromSpeakResponseDtoListToResponseDtoList([
            *self.mapper.audioSpeak.fromModelListToResponseDtoList(existingModelList),
            *self.service.speak.speakAll([
                SpeakConverterStatic.toRequestDto(SpeakDto.SpeakRequestDto(
                    text = dto.text,
                    voice = dto.voice,
                    name = SpeakConverterStatic.getDefaultValidName(dto),
                    muted = True
                ))
                for dto in dtoList if dto.name not in [
                    model.name
                    for model in existingModelList
                ]
            ])
        ]))
        orderedResponseDtoList = [
            responseDto
            for dto in dtoList
            for responseDto in responseDtoList
            if dto.name == responseDto.name
        ]
        assert len(dtoList) == len(orderedResponseDtoList), f'Some audio datas werend found. dtoList: {[dto.name for dto in dtoList]}, orderedResponseDtoList: {[dto.name for dto in orderedResponseDtoList]}. Request length: {len(dtoList)}, dto length: {len(orderedResponseDtoList)}'
        return orderedResponseDtoList
