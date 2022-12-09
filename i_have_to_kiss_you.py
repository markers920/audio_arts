
from notes import *
from chords import *
from midi_instrument_numbers import *
import music_functions

#add more configuration

SONG_NAME = 'I Have to Kiss You'

tempo = 60

#(NOTE_C4,quarter,volume), (NOTE_C4,quarter,volume), (NOTE_C4,quarter,volume)
# chord_progression_CGaF

# C - c_major_chord - [C4 (60), E4 (64), G (67)]
# G - g_major_chord - [G4 (67), B4 (71), D5 (74)]
# a - a_minor_chord - [A4 (69), C5 (72), E5 (76)]
# F - f_major_chord - [F4 (65), A4 (69), C5 (72)]


def get_chorus(volume):
    chorus = [
        #this was sum to 4
        #"now - I have to kiss you tonight" - 'I ', 'ha', 've ', 'to ', 'kis', 's y', 'o', 'u', ' ', 'to', 'night"'
        #(NOTE_F4,quarter,volume), (NOTE_A4,quarter,volume), (NOTE_A4,quarter,volume), (NOTE_C5,quarter,volume), # 'I ', 'ha', 've ', 'to ', 
        #(NOTE_C5,half,volume), (NOTE_A4,half,volume),                                                           # 'kis', 's y', 'o', 'u', ' ', 
        #(f_major_chord,half,volume), (f_major_chord,half,volume),                                               #'to', 'night"'
        #(REST,whole,volume),#1
        
        #"I have to kiss you" - 'I ', 'ha', 've ', 'to ', 'kis', 's y', 'o', 'u'
        #(f_major_chord,half,volume),                                   # I 
        #(REST,eigth,volume),
        #(NOTE_F4,half,volume), (NOTE_F4,quarter,volume),             #'ha', 've ', 'to ',  (need to)
        #(REST,eigth,volume),
        #([NOTE_F4, NOTE_A4, NOTE_C5, NOTE_F5, NOTE_A5],half,volume),                                    #kiss
        #(f_major_chord,half,volume),   # you
        #(REST,eigth,volume),
        #(NOTE_F4,half,volume), (NOTE_A4,whole,volume),                                      #'to', 'night"'
        #(REST,whole,volume),#1
        
        #(NOTE_C4,quarter,volume), (NOTE_E4,quarter,volume), (NOTE_G4,quarter,volume), (c_major_chord,quarter,volume),
        #(NOTE_G4,quarter,volume), (NOTE_B4,quarter,volume), (NOTE_D4,quarter,volume), (g_major_chord,quarter,volume),
        #(NOTE_A4,quarter,volume), (NOTE_C4,quarter,volume), (NOTE_E4,quarter,volume), (a_minor_chord,quarter,volume),
        #(NOTE_F4,quarter,volume), (NOTE_A4,quarter,volume), (NOTE_C4,quarter,volume), (f_major_chord,quarter,volume)
        
        
        #sum to 4
        #(NOTE_C4,quarter,volume), (c_major_chord,half,volume), (REST,eigth,volume), #(NOTE_G4,quarter,volume), (c_major_chord,half,volume),
        #(NOTE_G4,quarter,volume), (g_major_chord,half,volume), (REST,eigth,volume), #(NOTE_D4,quarter,volume), (g_major_chord,quarter,volume),
        #(NOTE_A4,quarter,volume), (a_minor_chord,half,volume), (REST,eigth,volume), #(NOTE_E4,quarter,volume), (a_minor_chord,quarter,volume),
        #(NOTE_F4,quarter,volume), (f_major_chord,half,volume),
        #(REST,3*eigth + quarter,volume)
        
        #sum to 4
        (NOTE_C4,quarter,volume), ([NOTE_C4, NOTE_G4],half,volume), (REST,eigth,volume), #(NOTE_G4,quarter,volume), (c_major_chord,half,volume),
        (NOTE_G4,quarter,volume), ([NOTE_G4, NOTE_D5],half,volume), (REST,eigth,volume), #(NOTE_D4,quarter,volume), (g_major_chord,quarter,volume),
        (NOTE_A4,quarter,volume), ([NOTE_A4, NOTE_E5],half,volume), (REST,eigth,volume), #(NOTE_E4,quarter,volume), (a_minor_chord,quarter,volume),
        (NOTE_F4,quarter,volume), (f_major_chord,half,volume),
        (REST,3*eigth + quarter,volume)
    ]
    return chorus

