import rainbowhat as rh

def playFrequencyNoteForTime(freq, timeInSec):
    try:
        rh.buzzer.note(freq, timeInSec)
    except Exception as e:
        print (str(e))

def playMidiNoteForTime(midi_note, timeInSec):
    try:
        rh.buzzer.midi_note(midi_note, timeInSec)
    except Exception as e:
        print (str(e))