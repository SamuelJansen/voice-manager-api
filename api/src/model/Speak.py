from python_helper import Constant as c
from python_helper import ObjectHelper, StringHelper, DateTimeHelper
from python_framework import SqlAlchemyProxy as sap
from python_framework import ConverterStatic

from ModelAssociation import SPEAK, MODEL
from constant import SpeechConstant


class Speak(MODEL):
    __tablename__ = SPEAK

    id = sap.Column(sap.Integer(), sap.Sequence(f'{__tablename__}{sap.ID}{sap.SEQ}'), primary_key=True)
    createdAt = sap.Column(sap.DateTime)
    key = sap.Column(sap.String(sap.STRING_SIZE), unique=True)
    text = sap.Column(sap.String(sap.GIANT_STRING_SIZE))
    voice = sap.Column(sap.String(sap.LITTLE_STRING_SIZE))
    path = sap.Column(sap.String(sap.STRING_SIZE))
    name = sap.Column(sap.String(sap.GIANT_STRING_SIZE))
    extension = sap.Column(sap.String(sap.LITTLE_STRING_SIZE))
    duration = sap.Column(sap.Float())
    staticUrl = sap.Column(sap.String(sap.LARGE_STRING_SIZE))
    staticFileCreatedAt = sap.Column(sap.Integer())
    status = sap.Column(sap.String(sap.LITTLE_STRING_SIZE), nullable=False, default=SpeechConstant.DEFAULT_STATUS)

    def __init__(self,
        id = None,
        createdAt = None,
        key = None,
        text = None,
        voice = None,
        path = None,
        name = None,
        extension = None,
        duration = None,
        staticUrl = None,
        staticFileCreatedAt = None,
        status = None
    ):
        self.id = id
        self.createdAt = DateTimeHelper.dateTimeNow() if ObjectHelper.isNone(createdAt) else DateTimeHelper.forcedlyGetDateTime(createdAt)
        self.key = key
        self.text = text
        self.voice = voice
        self.path = path
        self.name = name
        self.extension = extension
        self.duration = duration
        self.staticUrl = staticUrl
        self.staticFileCreatedAt = staticFileCreatedAt
        self.status = ConverterStatic.getValueOrDefault(status, SpeechConstant.DEFAULT_STATUS)

    def __repr__(self):
        return f'{self.__tablename__}(id: {self.id}, name: {self.name})'