#chorus_rest = [(REST,4.0,volume)]
chorus_rest = [c for c in get_chorus(0)]




music_frames_map = {}

######################################################################################
# basic rythm keeping us on track
volume = 20
music_frames_map[(len(music_frames_map),woodblock)] = [
    {'number_of_cycles': 1,                 
    'music': [(NOTE_C4,quarter,volume)]*(25*4)
    }
]


######################################################################################
# strings/voices adding some bulk
volume = 60
music_frames_map[(len(music_frames_map),string_ensemble_1)] = [
    {'number_of_cycles': 1,     #block lead in            
    'music': [
        (REST,whole,volume),
    ]},
    
    {'number_of_cycles': 1,     #chorus
    'music': get_chorus(volume)
    },
    
    {'number_of_cycles': 1,                 
    'music': [
        (c_major_chord,3.75,volume), (REST,0.25,volume),    #sum 4
        (g_major_chord,3.75,volume), (REST,0.25,volume),    #sum 4
        (a_minor_chord,3.75,volume), (REST,0.25,volume),    #sum 4
        (f_major_chord,3.75,volume), (REST,0.25,volume),    #sum 4
    ]},
    
    {'number_of_cycles': 1,                 
    'music': get_chorus(volume)
    },
]


volume = 60
music_frames_map[(len(music_frames_map),string_ensemble_2)] = [
    {'number_of_cycles': 1,     #block lead in            
    'music': [
        (REST,whole,volume),
    ]},
    
    {'number_of_cycles': 1,     #chorus
    'music': get_chorus(volume)
    },
    
    {'number_of_cycles': 1,                 
    'music': [
        (c_major_chord,3.95,volume), (REST,0.05,volume),    #sum 4
        (g_major_chord,3.95,volume), (REST,0.05,volume),    #sum 4
        (a_minor_chord,3.95,volume), (REST,0.05,volume),    #sum 4
        (f_major_chord,3.95,volume), (REST,0.05,volume),    #sum 4
    ]},
    
    {'number_of_cycles': 1,                 
    'music': get_chorus(volume)
    },
]

volume = 60
music_frames_map[(len(music_frames_map),synth_voice)] = [
    {'number_of_cycles': 1,     #block lead in            
    'music': [
        (REST,whole,volume),
    ]},
    
    {'number_of_cycles': 1,     #chorus
    'music': get_chorus(volume)
    },
    
    {'number_of_cycles': 1,                 
    'music': [
        (c_major_chord,4,volume),     #sum 4
        (g_major_chord,4,volume),     #sum 4
        (a_minor_chord,4,volume),     #sum 4
        (f_major_chord,4,volume),     #sum 4
    ]},
    
    {'number_of_cycles': 1,                 
    'music': get_chorus(volume)
    },
]

