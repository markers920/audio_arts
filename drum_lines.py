
from notes import *
from chords import *
from midi_instrument_numbers import *
import music_functions

#add more configuration

#https://beatsure.com/common-drum-beats/#standard
SONG_NAME = 'Drum Lines'

tempo = 30

#(NOTE_C4,quarter,volume), (NOTE_C4,quarter,volume), (NOTE_C4,quarter,volume)
# chord_progression_CGaF

# C - c_major_chord - [C4 (60), E4 (64), G (67)]
# G - g_major_chord - [G4 (67), B4 (71), D5 (74)]
# a - a_minor_chord - [A4 (69), C5 (72), E5 (76)]
# F - f_major_chord - [F4 (65), A4 (69), C5 (72)]



music_frames_map = {}

######################################################################################
# basic rythm keeping us on track
volume = 30
music_frames_map[(len(music_frames_map),banjo)] = [
    {'number_of_cycles': 3,
    'music': [
        (NOTE_C4,sixteenth,volume),
        (NOTE_C4,sixteenth,volume),
        (NOTE_C4,sixteenth,volume),
        (NOTE_C4,sixteenth,volume),
        
        (NOTE_C4,sixteenth,volume),
        (NOTE_C4,sixteenth,volume),
        (NOTE_C4,sixteenth,volume),
        (NOTE_C4,sixteenth,volume),
        
        (NOTE_C4,sixteenth,volume),
        (NOTE_C4,sixteenth,volume),
        (NOTE_C4,sixteenth,volume),
        (NOTE_C4,sixteenth,volume),
        
        (NOTE_C4,sixteenth,volume),
        (NOTE_C4,sixteenth,volume),
        (NOTE_C4,sixteenth,volume),
        (NOTE_C4,sixteenth,volume)
    ]}
]

volume = 120
music_frames_map[(len(music_frames_map),melodic_tom)] = [
    {'number_of_cycles': 3,
    'music': [
        (NOTE_C4,quarter,volume),
        (REST,0.75,volume)
    ]}
]

