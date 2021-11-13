from python_framework import Enum, EnumItem


@Enum()
class ApiKeyContextEnumeration :
    ADMIN = EnumItem()
    USER = EnumItem()
    FREE_TIER = EnumItem()

ApiKeyContext = ApiKeyContextEnumeration()
