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
    
    
def add_chord(midi_file, track, channel, time, volume, chord, durations):
    for duration in durations:
        if type(duration) == tuple: #rest
            duration = duration[1]  #the "sound of silence"
        else: #duration is a number of some kind
            for note in chord:
                midi_file.addNote(track, channel, note, time, duration, volume)
        time += duration
    return time
    
    
###############################################################################
# major chords - first set for convenience and backward capacity
a_major_chord = get_major_chord(notes.NOTE_A4)
b_major_chord = get_major_chord(notes.NOTE_B4)
c_major_chord = get_major_chord(notes.NOTE_C4)
d_major_chord = get_major_chord(notes.NOTE_D4)
e_major_chord = get_major_chord(notes.NOTE_E4)
f_major_chord = get_major_chord(notes.NOTE_F4)
g_major_chord = get_major_chord(notes.NOTE_G4)

#################################################
# octave 2 major chords
a2_major_chord = get_major_chord(notes.NOTE_A2)
b2_major_chord = get_major_chord(notes.NOTE_B2)
c2_major_chord = get_major_chord(notes.NOTE_C2)
d2_major_chord = get_major_chord(notes.NOTE_D2)
e2_major_chord = get_major_chord(notes.NOTE_E2)
f2_major_chord = get_major_chord(notes.NOTE_F2)
g2_major_chord = get_major_chord(notes.NOTE_G2)

A2_c = a2_major_chord
B2_c = b2_major_chord
C2_c = c2_major_chord
D2_c = d2_major_chord
E2_c = e2_major_chord
F2_c = f2_major_chord
G2_c = g2_major_chord

#################################################
# octave 3 major chords
a3_major_chord = get_major_chord(notes.NOTE_A3)
b3_major_chord = get_major_chord(notes.NOTE_B3)
c3_major_chord = get_major_chord(notes.NOTE_C3)
d3_major_chord = get_major_chord(notes.NOTE_D3)
e3_major_chord = get_major_chord(notes.NOTE_E3)
f3_major_chord = get_major_chord(notes.NOTE_F3)
g3_major_chord = get_major_chord(notes.NOTE_G3)

A3_c = a3_major_chord
B3_c = b3_major_chord
C3_c = c3_major_chord
D3_c = d3_major_chord
E3_c = e3_major_chord
F3_c = f3_major_chord
G3_c = g3_major_chord

#################################################
# octave 4 major chords
a4_major_chord = get_major_chord(notes.NOTE_A4)
b4_major_chord = get_major_chord(notes.NOTE_B4)
c4_major_chord = get_major_chord(notes.NOTE_C4)
d4_major_chord = get_major_chord(notes.NOTE_D4)
e4_major_chord = get_major_chord(notes.NOTE_E4)
f4_major_chord = get_major_chord(notes.NOTE_F4)
g4_major_chord = get_major_chord(notes.NOTE_G4)

A4_c = a4_major_chord
B4_c = b4_major_chord
C4_c = c4_major_chord
D4_c = d4_major_chord
E4_c = e4_major_chord
F4_c = f4_major_chord
G4_c = g4_major_chord

#################################################
# octave 5 major chords
a5_major_chord = get_major_chord(notes.NOTE_A5)
b5_major_chord = get_major_chord(notes.NOTE_B5)
c5_major_chord = get_major_chord(notes.NOTE_C5)
d5_major_chord = get_major_chord(notes.NOTE_D5)
e5_major_chord = get_major_chord(notes.NOTE_E5)
f5_major_chord = get_major_chord(notes.NOTE_F5)
g5_major_chord = get_major_chord(notes.NOTE_G5)

A5_c = a5_major_chord
B5_c = b5_major_chord
C5_c = c5_major_chord
D5_c = d5_major_chord
E5_c = e5_major_chord
F5_c = f5_major_chord
G5_c = g5_major_chord

#################################################
# octave 6 major chords
a6_major_chord = get_major_chord(notes.NOTE_A6)
b6_major_chord = get_major_chord(notes.NOTE_B6)
c6_major_chord = get_major_chord(notes.NOTE_C6)
d6_major_chord = get_major_chord(notes.NOTE_D6)
e6_major_chord = get_major_chord(notes.NOTE_E6)
f6_major_chord = get_major_chord(notes.NOTE_F6)
g6_major_chord = get_major_chord(notes.NOTE_G6)

