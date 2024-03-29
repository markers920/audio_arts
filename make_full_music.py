
from midiutil import MIDIFile


import midi_instrument_numbers


#from dishwasher_rythm import * 
#from i_have_to_kiss_you import * 
#from drum_lines import * 
#from troubled_with_yourself import * 
from short_samples import * 


def main():

    #tempo = int(30) #192/2     # In BPM
    number_of_tracks = len(music_frames_map.keys())
    midi_file = MIDIFile(number_of_tracks)
    midi_file.addTempo(track=0, time=0, tempo=tempo)
    
    #base_note = 60 #middle C
    #degrees = [base_note, base_note+4, base_note+7] #major
    #degrees = [base_note, base_note+3, base_note+7]  #minor
    
    for track_tuple in music_frames_map:
        tc_idx, instrument_index = track_tuple
        
        time = 0
        
        music_frames = music_frames_map[track_tuple]
        
        track, channel = tc_idx, tc_idx
        volume = 70
        #instrument_index = midi_instrument_numbers.acoustic_grand_piano #.celesta # string_ensemble_2 #.acoustic_guitar_nylon #.steel_drums #steel_drums #.pan_flute
        midi_file.addProgramChange(
            track, 
            channel, 
            0,  #time
            instrument_index) #pan_flute) #tubular_bells) #acoustic_grand_piano)
        instrument_name = midi_instrument_numbers.instrument_names[instrument_index]
        
        time_note_epsilon = 1.01 #(1/32.0)
        for music_frame in music_frames:
            number_of_cycles = music_frame['number_of_cycles']
            music = music_frame['music']
            for cycle_index in range(number_of_cycles):
                for notes, duration, volume in music:
                    if notes != REST:
                        if type(notes) == int:
                            notes = [notes]
                        for note in notes:
                            midi_file.addNote(track, channel, note, time, duration, volume)
                    #time += (duration + time_note_epsilon)
                    time += (duration * time_note_epsilon)
    #END for instrument
    
    #fn = directory + "/" + instrument_name + "-" + str(instrument_index) + ".mid"
    fn = SONG_NAME + '.mid'
    with open(fn, "wb") as output_file:
        midi_file.writeFile(output_file)
    
        
if __name__ == '__main__':
    main()