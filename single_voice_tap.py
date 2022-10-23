
from midiutil import MIDIFile

import notes
import midi_instrument_numbers
import chords
import fractal_functions


whole = 1.0
half = 1.0 / 2.0
quarter = 1.0 / 4.0
eigth = 1.0 / 8.0
sixteenth = 1.0 / 16.0


def main():
    tempo = int(60) #192/2     # In BPM
    
    number_of_tracks = 4
    midi_file = MIDIFile(number_of_tracks)
    midi_file.addTempo(track=0, time=0, tempo=tempo)
    
    total_time = 4
    
    
    
    base_note = 60 #middle C
    degrees = [base_note, base_note+4, base_note+7] #major
    #degrees = [base_note, base_note+3, base_note+7]  #minor
    
    
    
    
    
    track, channel = 0, 0
    volume = 70
    instrument_index = midi_instrument_numbers.pan_flute #steel_drums #.pan_flute
    midi_file.addProgramChange(
        track, 
        channel, 
        0,  #time
        instrument_index) #pan_flute) #tubular_bells) #acoustic_grand_piano)
    instrument_name = midi_instrument_numbers.instrument_names[instrument_index]
    
    ratio = 2.0
    for ttt in range(int(total_time/ratio)):
        #midi_file.addNote(track, channel, notes.NOTE_C4, time=ratio*ttt, duration=whole, volume=volume)
        #full chord
        for pitch in degrees:
            midi_file.addNote(track, channel, pitch, ttt, duration=whole, volume=volume)
        
        
        
        
    track, channel = 1, 1
    volume = 70
    instrument_index = midi_instrument_numbers.pan_flute
    midi_file.addProgramChange(
        track, 
        channel, 
        0,  #time
        instrument_index) #pan_flute) #tubular_bells) #acoustic_grand_piano)
    instrument_name = midi_instrument_numbers.instrument_names[instrument_index]
    
    ratio = 1.0
    for ttt in range(int(total_time/ratio)):
        midi_file.addNote(track, channel, notes.NOTE_E4, time=ratio*ttt, duration=whole, volume=volume)
    
        
        
        
    track, channel = 2, 2
    volume = 70
    instrument_index = midi_instrument_numbers.pan_flute
    midi_file.addProgramChange(
        track, 
        channel, 
        0,  #time
        instrument_index) #pan_flute) #tubular_bells) #acoustic_grand_piano)
    instrument_name = midi_instrument_numbers.instrument_names[instrument_index]
    
    ratio = 0.5
    for ttt in range(int(total_time/ratio)):
        midi_file.addNote(track, channel, notes.NOTE_D4, time=ratio*ttt, duration=whole, volume=volume)
    
    
    
    
    
    
    
    
    
    track, channel = 3, 3
    volume = 100
    instrument_index = midi_instrument_numbers.tubular_bells
    midi_file.addProgramChange(
        track, 
        channel, 
        0,  #time
        instrument_index) #pan_flute) #tubular_bells) #acoustic_grand_piano)
    instrument_name = midi_instrument_numbers.instrument_names[instrument_index]
    
    ratio = 1.0
    for ttt in range(int(total_time/ratio)):
        #full chord
        for pitch in degrees:
            midi_file.addNote(track, channel, pitch, ttt, duration=whole, volume=volume)
            
            
            
            

    for pitch in degrees:
        midi_file.addNote(track, channel, pitch, time=total_time, duration=whole, volume=120)


    
    
    
    
    #fn = directory + "/" + instrument_name + "-" + str(instrument_index) + ".mid"
    fn = 'voices.mid'
    with open(fn, "wb") as output_file:
        midi_file.writeFile(output_file)
    
        
if __name__ == '__main__':
    main()