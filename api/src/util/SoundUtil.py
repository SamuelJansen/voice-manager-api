from pygame import mixer
import time, winsound
from python_helper import log

def beepAndSleep(beep=1, wait=0) :
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 50  # Set Duration To 1000 ms == 1 second
    interval = 50
    for _ in range(beep):
        winsound.Beep(frequency, duration)
        time.sleep(interval/1000)
    time.sleep(wait)

def initializeIfNeeded():
    if not mixer.get_init():
        mixer.init(frequency=48000)

def persistSound(audioPath, audioData) :
    log.debug(persistSound, f'creating audio at audioPath: {audioPath}')
    with open(audioPath,'wb') as output :
        output.write(audioData.read())
        output.flush()
        output.close()
        del output

def playSound(audioPath, duration=0):
    initializeIfNeeded()
    mixer.music.load(audioPath)
    mixer.music.play()
    # time.sleep(duration)

def isPlaying():
    initializeIfNeeded()
    return mixer.music.get_busy()

def speak(audioData, audioPath, duration=1):
    persistSound(audioPath, audioData)
    speakFromCache(audioPath, duration=duration)

def speakFromCache(audioPath, duration=1) :
    log.debug(speakFromCache, f'reading audio at audioPath: {audioPath}')
    playSound(audioPath, duration=duration)
