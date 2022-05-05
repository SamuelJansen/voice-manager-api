from python_helper import EnvironmentHelper
from constant import SpeechConstant

from python_framework import Enum, EnumItem

from globals import getGlobalsInstance
globalsInstance = getGlobalsInstance()


PLAY_HT_USER_ID = EnvironmentHelper.get(SpeechConstant.KEY_PLAY_HT_USER_ID)
PLAY_HT_BASE_URL = EnvironmentHelper.get(SpeechConstant.KEY_PLAY_HT_BASE_URL)
FREQUENCY = globalsInstance.getSetting('speech.client.frequency')
