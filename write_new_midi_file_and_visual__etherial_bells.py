
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
import chords
import fractal_functions


import cv2
from PIL import Image
from datetime import datetime
import numpy as np
import math
import sys
import time




random.seed(1989) #datetime.now()) #1987

TWO_PI = 2.0*math.pi
PI = math.pi
HALF_PI = math.pi/2.0




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
    index_to_rest = set()
    while (len(ret) <= 0) or (sum(ret) < s):
        #print(ret, sum(ret), s)
        d = random.choice(possible_durations)
        if (sum(ret) + d) <= s:
            if allow_rest != None and random.random() < allow_rest:
                #d = ('rest',d)
                index_to_rest.add(len(ret))
            ret.append(d)
    
    for idx in index_to_rest:
        d = ret[idx]
        ret[idx] = ('rest',d)
    return ret




def build_music():

    tempo = int(80*0.9391) #192/2     # In BPM
    beats_per_measure = 6
    selected_chord_progression = chords.chord_progression_CFGF #chord_progression_CGaF
    number_of_cycles_1 = 3
    number_of_cycles_2 = 2
    
    possible_durations = sorted([1,20.5,0.25]) #sorted([1,2,4,0.5,0.25,0.125])
    
    number_of_tracks = 5
    midi_file = MIDIFile(number_of_tracks)
    midi_file.addTempo(track=0, time=0, tempo=tempo)
    
    for track_index in range(number_of_tracks):
        time = track_index
        midi_file.addTempo(track_index, time, tempo) #(track,time,tempo) ... track=0, time = 0
    
    
    
    number_of_chords = len(selected_chord_progression)

    
    number_of_beats = number_of_cycles_1*number_of_cycles_2*number_of_chords*beats_per_measure
    total_time_in_seconds = 60.0 * (number_of_beats / tempo)
    
    print('number_of_beats:', number_of_beats)
    print('total_time_in_seconds:', total_time_in_seconds)
    
    
    
    #set instruments ----------------------------------------------------
    percussion_track, percussion_channel, percussion_volume = 0, 0, 20
    midi_file.addProgramChange(percussion_track, percussion_channel, 0, midi_instrument_numbers.reverse_cymbal) #woodblock)
    
    base_track, base_channel, base_volume = 1, 1, 70
    midi_file.addProgramChange(base_track, base_channel, 0, 
        midi_instrument_numbers.pan_flute) #tubular_bells) #acoustic_grand_piano)
    
    top_1_track, top_1_channel, top_1_volume = 2, 2, 70
    midi_file.addProgramChange(top_1_track, top_1_channel, 0, 
        midi_instrument_numbers.fx_7_echoes) #acoustic_grand_piano) #string_ensemble_2)
    
    top_2_track, top_2_channel, top_2_volume = 3, 3, 80
    midi_file.addProgramChange(top_2_track, top_2_channel, 0, 
        midi_instrument_numbers.fx_4_atmosphere) #string_ensemble_1)
    
    top_3_track, top_3_channel, top_3_volume = 3, 3, 80
    midi_file.addProgramChange(top_3_track, top_3_channel, 0, 
        midi_instrument_numbers.fx_3_crystal) #tubular_bells)
    
    #acoustic_grand_piano
    #string_ensemble_2
    
    time = 0
    for cycle_index_1 in range(number_of_cycles_1):
        #dim the volumes
        percussion_volume = int(percussion_volume*(0.9**cycle_index_1))
        base_volume = int(base_volume*(0.9**cycle_index_1))
        top_1_volume = int(top_1_volume*(0.9**cycle_index_1))
        top_2_volume = int(top_2_volume*(0.9**cycle_index_1))
        
    
        #set durations for this outer cycle loop
        percussion_durations = [1 for idx in range(beats_per_measure)]
        percussion_chord = [notes.NOTE_C4]
    
        #base_durations = [1, 1, 0.5, 0.5, ('rest',0.5), 0.25, 0.25, 1, 1]   #6
        #base_durations = [1, 1, 0.5, 0.5, ('rest',0.5), 0.25, 0.25]   #4
        base_durations = [1,0.5, 0.5,1,1]
        
        #top_track_durations_sample = get_durations_from_sum(possible_durations, beats_per_measure, allow_rest=0.5)
        #top_1_durations = top_track_durations_sample[4:] + top_track_durations_sample[:4]
        #top_2_durations = top_track_durations_sample[3:] + top_track_durations_sample[:3]
        top_1_durations = [1, 1, 0.5, 0.5, ('rest',1)] #4
        top_2_durations = [('rest', 1), 1, 1, 0.5, 0.5] #[('rest',1.5), 1, 1, 0.25, 0.25] #4
        top_3_durations = [('rest', 1), 1, 1, 0.5, 0.5]
        
        for cycle_index_2 in range(number_of_cycles_2):
        
            for chord_index, chord in enumerate(selected_chord_progression):
                measure_index = cycle_index_2*chord_index
                time_going_in = time+0
                
                #percussion
                time = add_chord(midi_file, percussion_track, percussion_channel, time_going_in, percussion_volume, percussion_chord, percussion_durations)
                    
                #base
                time = add_chord(midi_file, base_track, base_channel, time_going_in, base_volume, chord, base_durations)
                
                #top 1
                time = pick_at_chord(midi_file, top_1_track, top_1_channel, time_going_in, top_1_volume, chord, top_1_durations)
                
                #top 2
                time = pick_at_chord(midi_file, top_2_track, top_2_channel, time_going_in, top_2_volume, chord, top_2_durations)
                
                #top 3
                time = pick_at_chord(midi_file, top_3_track, top_3_channel, time_going_in, top_3_volume, chord, top_3_durations)
            #END for chord
        #END for cycle_index_2
    #END for cycle_index_1
    
    
        
    with open('my_song.mid', 'wb') as output_file:
        midi_file.writeFile(output_file)
        
    return total_time_in_seconds, number_of_cycles_1, number_of_cycles_2, selected_chord_progression
