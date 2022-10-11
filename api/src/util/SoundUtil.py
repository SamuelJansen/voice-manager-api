import time
from pygame import mixer
from python_helper import log


DEFAULT_FREQUENCY = 48_000
DEFAULT_BIT_RATE = 16
DEFAULT_CHANNELS = 2
DEFAULT_BUFFER = 1024


def initializeIfNeeded(
    frequency = DEFAULT_FREQUENCY,
    size = DEFAULT_BIT_RATE,
    channels = DEFAULT_CHANNELS,
    buffer = DEFAULT_BUFFER
):
    '''size is inttendly set to negative'''
    if not mixer.get_init():
        mixer.init(frequency=frequency, size=-size, channels=channels, buffer=buffer)

def persistSound(audioPath, audioData) :
    log.debug(persistSound, f'creating audio at audioPath: {audioPath}')
    with open(audioPath,'wb') as output :
        output.write(audioData.read()) ###- web mp3
        output.flush()
        output.close()
        del output

def playSound(audioPath, duration=0, frequency=DEFAULT_FREQUENCY):
    initializeIfNeeded(frequency=frequency)
    mixer.music.load(audioPath)
    mixer.music.play()

def isPlaying(frequency=DEFAULT_FREQUENCY):
    initializeIfNeeded(frequency=frequency)
    return mixer.music.get_busy()

def speak(audioData, audioPath, duration=1, frequency=DEFAULT_FREQUENCY):
    persistSound(audioPath, audioData)
    speakFromCache(audioPath, duration=duration, frequency=frequency)

def speakFromCache(audioPath, duration=1, frequency=DEFAULT_FREQUENCY) :
    log.debug(speakFromCache, f'reading audio at audioPath: {audioPath}')
    playSound(audioPath, duration=duration, frequency=frequency)
