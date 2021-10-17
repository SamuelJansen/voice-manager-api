from python_helper import EnvironmentHelper
from domain import SpeechConstants

from python_framework import Enum, EnumItem

USER_ID = EnvironmentHelper.get(SpeechConstants.KEY_SPEECH_USER_ID)
SPEECH_BASE_URL = EnvironmentHelper.get(SpeechConstants.KEY_SPEECH_BASE_URL)
