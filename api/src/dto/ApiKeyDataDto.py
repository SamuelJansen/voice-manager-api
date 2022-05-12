from python_framework import JwtConstant

class ApiKeyDataDto:

    _contextInfo = dict()

    def __init__(self,
        accountKey = None,
        maximunTries = None,
        remainingTries = None
    ):
        self.accountKey = accountKey
        self.maximunTries = maximunTries
        self.remainingTries = remainingTries
