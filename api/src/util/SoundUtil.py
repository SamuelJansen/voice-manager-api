import time
from pygame import mixer
from python_helper import log

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