######################################################################################
# drums emphasize parts
volume = 80
music_frames_map[(len(music_frames_map),melodic_tom)] = [
    {'number_of_cycles': 1,     #block lead in
    'music': [
        (REST,whole,volume),
    ]},
    
    {'number_of_cycles': 1,     #chorus
    'music': get_chorus(volume)
    },
    
    {'number_of_cycles': 1,     #phrase
    'music': music_functions.get_full_score_from_sum(possible_tones=c_major_chord, possible_durations=[eigth,quarter,half], s=4, allow_rest=True, volume=volume, seed=1) #sum 4
    },
    
    {'number_of_cycles': 1,     #phrase
    'music': music_functions.get_full_score_from_sum(possible_tones=g_major_chord, possible_durations=[eigth,quarter,half], s=4, allow_rest=True, volume=volume, seed=2) #sum 4
    },
    
    {'number_of_cycles': 1,     #phrase
    'music': music_functions.get_full_score_from_sum(possible_tones=a_minor_chord, possible_durations=[eigth,quarter,half], s=4, allow_rest=True, volume=volume, seed=3) #sum 4
    },
    
    {'number_of_cycles': 1,     #phrase
    'music': music_functions.get_full_score_from_sum(possible_tones=f_major_chord, possible_durations=[eigth,quarter,half], s=4, allow_rest=True, volume=volume, seed=4) #sum 4
    },
    
    {'number_of_cycles': 1,                 
    'music': get_chorus(volume)
    },
]


volume = 80
music_frames_map[(len(music_frames_map),taiko_drum)] = [
    {'number_of_cycles': 1,     #block lead in
    'music': [
        (REST,whole,volume),
    ]},
    
    {'number_of_cycles': 1,     #chorus
    'music': get_chorus(volume)
    },
    
    {'number_of_cycles': 1,     #phrase
    'music': [
        (REST,4.0,volume),     #sum 4
        (REST,4.0,volume),     #sum 4
        (REST,4.0,volume),     #sum 4
        
        #sum 4 - drum lead into chorus
        (REST,1.5,volume),
        (REST,1.0,volume),
        #(REST,1.5,volume),
    ]},
    
    {'number_of_cycles': 1,     #phrase
    'music': music_functions.get_full_score_from_sum(possible_tones=f_major_chord, possible_durations=[eigth,quarter,half], s=1.5, allow_rest=False, volume=volume, seed=0)
    },
    
    {'number_of_cycles': 1,                 
    'music': get_chorus(volume)
    },
]


volume = 80
music_frames_map[(len(music_frames_map),tubular_bells)] = [
    {'number_of_cycles': 1,     #block lead in
    'music': [
        (REST,whole,volume),
    ]},
    
    {'number_of_cycles': 1,     #chorus
    'music': get_chorus(volume)
    },
    
    {'number_of_cycles': 1,     #phrase
    'music': [
        (c_major_chord,half,volume), (REST,3.5,volume),     #sum 4
        (g_major_chord,half,volume), (REST,3.5,volume),     #sum 4
        (a_major_chord,half,volume), (REST,3.5,volume),     #sum 4
        
        #sum 4 - drum lead into chorus
        (REST,1.5,volume),
        (REST,1.0,volume),
        #(REST,1.5,volume),
    ]},
    
    {'number_of_cycles': 1,     #phrase
    'music': music_functions.get_full_score_from_sum(possible_tones=f_major_chord, possible_durations=[eigth,quarter,half], s=1.5, allow_rest=False, volume=volume, seed=0)
    },
    
    {'number_of_cycles': 1,                 
    'music': get_chorus(volume)
    },
]


