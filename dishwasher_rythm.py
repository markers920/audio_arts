
from notes import *

#add more configuration

SONG_NAME = 'Dishwasher Rythm'

volume = 100

# Dishwasher Rythm
# C, E, G (C triad)
music_frames = [
    {'number_of_cycles': 3,                 
    'music': [
        (NOTE_C4,quarter,volume),
        #(NOTE_G4,eigth,volume),
        #(NOTE_E4,eigth,volume),  #sixteenth
        (NOTE_C4,eigth,volume),
        (NOTE_E4,eigth,volume),
        (NOTE_G4,eigth,volume),
        (REST,eigth,volume),
        (NOTE_E4,quarter,volume),
        (NOTE_C4,quarter,volume),]
    },
    {'number_of_cycles': 1,     
    'music': [
        (NOTE_C4,half,volume),
        (NOTE_E4,quarter,volume),
        (NOTE_E4,quarter,volume)]
    },
    {'number_of_cycles': 1,     
    'music': [
        (NOTE_G3,half,volume),
        (REST,half,volume)]
    }
]
