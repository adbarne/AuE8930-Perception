import numpy as np
from numpy import sqrt, exp, pi
import matplotlib.pyplot as plt

# def gaussian(mu, sigma):
# 	# define probability density function (PDF)
# 	sigrange = 6						# how many standard deviations to range the PDF			
# 	PDFdom = np.arange(-sigrange*sigma, sigrange*sigma, (2*sigrange*sigma)/500) 
# 	pdf = 1/(sqrt(2*pi*sigma**2))*exp(-(PDFdom-mu)**2/(2*sigma**2))
	
# 	return PDFdom, pdf

# define variables for probability density function

mean = 0
var = 1
std = sqrt(var)

#define time domain
k = np.arange(0,499)

#define x(k) and n(k)
x = []
for i in range(len(k)):  
	x.append(20)

# n = gaussian(mean, std)
# print(n)
n = np.random.normal(mean, std, len(k))
xp = x + n
xp_fft = np.fft.fft(xp)
freq = np.fft.fftfreq(len(xp_fft))

# a) Visualize both x(k) and xp(k) in one figure
plt.figure()
plt.plot(k,xp,k,x)
plt.title('Visualize x(k) and xp(k)')
plt.xlabel('k')
plt.ylabel('Amplitude')

plt.show()