######################################################################################
#main voice
volume = 120
music_frames_map[(len(music_frames_map),acoustic_grand_piano)] = [# acoustic_grand_piano  electric_guitar_clean] = [#rock_organ] = [#reed_organ] = [#guitar_harmonics] = [#acoustic_grand_piano] = [
    {'number_of_cycles': 1,     #block lead in
    'music': [
        (REST,whole,volume),
    ]},
    
    {'number_of_cycles': 1,     #chorus
    'music': get_chorus(volume)
    },
    
    {'number_of_cycles': 1,                 
    'music': [
        # ------------------------------------------------------------------------------------------------------
        # C - c_major_chord - [C4 (60), E4 (64), G (67)]

        #she didn-t know--
        (c_major_chord,half,volume), (NOTE_E4,quarter,volume), (NOTE_E4,quarter,volume), (NOTE_G4,half,volume), # 1.5
        
        #how much her life 
        (NOTE_C4,quarter,volume), (NOTE_C4,quarter,volume), (NOTE_C4,quarter,volume), (NOTE_C4,quarter,volume), # 1
        
        #would change
        (c_major_chord,half,volume), (c_major_chord,half,volume), #1
        
        (REST,half,volume),
        
        # ------------------------------------------------------------------------------------------------------
        # G - g_major_chord - [G4 (67), B4 (71), D5 (74)]
        
        #He join-ed her
        (g_major_chord,half,volume), (NOTE_B4,half,volume), (NOTE_D5,half,volume), # 1.5
        
        #bea-uty and breath
        #(NOTE_G4,eigth,volume), (NOTE_G4,eigth,volume),          (NOTE_G4,quarter,volume),        (NOTE_G4,eigth,volume), (NOTE_G4,eigth,volume),       (NOTE_G4,eigth,volume), (NOTE_G4,eigth,volume), # 1
        (NOTE_G4,quarter,volume), (NOTE_G4,quarter,volume), (NOTE_G4,quarter,volume), (NOTE_G4,quarter,volume), # 1

        # so strange
        (g_major_chord,quarter,volume), (g_major_chord,half+quarter,volume), #1
        
        (REST,half,volume), #0.5
        
        # ------------------------------------------------------------------------------------------------------
        # a - a_minor_chord - [A4 (69), C5 (72), E5 (76)]
        
        # Echoing practiced word  -  'Echoin', 'g ',           'prac', 'ti', 'ce', 'd ',         'wor', 'd ', 
        (a_minor_chord,half,volume), (NOTE_C5,quarter,volume), (NOTE_C5,quarter,volume), (NOTE_E5,quarter,volume), (NOTE_E5,quarter,volume),# 1.5
        
        # to get the intonation  -  'to ', 'ge', 't t', 'he ', 'in', 'to', 'na', 'tio', 'n '
        (NOTE_A4,quarter,volume), (NOTE_A4,quarter,volume), (NOTE_A4,quarter,volume), (NOTE_A4,quarter,volume), # 1
        
        # right
        (a_minor_chord,whole,volume), #1
        
        (REST,half,volume),
        
        # ------------------------------------------------------------------------------------------------------
        # F - f_major_chord - [F4 (65), A4 (69), C5 (72)]
        
        # In the dark and still - ['In t', 'he ', 'dar', 'k an', ]
        (f_major_chord,half,volume), (NOTE_A4,quarter,volume), (NOTE_A4,quarter,volume), (NOTE_C5,quarter,volume), (NOTE_C5,quarter,volume), # 1.5
        
        # he whispered - 'he w', 'his', 'pe', 're', 'd ', '"', 
        (NOTE_F4,quarter,volume), (REST,quarter,volume), (NOTE_F4,half,volume), #1
        
        (REST,1.5,volume),
    ]},
    
    {'number_of_cycles': 1,                 
    'music': get_chorus(volume)
    },
]


"""volume = 20
music_frames_map[taiko_drum] = [
    {'number_of_cycles': 1,            
    'music': [
        (REST,whole,volume),
    ]},
    
    {'number_of_cycles': 3,                
    'music': [
        (NOTE_C4,quarter,volume), (NOTE_C4,quarter,volume), (NOTE_C4,quarter,volume), (NOTE_C4,quarter,volume), (NOTE_C4,half,volume), (NOTE_C4,quarter,volume), # 1.5
        (NOTE_C4,quarter,volume), (NOTE_C4,quarter,volume), (NOTE_C4,quarter,volume), (NOTE_C4,quarter,volume), # 1
        (NOTE_C4,quarter,volume), (NOTE_C4,quarter,volume), (NOTE_C4,quarter,volume), (NOTE_C4,quarter,volume), # 1
        (NOTE_C4,quarter,volume), (NOTE_C4,quarter,volume), (NOTE_C4,quarter,volume), (NOTE_C4,quarter,volume) # 1
    ]},
    
    {'number_of_cycles': 1,                 
    'music': [
        (NOTE_C4,quarter,volume), (NOTE_C4,quarter,volume), (NOTE_C4,quarter,volume), (NOTE_C4,quarter,volume), (NOTE_C4,half,volume), (NOTE_C4,quarter,volume), # 1.5
        (NOTE_C4,quarter,volume), (NOTE_C4,quarter,volume), (NOTE_C4,quarter,volume), (NOTE_C4,quarter,volume), # 1
        
        #piano rest
        (NOTE_F4,quarter,volume), (NOTE_C5,quarter,volume), (NOTE_F4,quarter,volume), (NOTE_A4,quarter,volume), 
        
        (NOTE_C4,quarter,volume), (NOTE_C4,quarter,volume), (NOTE_C4,quarter,volume), (NOTE_C4,quarter,volume), # 1
        (NOTE_C4,quarter,volume), (NOTE_C4,quarter,volume), (NOTE_C4,quarter,volume), (NOTE_C4,quarter,volume), # 1
    ]}
]"""





