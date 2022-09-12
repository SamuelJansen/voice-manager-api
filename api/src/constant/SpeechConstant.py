from python_helper import Constant as c

from Voice import Voice
from enumeration.SpeakStatus import SpeakStatus


KEY_PLAY_HT_AUTHORITY = 'PLAY_HT_AUTHORITY'
KEY_PLAY_HT_USER_ID = 'PLAY_HT_USER_ID'
KEY_PLAY_HT_BASE_URL = 'PLAY_HT_BASE_URL'

SPEAK_CHECK_INTERVAL = 0.2
DEFAULT_VOICE: str = Voice.KAREN

VALID_CHARACTER_SET = c.CHARACTERES

DEFAULT_VOICE_SERVICE_IS_OFFLINE_MESSAGE = 'Voice service is unavailable right now'
DEFAULT_STATUS = SpeakStatus.NONE
