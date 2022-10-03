
# https://stackoverflow.com/questions/38797934/get-the-amplitude-data-from-an-mp3-audio-files-using-python


# C:\Users\marke\Desktop\workspace\audio_arts>python mp3_to_signal.py ..\visual_arts\large_image_exploration\Fall_Back.mp3



from pydub import AudioSegment
import sys

import numpy as np
import matplotlib.pyplot as plt


sound = AudioSegment.from_mp3(sys.argv[1])

# get raw audio data as a bytestring
raw_data = sound.raw_data

# get the frame rate
sample_rate = sound.frame_rate

# get amount of bytes contained in one sample
sample_size = sound.sample_width #in BYTES

# get channels
number_channels = sound.channels


# If _ is a sample 
# and you have 3 channels 
# then song |_ _ _| |_ _ _| |_ _ _| has 6 samples, 3 frames. 
# Each _ is sample_size bytes long. 
# If sample_size = 2 bytes then my song is 12 bytes long, 
# and played at sample_rate = 6 Hz will have duration of 1 second.


raw_data_len = len(raw_data)

number_samples = int(raw_data_len / (sample_size*number_channels))
length_in_seconds = int(number_samples / sample_rate)
length_in_time_seconds = int(length_in_seconds)%60
length_in_time_minutes = int(length_in_seconds/60)
length_in_time_hours = int(length_in_seconds/3600)
length_in_time = ''
length_in_time = length_in_time if length_in_time_hours <= 0 else (str(length_in_time_hours) + ' hrs ')
length_in_time = length_in_time if length_in_time_minutes <= 0 else (str(length_in_time_minutes) + ' mins ')
length_in_time = length_in_time if length_in_time_seconds <= 0 else (str(length_in_time_seconds) + ' secs ')


print('-'*80)
print('raw_data_len:', raw_data_len)
print('number_samples:', number_samples)
print('length_in_seconds:', length_in_seconds)
print('length_in_time:', length_in_time)

print('sample_rate:', sample_rate)
print('sample_size:', sample_size)

print('number_channels:', number_channels)



#data = np.fromstring(raw_data, dtype=np.int16)
data = np.frombuffer(raw_data, dtype=np.int16)

# number_samples = len(data)/number_channels
data_by_channel = []
for channel_index in range(number_channels):
    slice_low = int(channel_index*number_samples)
    slice_high = int((channel_index+1)*number_samples)
    data_by_channel.append(data[slice_low:slice_high])
    #print('...', channel_index, channel_index*number_samples, (channel_index+1)*number_samples)
    #data_by_channel.append(data[:])

print('len(data)', len(data), len(data)/number_channels)


print('-'*80)
plt.figure(figsize=(9, 3))
time = [(length_in_seconds/60.0)*(idx/number_samples) for idx in range(number_samples)]

if False:
    for channel_index in range(number_channels):
        subplot_number = int(str(number_channels) + str(1) + str(channel_index+1))
        plt.subplot(subplot_number)
        plt.plot(time, data_by_channel[channel_index])
    plt.show()
