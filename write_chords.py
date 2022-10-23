
from midiutil import MIDIFile
import sys

import midi_instrument_numbers

# https://studiocode.dev/resources/midi-middle-c/
base_note = 60 #middle C


if False:
    degrees = [base_note, base_note+4, base_note+7] #major
    directory = 'major_chords'

else:
    degrees = [base_note, base_note+3, base_note+7] 
    directory = 'minor_chords'


track = 0
channel = 0
duration = 1 # In beats
tempo = 60 # In BPM
volume = 100 # 0-127, as per the MIDI standard



midi_file_all = MIDIFile(1) # One track, defaults to format 1 (tempo track
time_all = 0



#instrument_index = int(sys.argv[1])
for instrument_index in range(0,128): #cycle through instruments
    midi_file = MIDIFile(1) # One track, defaults to format 1 (tempo track
    time = 0 # In beats
    
    midi_file.addProgramChange(track, channel, time, instrument_index)
    midi_file_all.addProgramChange(track, channel, time_all, instrument_index)

    # automatically created)
    midi_file.addTempo(track,time, tempo)
    for pitch in degrees:
        midi_file.addNote(track, channel, pitch, time, duration, volume)
        time = time + 1
        
        midi_file_all.addNote(track, channel, pitch, time_all, duration, volume)
        time_all = time_all + 1
        
    #full chord
    for pitch in degrees:
        midi_file.addNote(track, channel, pitch, time, duration, volume)
        
    instrument_name = midi_instrument_numbers.instrument_names[instrument_index]
    fn = directory + "/" + instrument_name + "-" + str(instrument_index) + ".mid"
    with open(fn, 'wb') as output_file:
        midi_file.writeFile(output_file)
        
with open(directory + "/major-scale-all.wav", "wb") as output_file_all:
    midi_file_all.writeFile(output_file_all)



"""
# https://stackoverflow.com/questions/50663428/midi2audio-fluidsynth-winerror-2-the-system-cannot-find-the-file-specified
# https://musical-artifacts.com/?apps=fluidsynth&formats=sf2&license=free&order=top_rated&tags=soundfont
# https://musical-artifacts.com/artifacts/433
soundfont = 'sound_fonts/Touhou.sf2'   
sample_rate = 44100
fs = fluidsynth(sound_font=soundfont, sample_rate=sample_rate)"""