# https://blog.landr.com/common-chord-progressions/#:~:text=I%2DV%2Dvi%2DIV&text=This%20progression%20is%20called%20%E2%80%9Cthe,like%20a%20fresh%20emotional%20statement.

import notes

# The major chord contains the 1st, 3rd, and 5th notes of a major scale
# The notes of a C major chord are the 
#   1st C note - (the root note) ... 60
#   3rd E note                   ... 64
#   5th G note                   ... 67
def get_major_chord(n):
    return [n, n+4, n+7]
    
    
def get_minor_chord(n):
    return [n, n+3, n+7]

a_major_chord = get_major_chord(notes.NOTE_A4)
b_major_chord = get_major_chord(notes.NOTE_B4)
c_major_chord = get_major_chord(notes.NOTE_C4)
d_major_chord = get_major_chord(notes.NOTE_D4)
e_major_chord = get_major_chord(notes.NOTE_E4)
f_major_chord = get_major_chord(notes.NOTE_F4)
g_major_chord = get_major_chord(notes.NOTE_G4)

a_minor_chord = get_minor_chord(notes.NOTE_A4)
b_minor_chord = get_minor_chord(notes.NOTE_B4)
c_minor_chord = get_minor_chord(notes.NOTE_C4)
d_minor_chord = get_minor_chord(notes.NOTE_D4)
e_minor_chord = get_minor_chord(notes.NOTE_E4)
f_minor_chord = get_minor_chord(notes.NOTE_F4)
g_minor_chord = get_minor_chord(notes.NOTE_G4)


chord_progression_CFG  = [c_major_chord, f_major_chord, g_major_chord]
chord_progression_CGaF = [c_major_chord, g_major_chord, a_minor_chord, f_major_chord] #most popular
chord_progression_GeaD = [g_major_chord, e_minor_chord, a_minor_chord, d_major_chord]
chord_progression_aFCG = [a_minor_chord, f_major_chord, c_major_chord, g_major_chord] #sad: Am F C G
chord_progression_CFGF = [c_major_chord, f_major_chord, g_major_chord, f_major_chord]
chord_progression_CaFG = [c_major_chord, a_minor_chord, f_major_chord, g_major_chord] #sad

chord_progression_EADGBE = [e_major_chord, a_major_chord, d_major_chord, g_major_chord, b_major_chord, e_major_chord] #sound of silence
chord_progression_eadgbe = chord_progression_eadgbe = [e_minor_chord, a_minor_chord, d_minor_chord, g_minor_chord, b_minor_chord, e_minor_chord] #sound of silence

#https://www.thedawstudio.com/chord-progression-example-let-it-be-by-the-beatles/
chord_progression_let_it_be = [c_major_chord, g_major_chord, a_major_chord, f_major_chord, c_major_chord, g_major_chord, f_major_chord, c_major_chord, a_major_chord, g_major_chord, f_major_chord, c_major_chord, c_major_chord, g_major_chord, f_major_chord, c_major_chord]

#emotional 
#Em – D – C – G – G/F#
#chord_progression_eDCGG = [e_minor_chord, d_major_chord, c_major_chord, g_major_chord, g_major_chord]


#happy
chord_progression_GCD = [g_major_chord, c_major_chord, d_major_chord]