# she didn't know how much her life would change
# ['she ', 'didn', "'", 't ', 'kno', 'w ', 
#   'ho', 'w ', 'muc', 'h ', 'he', 'r ', 'li', 'fe ', 
#   'woul', 'd c', 'han', 'ge']

# He joined her unaware beauty and breath can be so strange
# ['He ', 'joi', 'ne', 'd ', 'he', 'r u', 'na', 'wa', 're ', 
# 'bea', 'u', 'ty ', 'an', 'd ', 'breat', 'h ', 
# 'ca', 'n ', 'be ', 'so s', 'tran', 'ge']

# Echoing practiced word to get the intonation right
# ['Echoin', 'g ', 'prac', 'ti', 'ce', 'd ', 'wor', 'd ', 'to ', 'ge', 't t', 'he ', 'in', 'to', 'na', 'tio', 'n ', 'right']

# In the dark and still he whispered "I have to kiss you tonight"
# ['In t', 'he ', 'dar', 'k an', 'he w', 'his', 'pe', 're', 'd ', '"', 'I ', 'ha', 've ', 'to ', 'kis', 's y', 'o', 'u', ' ', 'to', 'night"']



# Frozen and unsure Her face and neck flushed
# ['Fro', 'ze', 'n an', 'd un', 'su', 're ', 'He', 'r ', 'fa', 'ce ', 'an', 'd ', 'nec', 'k ', 'flus', 'hed']
# ...Finally that Easter friend was a man rushed
# ['.', '.', '', '.', 'Fi', 'nal', 'ly t', 'ha', 't E', 'as', 'te', 'r ', 'frien', 'd ', 'wa', 's a', ' ', 'ma', 'n ', 'rus', 'hed']
# Touched, rushed, crushed, hushed
# ['Touc', 'hed', ',', ' ', 'rus', 'hed', ',', ' ', 'crus', 'hed', ',', ' ', 'hus', 'hed']

# Against red leather it all felt so right
# ['Agains', 't ', 're', 'd ', 'leat', 'he', 'r i', 't al', 'l ', 'fel', 't ', 'so ', 'right']
# In his driveway - I have to kiss you tonight
# ['In ', 'hi', 's ', 'dri', 've', 'way', ' ', '-', ' I', ' ', 'ha', 've ', 'to ', 'kis', 's y', 'o', 'u', ' ', 'to', 'night']



# Only the crazy would start this during school
# ['Only t', 'he ', 'cra', 'zy ', 'woul', 'd s', 'tar', 't t', 'hi', 's ', 'du', 'rin', 'g sc', 'hool']
# But No one had told him that fool's rule
# ['Bu', 't ', 'No ', 'o', 'ne ', 'ha', 'd ', 'tol', 'd ', 'hi', 'm t', 'ha', 't ', 'fool', "'", 's ', 'ru', 'le']

