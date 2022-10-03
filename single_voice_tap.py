
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
    tempo = int(80) #192/2     # In BPM
    
    number_of_tracks = 1
    midi_file = MIDIFile(number_of_tracks)
    midi_file.addTempo(track=0, time=0, tempo=tempo)
    
    track, channel = 0, 0
    volume = 70
    midi_file.addProgramChange(
        track, 
        channel, 
        0,  #time
        midi_instrument_numbers.pan_flute) #pan_flute) #tubular_bells) #acoustic_grand_piano)
    
    note = notes.NOTE_C4
    
    
    midi_file.addNote(track, channel, note, time=0, duration=whole, volume=volume)
    midi_file.addNote(track, channel, note, time=1, duration=whole, volume=volume)
    
        
if __name__ == '__main__':
    main()