from python_helper import log
from python_framework import Scheduler, SchedulerMethod, SchedulerType

from constant import SpeechConstant

@Scheduler(muteLogs=True)
class AudioScheduler :

    @SchedulerMethod(
        SchedulerType.INTERVAL,
        seconds = SpeechConstant.SPEAK_CHECK_INTERVAL,
        instancesUpTo = 2,
        toleranceTime = 2
    )
    def checkAndHandelAudioBuffer(self) :
        self.service.speak.checkAndHandelAudioBuffer()
