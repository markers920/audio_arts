
import numpy as np
#from scipy.io.wavfile import write
from scipy.io import wavfile

import frequency_map


#data = np.random.uniform(-1,1,44100) # 44100 random samples between -1 and 1

samples_per_second = 44100
number_of_seconds = 2
frequency = 440

#data = [np.random.uniform(-1,1) for s in range(samples_per_second*number_of_seconds)]
#data = [np.sin(s/1000) for s in range(samples_per_second*number_of_seconds)]
#data = [np.sin((frequency/samples_per_second)*s) for s in range(samples_per_second*number_of_seconds)]

#scaled = np.int16(data/np.max(np.abs(data)) * 32767)
#write('test.wav', samples_per_second, scaled)


#  Produces an Audio-File
t = np.linspace(0, number_of_seconds, samples_per_second * number_of_seconds)  
y = np.sin(frequency * 2 * np.pi * t)  #  Has frequency of 440Hz

wavfile.write('Sine.wav', samples_per_second, y)