
from notes import *
from chords import *
from midi_instrument_numbers import *

import random
import time

def seed(seed):
    random.seed(seed)


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
    
    
def get_full_score_from_sum(possible_tones, possible_durations, s, allow_rest, volume, seed=int(time.time())):
    durations = get_durations_from_sum(possible_durations, s, allow_rest=None)
    
    ret = []
    for duration in durations:
        tup = (random.choice(possible_tones),duration,volume)
        ret.append(tup)
    
    return ret