import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np


path_to_wavefile = "こんにちは (online-audio-converter.com).wav"


def wav_read(path):
    wave, fs = sf.read(path, dtype="int16") #音データと周波数を読み込む
    with open('./soundrecord.txt') as f:
        l_strip = [int(s.strip()) for s in f.readlines()]
    return l_strip, wave, fs


if __name__ == "__main__":
    lstrip, wave, fs = wav_read(path_to_wavefile)
    """
    time = np.arange(0,len(wave))/fs
    plt.plot(time, wave)
    plt.show()
    plt.close()
    """

    wave = wave[:, 0]
    Pxx, freqs, bins, im = plt.specgram(lstrip, Fs=fs, cmap = 'jet', mode='magnitude')
    x1, x2, y1, y2 = plt.axis()
    plt.axis((x1, x2, y1, y2))
    plt.xlabel("time")
    plt.ylabel("frequency")
    plt.colorbar(im).set_label('Intensity [dB]')
    plt.show()
    plt.close()
