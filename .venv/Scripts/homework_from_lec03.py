#TASK: Use Numpy and Matplotlib to define a "Rect" signal in the time dimension and plot it.
#then apply a fourier transform to the signal and plot the result.
#in the next step, remove order coefficients from the fourier transform and apply an inverse fourier transform to the signal.

#A furier transform is a mathematical transform that decomposes a function (often a function of time, or a signal) into its constituent frequencies.
#It calculates the mass center of the signal in the frequency domain.


import numpy as np
import matplotlib.pyplot as plt

# Define the Rect signal
def rect(length, width):
    singal = np.zeros(length)               # Create an array of zeros
    start = (length - width) // 2           # Start of the signal "//" is used for integer division
    end = start + width                     # End of the signal
    singal[start:end] = 1                   # Set the signal to 1
    return singal

# Parameters
length = 128
width = 32

# Generate the signal
signal = rect(length, width)

# Compute the fourier transform
fourier_transform = np.fft.fft(signal)          # Fourier Transform
frequencies = np.fft.fftfreq(length)            # creating Array of Frequencies

# Plot the Rect signal
plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
plt.stem(signal, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.title('Rect Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

# Plot the magnitude of the fourier transform
plt.subplot(1, 2, 2)
plt.stem(frequencies, np.abs(fourier_transform), linefmt='g-', markerfmt='go', basefmt='r-')
plt.title('Magnitude of Fourier Transform')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')

plt.tight_layout()
plt.show()

# Zero out higher order coefficients
cutoff = 10
fourier_transform[np.abs(frequencies) > cutoff] = 0

# INverse Fourier transform to obtain the filtered signal
filtered_signal = np.fft.ifft(fourier_transform)

# Plot the filtered signal
plt.figure(figsize=(7, 4))
plt.stem(filtered_signal, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.title('Filtered signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()