
from notes import *
from chords import *
from midi_instrument_numbers import *
import music_functions

#add more configuration

#https://beatsure.com/common-drum-beats/#standard
SONG_NAME = 'Troubled with Yourself'

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



# Even in light - It can still be dark, 
# when you’re troubled - with yourself
# Sitting alone - watching the walls, 
# a misplaced toy - upon the shelf

# A square peg - among round holes
# trying to find - a fit
# Applying to jobs - learning a language
# every rejection - a solid hit

# We get back up - mount the horse,
# try again - one more time
# Reassuring yourself - it's not the destination,
# rather - it's the climb

# Only through struggle - only through grind
# can a man - really grow
# Improving yourself - building character
# challenges - that I know

# Appreciated and - cherished are
# the blessings - I’ve acquired
# But make no mistake - they only come  
# through challenges - transpired


music_frames_map = {}

######################################################################################
# basic rythm keeping us on track
volume_piano = 100
music_frames_map[(len(music_frames_map),acoustic_grand_piano)] = [
    {'number_of_cycles': 1,                     #INTRO
    'music': [
        (a_minor_chord,whole,volume_piano),
        (f_major_chord,whole,volume_piano),
        (c_major_chord,whole,volume_piano),
        (g_major_chord,whole,volume_piano),
    ]},
    
    {'number_of_cycles': 1,                     #DRUMS in
    'music': [
        (REST, 2.0, volume_piano)
    ]},
    
    {'number_of_cycles': 5,
    'music': [
        (a_minor_chord,whole,volume_piano),   # 1, 2 bars
        (a_minor_chord,whole,volume_piano),   # 3, 4
        
        (f_major_chord,whole,volume_piano),   # 5, 6
        (f_major_chord,whole,volume_piano),   # 7, 8
        
        (c_major_chord,whole,volume_piano),   # 9, 10
        (c_major_chord,whole,volume_piano),   # 11, 12
        
        (g_major_chord,whole,volume_piano),   # 13, 14
        (g_major_chord,whole,volume_piano),   # 15, 16
    ]}
]

volume_strings = 60
music_frames_map[(len(music_frames_map),synthstrings_2)] = [
    {'number_of_cycles': 1,                     #INTRO
    'music': [
        (a_minor_chord,whole,volume_strings),
        (f_major_chord,whole,volume_strings),
        (c_major_chord,whole,volume_strings),
        (g_major_chord,whole,volume_strings),
    ]},
    
    {'number_of_cycles': 1,                     #DRUMS in
    'music': [
        (REST, 2.0, volume_strings)
    ]},
    
    {'number_of_cycles': 5,
    'music': [
        (a_minor_chord,whole,volume_strings),   # 1, 2 bars
        (a_minor_chord,whole,volume_strings),   # 3, 4
        
        (f_major_chord,whole,volume_strings),   # 5, 6
        (f_major_chord,whole,volume_strings),   # 7, 8
        
        (c_major_chord,whole,volume_strings),   # 9, 10
        (c_major_chord,whole,volume_strings),   # 11, 12
        
        (g_major_chord,whole,volume_strings),   # 13, 14
        (g_major_chord,whole,volume_strings),   # 15, 16
    ]}
]

"""volume_drums = 50
music_frames_map[(len(music_frames_map),taiko_drum)] = [
    {'number_of_cycles': 1,
    'music': [
        (REST, 4.0, volume_drums)
    ]},
    
    {'number_of_cycles': 1,
    'music': [
        (NOTE_A4,quarter,volume_drums),
        (REST, eigth, volume_drums),
        
        (NOTE_C5,quarter,volume_drums),
        (REST, eigth, volume_drums),
        
        (NOTE_E5,quarter,volume_drums),
        (REST, eigth, volume_drums),
        
        (NOTE_A4,quarter,volume_drums),
        (REST, eigth, volume_drums),
        
        (REST, half, volume_drums),
    ]},
    
    {'number_of_cycles': 5,
    'music': [
        (a_minor_chord,quarter,volume_drums),   # 1, 2 bars
        #(REST, 0.75, volume_drums),
        (a_minor_chord,whole,volume_drums),   # 3, 4
        #(REST, 0.75, volume_drums),
        
        (f_major_chord,whole,volume_drums),   # 5, 6
        (f_major_chord,whole,volume_drums),   # 7, 8
        
        (c_major_chord,whole,volume_drums),   # 9, 10
        (c_major_chord,whole,volume_drums),   # 11, 12
        
        (g_major_chord,whole,volume_drums),   # 13, 14
        (g_major_chord,whole,volume_drums),   # 15, 16
    ]}
]"""

