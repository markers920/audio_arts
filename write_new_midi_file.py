
# https://www.inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies
# The formula connecting the MIDI note number and the base frequency - 
# assuming equal tuning based on A4=a'=440 Hz - is:
# f = 440 * 2^((n−69)/12)

# https://music.utk.edu/theorycomp/courses/murphy/documents/Major+MinorScales.pdf
# https://blog.landr.com/common-chord-progressions/


#issues with midi2audio writing mp3 files
#https://github.com/FluidSynth/fluidsynth/wiki/Download
# choco install fluidsynth

from midiutil import MIDIFile
import random
from datetime import datetime

import notes
import midi_instrument_numbers

random.seed(1989) #datetime.now()) #1987






#W W H W W W H
# whole whole half whole whole whole half
# 2     2     1    2     2     2     1
def get_major_scale_from_start(n):
    #adds = [0,2,2,1,2,2,2,1]
    adds = [0,2,4,5,7,9,11,12]
    return [n+a for a in adds]
    
    
#W H W W H W W
#2,1,2,2,1,2,2
def get_minor_scale_from_start(n):
    #adds = [0,2,1,2,2,1,2,2]
    adds = [0,2,3,5,7,8,10,12]
    return [n+a for a in adds]
    
    
# The major chord contains the 1st, 3rd, and 5th notes of a major scale
# The notes of a C major chord are the 
#   1st C note - (the root note) ... 60
#   3rd E note                   ... 64
#   5th G note                   ... 67
def get_major_chord(n):
    return [n, n+4, n+7]
    
    
def get_minor_chord(n):
    return [n, n+3, n+7]
    
    
def add_scale_c_major(midi_file,time):
    scale_c_major = get_major_scale_from_start(notes.NOTE_C4)
    for pitch in scale_c_major:
        midi_file.addNote(track, channel, pitch, time, duration, volume)
        time = time + 1
    return time


def add_scale_c_minor(midi_file,time):
    scale_c_minor = get_minor_scale_from_start(notes.NOTE_C4)
    for pitch in scale_c_minor:
        midi_file.addNote(track, channel, pitch, time, duration, volume)
        time = time + 1
    return time
    
    
def add_chord(midi_file, track, channel, time, volume, chord, durations):
    for duration in durations:
        if type(duration) == tuple: #rest
            duration = duration[1]  #the "sound of silence"
        else: #duration is a number of some kind
            for note in chord:
                midi_file.addNote(track, channel, note, time, duration, volume)
        time += duration
    return time
    
    
def pick_at_chord(midi_file, track, channel, time, volume, chord, durations):
    #TODO break up beats into quarter/half/whole notes
    for duration in durations:
        if type(duration) == tuple: #rest
            duration = duration[1]  #the sound of silence
        else:
            note = random.choice(chord)
            midi_file.addNote(track, channel, note, time, duration, volume)
        time += duration
    return time
    
    
def get_durations_from_sum(possible_durations, s, allow_rest=None):
    ret = []
    while len(ret) <= 0  or sum(ret) < s:
        #print(ret, sum(ret), s)
        d = random.choice(possible_durations)
        if (sum(ret) + d) <= s:
            if allow_rest != None and random.random() < allow_rest:
                d = ('rest',d)
            ret.append(d)
    return ret