# The middle of exams, grad schools height
# ['The ', 'mid', 'dle ', 'o', 'f e', 'xams', ',', ' ', 'gra', 'd sc', 'hool', 's ', 'height']
# Oh well, we're here, i have to kiss you tonight
# ['Oh ', 'well', ',', ' ', 'we', "'", 're ', 'he', 're', ',', ' i', ' ', 'ha', 've ', 'to ', 'kis', 's y', 'o', 'u', ' ', 'to', 'night']



# He and and others had known for so long
# ['He ', 'an', 'd an', 'd ot', 'her', 's ', 'ha', 'd ', 'know', 'n ', 'fo', 'r ', 'so ', 'long']
# And he hopes you feel it with every song
# ['And ', 'he ', 'ho', 'pe', 's y', 'o', 'u', ' ', 'fee', 'l i', 't ', 'wit', 'h e', 've', 'ry ', 'song']
# He'd held it back with a professional might

# ['He', "'", 'd ', 'hel', 'd i', 't ', 'bac', 'k ', 'wit', 'h a', ' ', 'pro', 'fes', 'sio', 'na', 'l ', 'might']
# But damn the job - i have to kiss you tonight
# ['Bu', 't ', 'dam', 'n t', 'he ', 'jo', 'b ', '-', ' i', ' ', 'ha', 've ', 'to ', 'kis', 's y', 'o', 'u', ' ', 'to', 'night']



# Around the world his heart she carrie-d
# ['Aroun', 'd t', 'he ', 'worl', 'd ', 'hi', 's ', 'hear', 't s', 'he ', 'car', 'rie', '-d']
# Far from settled down but happily married
# ['Fa', 'r ', 'fro', 'm ', 'set', 'tle', 'd ', 'dow', 'n ', 'bu', 't ', 'hap', 'pi', 'ly ', 'mar', 'ried']

# Fast forward through the bumps and fights
# ['Fas', 't ', 'for', 'war', 'd t', 'hroug', 'h t', 'he ', 'bum', 'ps an', 'd ', 'fights']
# As we lay down together - i have to kiss you tonight
# ['As ', 'we ', 'lay', ' ', 'dow', 'n ', 'to', 'get', 'he', 'r ', '-', ' i', ' ', 'ha', 've ', 'to ', 'kis', 's y', 'o', 'u', ' ', 'to', 'night']




"""{'number_of_cycles': 20,                 
'music': [
(c_major_chord,quarter,volume)
]},

{'number_of_cycles': 20,                 
'music': [
(g_major_chord,quarter,volume)
]},

{'number_of_cycles': 20,                 
'music': [
(a_minor_chord,quarter,volume)
]},

{'number_of_cycles': 20,                 
'music': [
(f_major_chord,quarter,volume)
]},"""




# She sat there not knowing how much her life would change
# ['She ', 'sa', 't t', 'he', 're ', 'no', 't ', 'kno', 'win', 'g ', 'ho', 'w ', 'muc', 'h ', 'he', 'r ', 'li', 'fe ', 'woul', 'd c', 'han', 'ge']
# He joined her unaware beauty and breath can be so strange
# ['He ', 'joi', 'ne', 'd ', 'he', 'r u', 'na', 'wa', 're ', 'bea', 'u', 'ty ', 'an', 'd ', 'breat', 'h ', 'ca', 'n ', 'be ', 'so s', 'tran', 'ge']

# Echoing practiced word to get the intonation right
# ['Echoin', 'g ', 'prac', 'ti', 'ce', 'd ', 'wor', 'd ', 'to ', 'ge', 't t', 'he ', 'in', 'to', 'na', 'tio', 'n ', 'right']
# In the dark and still he whispered "I have to kiss you tonight"
# ['In t', 'he ', 'dar', 'k an', 'he w', 'his', 'pe', 're', 'd ', '"', 'I ', 'ha', 've ', 'to ', 'kis', 's y', 'o', 'u', ' ', 'to', 'night"']



