import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def wav_read(angle):
    with open(f'rawdata-1212/{angle}.txt') as f:
        l_strip = [int(s.strip()) for s in f.readlines()]
    return l_strip


if __name__ == "__main__":
    """
    time = np.arange(0,len(wave))/fs
    plt.plot(time, wave)
    plt.show()
    plt.close()
    """
    fs = 44100
    angle = input('Enter angle: ')
    lstrip = wav_read(angle)
    Pxx, freqs, bins, im = plt.specgram(lstrip, Fs=fs, cmap = 'jet', mode='magnitude')
    print(Pxx.shape)
    #print(Pxx)
    print("freqs", freqs.shape)
    print(freqs)
    print("bins", bins.shape)
    print(bins)

    print(Pxx.sum(axis=1).shape)
    print(Pxx.sum(axis=0).shape)

    # print(Pxx.sum(axis=1))
    # print(pd.Series(Pxx.sum(axis=1)))

    pd.Series(Pxx.sum(axis=1)).to_csv(f"stftdata-1212/{angle}.csv", index=False)

    #print(bins)
    x1, x2, y1, y2 = plt.axis()
    plt.axis((x1, x2, y1, y2))
    plt.xlabel("time [s]")
    plt.ylabel("frequency [Hz]")
    plt.colorbar(im).set_label('Intensity [dB]')
    plt.title(f"STFT Analysis of Waveform ({angle} Degrees)")
    #plt.savefig(f"visualizations/stftvis_{angle}.png")
    plt.show()
    plt.close()