def main():

    #track = 0
    #channel = 0
    
    duration = 1 # In beats
    tempo = 120 #120 # In BPM
    volume = 127 # 0-127, as per the MIDI standard
    
    beats_per_measure = 4
    
    possible_durations = sorted([1,2,4,0.5,0.25,0.125])
    
    #midi_file = MIDIFile(1) # One track, defaults to format 1 (tempo track automatically created)
    #midi_file = MIDIFile(2, adjust_origin=False)
    #midi_file = MIDIFile(4, adjust_origin=False)
    
    number_of_tracks = 3
    midi_file = MIDIFile(number_of_tracks)
    midi_file.addTempo(track=0, time=0, tempo=tempo)
    
    for track_index in range(3):
        midi_file.addTempo(track_index, track_index, tempo) #(track,time,tempo) ... track=0, time = 0
    
    
    
    
    c_major_chord = get_major_chord(notes.NOTE_C4)
    d_major_chord = get_major_chord(notes.NOTE_D4)
    f_major_chord = get_major_chord(notes.NOTE_F4)
    g_major_chord = get_major_chord(notes.NOTE_G4)
    
    a_minor_chord = get_minor_chord(notes.NOTE_A4)
    e_minor_chord = get_minor_chord(notes.NOTE_E4)
    
    #print('c_major_chord', NOTE_C4, c_major_chord)
    #print('f_major_chord', NOTE_F4, f_major_chord)
    #print('g_major_chord', NOTE_G4, g_major_chord)
    #print('a_minor_chord', NOTE_A4, a_minor_chord)
    
    #chord_progression_CFG = [c_major_chord, f_major_chord, g_major_chord]
    chord_progression_CGaF = [c_major_chord, g_major_chord, a_minor_chord, f_major_chord] #most popular
    
    #chord_progression_GeaD = [g_major_chord, e_minor_chord, a_minor_chord, d_major_chord]
    
    #chord_progression_aFCG = [a_minor_chord, f_major_chord, c_major_chord, g_major_chord] #sad: Am F C G

    #emotional 
    #Em – D – C – G – G/F#
    #chord_progression_eDCGG = [e_minor_chord, d_major_chord, c_major_chord, g_major_chord, g_major_chord]
    
    
    #happy
    chord_progression_GCD = [g_major_chord, c_major_chord, d_major_chord]
    
    selected_chord_progression = chord_progression_CGaF #chord_progression_GCD #chord_progression_CGaF #chord_progression_aFCG #chord_progression_GeaD #chord_progression_CGaF
    number_of_chords = len(selected_chord_progression)

    number_of_cycles = 4
    
    
    
    #midi_file.addProgramChange(0, 0, 0, 0)
    # tracknum – The zero-based track number to which program change event is added.
    # channel – the MIDI channel to assign to the event. [Integer, 0-15]
    # time – The time (in beats) at which the program change event is placed [Float].
    # program – the program number. [Integer, 0-127].
    
    
    #midi_file.addProgramChange(0, 0, 0*number_of_cycles*number_of_chords, 69) #69.  oboe
    #midi_file.addProgramChange(0, 0, 1*number_of_cycles*number_of_chords, 43) #43.	Cello
    #midi_file.addProgramChange(0, 0, 2*number_of_cycles*number_of_chords, 54) #43.	Cello
    
    
    #midi_file.addProgramChange(1, 1, 0*number_of_cycles*number_of_chords, 70) #70. english horn
    #midi_file.addProgramChange(1, 1, 1*number_of_cycles*number_of_chords, 41) #41 violin
    #midi_file.addProgramChange(1, 1, 2*number_of_cycles*number_of_chords, 61) #61 french horn
    
    
    percussion_intro_beats = beats_per_measure #one measure
    chord_intro_beats = beats_per_measure #one measure
    
    
    #percussion
    if True:
        duration_single_tap = 1
        durations_measure = [duration_single_tap]*beats_per_measure
        
        time = 0
        track = 0
        channel = 0
        percussion_volume = 100 #int(0.7*255)
        
        midi_file.addProgramChange(track, channel, time, midi_instrument_numbers.woodblock)
        
        #stand alone percussion lead in 
        for beat_index in range(percussion_intro_beats):
            #notes_to_choose = [selected_chord_progression[beat_index%len(selected_chord_progression)][0]]
            notes_to_choose = [selected_chord_progression[0][0]]
            time_going_in = time+0
            print('percussion time', time_going_in)
            time = pick_at_chord(midi_file, track, channel, time_going_in, volume, notes_to_choose, [duration_single_tap])
        
        notes_to_choose = [selected_chord_progression[0][0]]
        beat_index = 0
        for cycle_index in range(number_of_cycles):
            print('cycle_index', cycle_index)
            for chord in selected_chord_progression:
                time_going_in = time+0
                print('', 'percussion time', time_going_in)
                time = pick_at_chord(midi_file, track, channel, time_going_in, volume, notes_to_choose, durations_measure)
                
    
    
    #main chord strcuture
    if True:
        duration_single_tap = 1
        durations_measure = [duration_single_tap]*beats_per_measure
        
        time = percussion_intro_beats #start after drum lead in
        track = 1
        channel = 1
        midi_file.addProgramChange(track, channel, time, midi_instrument_numbers.acoustic_grand_piano)
        print('...', time, track, channel)
        #stand alone chord hammer - like a piano lead in 
        for beat_index in range(chord_intro_beats):
            time_going_in = time+0
            print('piano time', time_going_in)
            time = pick_at_chord(midi_file, track, channel, time_going_in, volume, notes_to_choose, [duration_single_tap])
        
        
        for cycle_index in range(number_of_cycles):
            print('cycle_index', cycle_index)
            for chord in selected_chord_progression:
                time_going_in = time+0
                print('', 'piano time', time_going_in)
                time = add_chord(midi_file, track, channel, time_going_in, volume, chord, durations_measure)
    
        
    
    """if False:
        #start after drum lead in and heavy chord lead in 
        #time = sum(number_of_cycles*durations_full_chord) #come in after first cycle
        time = percussion_intro_beats + chord_intro_beats
        
        track = 0
        
        channel = 0
        midi_file.addProgramChange(track, channel, time, instrument__acoustic_grand_piano) #Acoustic Grand Piano
        
        for cycle_index in range(number_of_cycles):
            #durations_pick_chord = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5] #get_durations_from_sum(possible_durations, sum(durations_full_chord), 0.25) #[0.5, 0.5, 0.5, 0.5, 1.0, 1.0] #[1,2,1]
            #durations_pick_chord = [0.5 if random.random() < 0.8 else ('rest',0.5) for idx in range(8)]
            #durations_pick_chord = [0.5  for idx in range(8)]
            
            dur_base = 0.5
            dur_rate = 0.9
            durations_pick_chord = [dur_base if random.random() < dur_rate else ('rest',dur_base)  for idx in range(8)]
            
            for chord in selected_chord_progression:
                #time = pick_at_chord(midi_file, track, channel, time, volume, chord, durations_pick_chord)
                time_going_in = time+0
                
                for idx in range(len(chord)):
                    time = pick_at_chord(midi_file, track, channel, time_going_in, volume, chord, durations_pick_chord)"""
                
                
    """if False:
        midi_file.addProgramChange(2, 2, 0*number_of_cycles*number_of_chords, 41) #violin
        time = 0
        track = 2
        channel = 2
        
        for cycle_index in range(number_of_cycles):
            dur_base = 0.25
            dur_rate = 0.9
            durations_pick_chord = [dur_base if random.random() < dur_rate else ('rest',dur_base)  for idx in range(8)]
            for chord in selected_chord_progression:
                time = pick_at_chord(midi_file, track, channel, time, volume, chord, durations_pick_chord)"""
                
                
    """if False:
        midi_file.addProgramChange(2, 2, 0*number_of_cycles*number_of_chords, 41) #violin
        time = 0
        track = 3
        channel = 3
        
        for cycle_index in range(number_of_cycles):
            dur_base = 0.25
            dur_rate = 0.7
            durations_pick_chord = [dur_base if random.random() < dur_rate else ('rest',dur_base)  for idx in range(8)]
            for chord in selected_chord_progression:
                time = pick_at_chord(midi_file, track, channel, time, volume, chord, durations_pick_chord)"""
        
    
        
    with open('my_song.mid', 'wb') as output_file:
        midi_file.writeFile(output_file)
        
        
        
if __name__ == '__main__':
    main()