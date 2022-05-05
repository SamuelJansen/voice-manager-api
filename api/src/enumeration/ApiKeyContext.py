from python_framework import Enum, EnumItem


@Enum()
class ApiKeyContextEnumeration :
    ADMIN = EnumItem()
    USER = EnumItem()
    API = EnumItem()
    FREE_TIER = EnumItem()

ApiKeyContext = ApiKeyContextEnumeration()
