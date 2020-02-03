clear
clc

t0 = 0;
tend = 5;

Fs = 1000;
step = 1/Fs;
t = t0:step:tend;

x = 2 + 3*cos(500*pi*t) + 2*cos(1000*pi*t) + 3*sin(2000*pi*t);
figure()
plot(t,x)

x_fft = fft(x);
figure()
plot(x_fft)