# Frozen and unsure Her face and neck flushed
# ['Fro', 'ze', 'n an', 'd un', 'su', 're ', 'He', 'r ', 'fa', 'ce ', 'an', 'd ', 'nec', 'k ', 'flus', 'hed']
# ...Finally that Easter friend was a man rushed
# ['.', '.', '', '.', 'Fi', 'nal', 'ly t', 'ha', 't E', 'as', 'te', 'r ', 'frien', 'd ', 'wa', 's a', ' ', 'ma', 'n ', 'rus', 'hed']
# Touched, rushed, crushed, hushed
# ['Touc', 'hed', ',', ' ', 'rus', 'hed', ',', ' ', 'crus', 'hed', ',', ' ', 'hus', 'hed']

# Against red leather it all felt so right
# ['Agains', 't ', 're', 'd ', 'leat', 'he', 'r i', 't al', 'l ', 'fel', 't ', 'so ', 'right']
# In his driveway - I have to kiss you tonight
# ['In ', 'hi', 's ', 'dri', 've', 'way', ' ', '-', ' I', ' ', 'ha', 've ', 'to ', 'kis', 's y', 'o', 'u', ' ', 'to', 'night']



# Only the crazy would start this during school
# ['Only t', 'he ', 'cra', 'zy ', 'woul', 'd s', 'tar', 't t', 'hi', 's ', 'du', 'rin', 'g sc', 'hool']
# But No one had told him that fool's rule
# ['Bu', 't ', 'No ', 'o', 'ne ', 'ha', 'd ', 'tol', 'd ', 'hi', 'm t', 'ha', 't ', 'fool', "'", 's ', 'ru', 'le']

# The middle of exams, grad schools height
# ['The ', 'mid', 'dle ', 'o', 'f e', 'xams', ',', ' ', 'gra', 'd sc', 'hool', 's ', 'height']
# Oh well, we're here, i have to kiss you tonight
# ['Oh ', 'well', ',', ' ', 'we', "'", 're ', 'he', 're', ',', ' i', ' ', 'ha', 've ', 'to ', 'kis', 's y', 'o', 'u', ' ', 'to', 'night']



# He and and others had known for so long
# ['He ', 'an', 'd an', 'd ot', 'her', 's ', 'ha', 'd ', 'know', 'n ', 'fo', 'r ', 'so ', 'long']
# And he hopes you feel it with every song
# ['And ', 'he ', 'ho', 'pe', 's y', 'o', 'u', ' ', 'fee', 'l i', 't ', 'wit', 'h e', 've', 'ry ', 'song']
# He'd held it back with a professional might

# ['He', "'", 'd ', 'hel', 'd i', 't ', 'bac', 'k ', 'wit', 'h a', ' ', 'pro', 'fes', 'sio', 'na', 'l ', 'might']
# But damn the job - i have to kiss you tonight
# ['Bu', 't ', 'dam', 'n t', 'he ', 'jo', 'b ', '-', ' i', ' ', 'ha', 've ', 'to ', 'kis', 's y', 'o', 'u', ' ', 'to', 'night']



# Around the world his heart she carrie-d
# ['Aroun', 'd t', 'he ', 'worl', 'd ', 'hi', 's ', 'hear', 't s', 'he ', 'car', 'rie', '-d']
# Far from settled down but happily married
# ['Fa', 'r ', 'fro', 'm ', 'set', 'tle', 'd ', 'dow', 'n ', 'bu', 't ', 'hap', 'pi', 'ly ', 'mar', 'ried']

# Fast forward through the bumps and fights
# ['Fas', 't ', 'for', 'war', 'd t', 'hroug', 'h t', 'he ', 'bum', 'ps an', 'd ', 'fights']
# As we lay down together - i have to kiss you tonight
# ['As ', 'we ', 'lay', ' ', 'dow', 'n ', 'to', 'get', 'he', 'r ', '-', ' i', ' ', 'ha', 've ', 'to ', 'kis', 's y', 'o', 'u', ' ', 'to', 'night']