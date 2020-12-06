import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np


def wav_read():
    with open('./soundrecord.txt') as f:
        l_strip = [int(s.strip()) for s in f.readlines()]
    return l_strip


if __name__ == "__main__":
    lstrip = wav_read()
    """
    time = np.arange(0,len(wave))/fs
    plt.plot(time, wave)
    plt.show()
    plt.close()
    """
    fs = 44100
    angle = input('Enter angle: ')
    Pxx, freqs, bins, im = plt.specgram(lstrip, Fs=fs, cmap = 'jet', mode='magnitude')
    x1, x2, y1, y2 = plt.axis()
    plt.axis((x1, x2, y1, y2))
    plt.xlabel("time [s]")
    plt.ylabel("frequency [Hz]")
    plt.colorbar(im).set_label('Intensity [dB]')
    plt.title(f"STFT Analysis of Waveform ({angle} Degrees)")
    plt.show()
    plt.close()
