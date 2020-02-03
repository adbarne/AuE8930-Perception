import numpy as np
from numpy import sin, cos, pi
import matplotlib.pyplot as plt

# initialize time and sampling frequency (freq = cyc/sec) 
t0 = 0
tf = 0.1
Fs = 1*10**3		# 1 KHz sampling frequency
step = 1/Fs 		# Time spaceing (s)		
t = np.arange(t0,tf,step)
# N = tf*Fs
# t = np.linspace(t0,tf,N)

# compute signal with respect to time domain and plot
x = 2 + 3*cos(500*pi*t) + 2*cos(1000*pi*t) + 3*sin(2000*pi*t)

# compute fast Fourier Transform of x, plot in freqeuncy domain
# t_norm = np.linspace(t0,tf,tf*Fs)
# x_norm = 2 + 3*cos(500*pi*t_norm) + 2*cos(1000*pi*t_norm) + 3*sin(2000*pi*t_norm)

x_fft = abs(np.fft.fft(x))
freq = abs(np.fft.fftfreq(len(t), d = step))

# plot x in the time domain
fig1 = plt.figure()
plt.plot(t,x)
plt.title('Time Domain of Continuous Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# plot x in the frequency domain

plt.figure()
plt.plot(freq,x_fft)
plt.title('Frequency Domain of Continuous Signal ')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

plt.show()