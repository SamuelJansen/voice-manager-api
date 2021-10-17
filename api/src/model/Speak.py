from python_helper import Constant as c
from python_helper import ObjectHelper, StringHelper, DateTimeHelper
from python_framework import SqlAlchemyProxy as sap
from ModelAssociation import SPEAK, MODEL


GIANT_STRING_SIZE = 16384
LARGE_STRING_SIZE = 1024
STRING_SIZE = 512
MEDIUM_STRING_SIZE = 128
LITTLE_STRING_SIZE = 64


class Speak(MODEL):
    __tablename__ = SPEAK

    id = sap.Column(sap.Integer(), sap.Sequence(f'{__tablename__}{sap.ID}{sap.SEQ}'), primary_key=True)
    createdAt = sap.Column(sap.DateTime)
    key = sap.Column(sap.String(STRING_SIZE))
    text = sap.Column(sap.String(GIANT_STRING_SIZE))
    voice = sap.Column(sap.String(LITTLE_STRING_SIZE))
    path = sap.Column(sap.String(STRING_SIZE))
    name = sap.Column(sap.String(GIANT_STRING_SIZE))
    extension = sap.Column(sap.String(LITTLE_STRING_SIZE))
    staticFileCreatedAt = sap.Column(sap.Integer())
    staticUrl = sap.Column(sap.String(LARGE_STRING_SIZE))
    duration = sap.Column(sap.Float())

    def __init__(self,
        id = None,
        createdAt = None,
        key = None,
        text = None,
        voice = None,
        path = None,
        name = None,
        extension = None,
        staticFileCreatedAt = None,
        staticUrl = None,
        duration = None
    ):
        self.id = id
        self.createdAt = DateTimeHelper.dateTimeNow() if ObjectHelper.isNone(createdAt) else DateTimeHelper.forcedlyGetDateTime(createdAt)
        self.key = key
        self.text = text
        self.voice = voice
        self.path = path
        self.name = name
        self.extension = extension
        self.staticFileCreatedAt = staticFileCreatedAt
        self.staticUrl = staticUrl
        self.duration = duration

    def __repr__(self):
        return f'{self.__tablename__}(id: {self.id}, name: {self.name})'