A6_c = a6_major_chord
B6_c = b6_major_chord
C6_c = c6_major_chord
D6_c = d6_major_chord
E6_c = e6_major_chord
F6_c = f6_major_chord
G6_c = g6_major_chord



###############################################################################
# minor chords - first set for convenience and backward capacity
a_minor_chord = get_minor_chord(notes.NOTE_A4)
b_minor_chord = get_minor_chord(notes.NOTE_B4)
c_minor_chord = get_minor_chord(notes.NOTE_C4)
d_minor_chord = get_minor_chord(notes.NOTE_D4)
e_minor_chord = get_minor_chord(notes.NOTE_E4)
f_minor_chord = get_minor_chord(notes.NOTE_F4)
g_minor_chord = get_minor_chord(notes.NOTE_G4)

#################################################
# octave 2 minor chords
a2_minor_chord = get_minor_chord(notes.NOTE_A2)
b2_minor_chord = get_minor_chord(notes.NOTE_B2)
c2_minor_chord = get_minor_chord(notes.NOTE_C2)
d2_minor_chord = get_minor_chord(notes.NOTE_D2)
e2_minor_chord = get_minor_chord(notes.NOTE_E2)
f2_minor_chord = get_minor_chord(notes.NOTE_F2)
g2_minor_chord = get_minor_chord(notes.NOTE_G2)

a2_c = a2_minor_chord
b2_c = b2_minor_chord
c2_c = c2_minor_chord
d2_c = d2_minor_chord
e2_c = e2_minor_chord
f2_c = f2_minor_chord
g2_c = g2_minor_chord

#################################################
# octave 3 minor chords
a3_minor_chord = get_minor_chord(notes.NOTE_A3)
b3_minor_chord = get_minor_chord(notes.NOTE_B3)
c3_minor_chord = get_minor_chord(notes.NOTE_C3)
d3_minor_chord = get_minor_chord(notes.NOTE_D3)
e3_minor_chord = get_minor_chord(notes.NOTE_E3)
f3_minor_chord = get_minor_chord(notes.NOTE_F3)
g3_minor_chord = get_minor_chord(notes.NOTE_G3)

a3_c = a3_minor_chord
b3_c = b3_minor_chord
c3_c = c3_minor_chord
d3_c = d3_minor_chord
e3_c = e3_minor_chord
f3_c = f3_minor_chord
g3_c = g3_minor_chord

#################################################
# octave 4 minor chords
a4_minor_chord = get_minor_chord(notes.NOTE_A4)
b4_minor_chord = get_minor_chord(notes.NOTE_B4)
c4_minor_chord = get_minor_chord(notes.NOTE_C4)
d4_minor_chord = get_minor_chord(notes.NOTE_D4)
e4_minor_chord = get_minor_chord(notes.NOTE_E4)
f4_minor_chord = get_minor_chord(notes.NOTE_F4)
g4_minor_chord = get_minor_chord(notes.NOTE_G4)

a4_c = a4_minor_chord
b4_c = b4_minor_chord
c4_c = c4_minor_chord
d4_c = d4_minor_chord
e4_c = e4_minor_chord
f4_c = f4_minor_chord
g4_c = g4_minor_chord

#################################################
# octave 5 minor chords
a5_minor_chord = get_minor_chord(notes.NOTE_A5)
b5_minor_chord = get_minor_chord(notes.NOTE_B5)
c5_minor_chord = get_minor_chord(notes.NOTE_C5)
d5_minor_chord = get_minor_chord(notes.NOTE_D5)
e5_minor_chord = get_minor_chord(notes.NOTE_E5)
f5_minor_chord = get_minor_chord(notes.NOTE_F5)
g5_minor_chord = get_minor_chord(notes.NOTE_G5)

a5_c = a5_minor_chord
b5_c = b5_minor_chord
c5_c = c5_minor_chord
d5_c = d5_minor_chord
e5_c = e5_minor_chord
f5_c = f5_minor_chord
g5_c = g5_minor_chord

#################################################
# octave 6 minor chords
a6_minor_chord = get_minor_chord(notes.NOTE_A6)
b6_minor_chord = get_minor_chord(notes.NOTE_B6)
c6_minor_chord = get_minor_chord(notes.NOTE_C6)
d6_minor_chord = get_minor_chord(notes.NOTE_D6)
e6_minor_chord = get_minor_chord(notes.NOTE_E6)
f6_minor_chord = get_minor_chord(notes.NOTE_F6)
g6_minor_chord = get_minor_chord(notes.NOTE_G6)

