import time
import rainbowhatwrapper.util.RhBuzzerUtil as rhBuzzer

class RhBuzzerHandler:

    #CONSTANTS
    BUZZER_PLAY_MODE_NOTE = 0
    BUZZER_PLAY_MODE_MIDI = 1

    @classmethod
    def play(cls, note, timeInSec, playMode = 0):
        if playMode == 0:
            rhBuzzer.playFrequencyNoteForTime(note, timeInSec)
        else:
            rhBuzzer.playMidiNoteForTime(note, timeInSec)
    
    @classmethod
    def playNote(cls, note, timeInSec):
        cls.play(note, timeInSec, cls.BUZZER_PLAY_MODE_NOTE)
    
    @classmethod
    def playMidi(cls, note, timeInSec):
        cls.play(note, timeInSec, cls.BUZZER_PLAY_MODE_MIDI)
    
    @staticmethod
    def playBeginning():
        time_count = 0
        song = [60, 60, 70, 60, 60, 70, 60, 60, 70, 60, 60, 90]
        for note in song:
            RhBuzzerHandler.playMidi(note, 0.1)
            time.sleep(0.1)
            time_count = time_count + 1
            if time_count%3 == 0:
                time.sleep(0.5)
