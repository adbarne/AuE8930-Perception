import numpy as np
import matplotlib.pyplot as plt

def square(t0, tf): 
	# convert to microseconds to iterate loops in microseconds
	cf = 10**(-6)
	t_0 = t0
	t_f = tf
	# print(t_f)
	signal = []
	that = 0
	while t_0 <= t_f:
		# one cycle spans 1*10^-6 seconds
		k = 0
		while k < 1000*cf:
			if k <= 499*cf:
				signal.append(0) 
			elif k > 499*cf:
				signal.append(1)
			t_0 = t_0 + cf
			k = k + cf
	return signal

t0 = 0				# seconds
tf = 0.025			# seconds
Fs = 1*10**6		# 1 MHz sampling frequency			
step = 1/Fs 		# step size in seconds									
t = np.arange(t0,tf,step)
# t = np.linspace(t0,1,1*Fs)
y = square(t0,tf)

# compute fast Fourier Transform of x, plot in freqeuncy domain
y_fft = np.fft.fft(y)
freq = np.fft.fftfreq(len(y),d = step)

plt.figure()
plt.plot(y)
plt.title('Time Domain of Discrete Signal')
plt.xlabel('Time (\u03BCs)')
plt.ylabel('Amplitude')

plt.figure()
plt.plot(freq,y_fft)
plt.title('Frequency Domain of Discrete Signal ')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.show()