a6_c = a6_minor_chord
b6_c = b6_minor_chord
c6_c = c6_minor_chord
d6_c = d6_minor_chord
e6_c = e6_minor_chord
f6_c = f6_minor_chord
g6_c = g6_minor_chord

"""###############################################################################
# major chord shorthands
A_c = a_major_chord
B_c = b_major_chord
C_c = c_major_chord
D_c = d_major_chord
E_c = e_major_chord
F_c = f_major_chord
G_c = g_major_chord

###############################################################################
# minor chord shorthands
a_c = a_minor_chord
b_c = b_minor_chord
c_c = c_minor_chord
d_c = d_minor_chord
e_c = e_minor_chord
f_c = f_minor_chord
g_c = g_minor_chord"""

###############################################################################
# chord_progression
chord_progression_CFG  = [c_major_chord, f_major_chord, g_major_chord]
chord_progression_CGaF = [c_major_chord, g_major_chord, a_minor_chord, f_major_chord] #most popular
chord_progression_GeaD = [g_major_chord, e_minor_chord, a_minor_chord, d_major_chord]
chord_progression_aFCG = [a_minor_chord, f_major_chord, c_major_chord, g_major_chord] #sad: Am F C G
chord_progression_CFGF = [c_major_chord, f_major_chord, g_major_chord, f_major_chord]
chord_progression_CaFG = [c_major_chord, a_minor_chord, f_major_chord, g_major_chord] #sad
chord_progression_CFGda = [c_major_chord, f_major_chord, g_major_chord, d_minor_chord, d_major_chord]

chord_progression_EADGBE = [e_major_chord, a_major_chord, d_major_chord, g_major_chord, b_major_chord, e_major_chord] #sound of silence
chord_progression_eadgbe = chord_progression_eadgbe = [e_minor_chord, a_minor_chord, d_minor_chord, g_minor_chord, b_minor_chord, e_minor_chord] #sound of silence

#https://www.thedawstudio.com/chord-progression-example-let-it-be-by-the-beatles/
chord_progression_let_it_be = [c_major_chord, g_major_chord, a_major_chord, f_major_chord, c_major_chord, g_major_chord, f_major_chord, c_major_chord, a_major_chord, g_major_chord, f_major_chord, c_major_chord, c_major_chord, g_major_chord, f_major_chord, c_major_chord]

#emotional 
#Em – D – C – G – G/F#
#chord_progression_eDCGG = [e_minor_chord, d_major_chord, c_major_chord, g_major_chord, g_major_chord]


#happy
chord_progression_GCD = [g_major_chord, c_major_chord, d_major_chord]



if __name__ == '__main__':
    from midiutil import MIDIFile
    
    #                  W  W  H  W  W  W  H
    #major_steps = [0, 2, 2, 1, 2, 2, 2, 1]
    #major_degrees = [base_note + sum(major_steps[0:s_idx+1]) for s_idx in range(len(major_steps))] # MIDI note number MAJOR

    #                  W  H  W  W  H  W  W
    #minor_steps = [0, 2, 1, 2, 2, 1, 2, 2]
    #minor_degrees = [base_note + sum(minor_steps[0:s_idx+1]) for s_idx in range(len(major_steps))] # MIDI note number MAJOR

    chords = chord_progression_CGaF #chord_progression_CFGda
    #chords = [c_major_chord, f_major_chord]
    tempo = 120
    
    
    number_of_tracks = 1
    midi_file = MIDIFile(number_of_tracks)
    midi_file.addTempo(track=0, time=0, tempo=tempo)
    
    time = 0
    track, channel = 0,0
    volume = 100
    #duration = notes.whole
    durations = [notes.quarter, ('rest',notes.quarter), notes.half]
    sum_durations = 1.0 #sum(durations)
    for chord in chords:
        #add_chord(midi_file,track, channel, time, volume, chord, [duration])
        #add_chord(midi_file,track, channel, time, volume, chord, [duration/8]*8)
        #add_chord(midi_file,track, channel, time, volume, chord, durations)
        #time = time + sum_durations
        
        
        add_chord(midi_file,track, channel, time+0, volume, chord, durations)
        add_chord(midi_file,track, channel, time+1, volume, chord, durations)
        add_chord(midi_file,track, channel, time+2, volume, chord, durations)
        add_chord(midi_file,track, channel, time+3, volume, chord, durations)
        time += 4
        
    with open('chord_sample.mid', 'wb') as output_file:
        midi_file.writeFile(output_file)