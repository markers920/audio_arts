
from notes import *

#add more configuration

SONG_NAME = 'I Have to Kiss You'

volume = 100

# thinking out loud
# https://tabs.ultimate-guitar.com/tab/ed-sheeran/thinking-out-loud-chords-1486860
# C     - 
# C/E   -
# F     - 
# G     - 
# Dm    - 
# Am    - 

#8 beats per phrase
#(NOTE_C4,quarter,volume), (NOTE_C4,quarter,volume), (NOTE_C4,quarter,volume)

music_frames = [
    {'number_of_cycles': 1,                 
    'music': [
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
    ]},
    
]



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