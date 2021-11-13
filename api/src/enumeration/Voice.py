from python_framework import Enum, EnumItem


@Enum(associateReturnsTo='name')
class VoiceEnumeration :
    KAREN = EnumItem(name='Karen')
    CAROLINA = EnumItem(name='pt-BR_IsabelaV3Voice')

Voice = VoiceEnumeration()
