import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def wav_read(angle):
    with open(f'rawdata-0101/{angle}.txt') as f:
        l_strip = [int(s.strip()) for s in f.readlines()]
    return l_strip


if __name__ == "__main__":
    """
    time = np.arange(0,len(wave))/fs
    plt.plot(time, wave)
    plt.show()
    plt.close()
    """
    fs = 20000
    for i in range(36):
        angle = str(i * 10)
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

        pd.Series(Pxx.sum(axis=1)).to_csv(f"stftdata-0101/{angle}.csv", index=False)