#END build_music



def build_visual(total_time_in_seconds, number_of_cycles_1, number_of_cycles_2, selected_chord_progression):
    number_of_transition_windows = number_of_cycles_1 * number_of_cycles_2 * len(selected_chord_progression)

    #image_width, image_height = 1080, 1350 #instagram smaller hd
    image_width, image_height = 1080, 1920    #instagram larger hd
    #image_width, image_height = 3840, 2160 #4k for youtube

    frames_per_second = 30 #...(2*3*5)
    number_of_frames = int(total_time_in_seconds*frames_per_second)
    
    output_file_name = 'music_video.mp4'
    videodims = (image_width, image_height)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    
    video = cv2.VideoWriter(
        output_file_name, 
        fourcc, 
        frames_per_second, 
        videodims)
        
        
        
    #for each frame -----------------------------------------------------------
    frame_times = []
    frame_time_sum = 0.0
    frame_time_avg, projected_time_remaining = None, None
    
    fractal_max_iterations = 5
    fractal_boundary = 1000
    
    for frame_index in range(number_of_frames):
        if True: #frame_index % 100 == 0:
            print('frame', frame_index, 'of', number_of_frames)
            if frame_index > 0:
                frame_time_avg = frame_time_sum/len(frame_times)
                frames_remaining = number_of_frames-frame_index
                projected_time_remaining = frames_remaining*frame_time_avg
                projected_time_remaining = str(int(projected_time_remaining/60)) + ' min, ' + str(int(projected_time_remaining)%60) + ' sec'
                print('', 'avg frame time', frame_time_avg)
                print('', 'remaining time', projected_time_remaining)
        frame_tic = time.process_time()
        
        frame_ratio = frame_index / number_of_frames
        theta = TWO_PI*frame_ratio
        frame_sin = np.sin(theta)
        
        
        
        #image = Image.new('RGBA', (image_width,image_height), (0,0,0,255))
        #image = np.zeros((image_height,image_width,4), np.uint8)
        image = fractal_functions.paint_julia(image_height, image_width, frame_ratio, fractal_max_iterations, fractal_boundary, number_of_transition_windows)
        
        ###############video.write(cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
        video.write(cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
        
        frame_toc = time.process_time()
        frame_time = frame_toc-frame_tic
        frame_times.append(frame_time)
        
        frame_time_sum += frame_time
    #END for each frame
    
    video.release()
    
    print('output_file_name', output_file_name)
#END build_visual





def main():
    total_time_in_seconds, number_of_cycles_1, number_of_cycles_2, selected_chord_progression = build_music()
    #build_visual(total_time_in_seconds, number_of_cycles_1, number_of_cycles_2, selected_chord_progression)
        
if __name__ == '__main__':
    main()