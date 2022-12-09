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