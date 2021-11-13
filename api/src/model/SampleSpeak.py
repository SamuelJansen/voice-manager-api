from python_helper import Constant as c
from python_helper import ObjectHelper, StringHelper, DateTimeHelper
from python_framework import SqlAlchemyProxy as sap
from ModelAssociation import SAMPLE_SPEAK, MODEL


LITTLE_STRING_SIZE = 64


class SampleSpeak(MODEL):
    __tablename__ = SAMPLE_SPEAK

    id = sap.Column(sap.Integer(), sap.Sequence(f'{__tablename__}{sap.ID}{sap.SEQ}'), primary_key=True)
    accountKey = sap.Column(sap.String(LITTLE_STRING_SIZE), nullable=False, unique=True)
    maximunTries = sap.Column(sap.Integer(), nullable=False)
    remainingTries = sap.Column(sap.Integer(), nullable=False)

    def __init__(self,
        id = None,
        accountKey = None,
        maximunTries = None,
        remainingTries = None
    ):
        self.id = id
        self.accountKey = accountKey
        self.maximunTries = maximunTries
        self.remainingTries = remainingTries

    def __repr__(self):
        return f'{self.__tablename__}(id: {self.id}, accountKey: {self.accountKey}, maximunTries: {self.maximunTries}, remainingTries: {self.remainingTries})'
