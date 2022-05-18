from python_framework import Enum, EnumItem


@Enum()
class SpeakStatusEnumeration :

    NONE = EnumItem()

    SUCCESS = EnumItem()
    ERROR = EnumItem()

SpeakStatus = SpeakStatusEnumeration()
