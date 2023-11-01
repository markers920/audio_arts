
from notes import *
from chords import *
from midi_instrument_numbers import *
import music_functions

#add more configuration

#https://beatsure.com/common-drum-beats/#standard
SONG_NAME = 'SHORT_SAMPLES'

tempo = 60

#(NOTE_C4,quarter,volume), (NOTE_C4,quarter,volume), (NOTE_C4,quarter,volume)
# chord_progression_CGaF

# C - c_major_chord - [C4 (60), E4 (64), G (67)]
# G - g_major_chord - [G4 (67), B4 (71), D5 (74)]
# a - a_minor_chord - [A4 (69), C5 (72), E5 (76)]
# F - f_major_chord - [F4 (65), A4 (69), C5 (72)]

# I–V–vi–IV :   C–G–Am–F
# V–vi–IV–I :   G–Am–F–C
# vi–IV–I–V :   Am–F–C–G
# IV–I–V–vi :   F–C–G–Am


music_frames_map = {}

######################################################################################

volume = 100
#synthstrings_2
music_frames_map[(len(music_frames_map),acoustic_grand_piano)] = [
    {'number_of_cycles': 1,
    'music': [
        (C4_c,whole,volume),
        (G4_c,whole,volume),
        (a4_c,whole,volume),
        (F4_c,whole,volume),
        
        
        
        
        (a_minor_chord,whole,volume),   # 3, 4
        
    ]}
]

