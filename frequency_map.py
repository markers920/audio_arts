
# https://pages.mtu.edu/~suits/NoteFreqCalcs.html

"""
The basic formula for the frequencies of the notes of the equal tempered scale is given by

fn = f0 * (a)^n

where
f0 = the frequency of one fixed note which must be defined. 
    A common choice is setting the A above middle C (A4) at f0 = 440 Hz.
n = the number of half steps away from the fixed note you are. 
    If you are at a higher note, n is positive. 
    If you are on a lower note, n is negative.
    fn = the frequency of the note n half steps away.
a = (2)^(1/12) = the twelth root of 2 = the number which when multiplied by itself 12 times equals 2 = 1.059463094359...

------

The wavelength of the sound for the notes is found from

Wn = c/fn

where W is the wavelength and c is the speed of sound. 
The speed of sound depends on temperature, 
but is approximately 345 m/s at "room temperature."
"""



#(A4) at f0 = 440 Hz
f0 = 440 #Hz

#the twelth root of 2
a = 2.0**(1.0/12.0)

#speed of sound at room temperature
c = 345 #m/s

def get_frequency_from_steps(n):
    return f0 * (a**n)
    
def get_wavelength_from_steps(n):
    return c / get_frequency_from_steps(n)
    
    
    
    