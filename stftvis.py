import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
DATE = os.environ.get("DATE")
FS_DIV = int(os.environ.get("FS_DIV"))
print(FS_DIV)

def wav_read(angle):
    try:
        with open(f'rawdata-{DATE}/{angle}.txt') as f:
            l_strip = [int(s.strip()) for s in f.readlines()]
    except:
        with open(f'rawdata-{DATE}/soundrecord.txt') as f:
            l_strip = [int(s.strip()) for s in f.readlines()]
            print("soundrecord")
    l_strip = l_strip[::3][:12900]
    return l_strip


if __name__ == "__main__":
    """
    time = np.arange(0,len(wave))/fs
    plt.plot(time, wave)
    plt.show()
    plt.close()
    """
    print(DATE)
    angle = input('Enter angle: ')
    lstrip = wav_read(angle)
    # fs = len(lstrip) // FS_DIV # 音声の場合
    fs = len(lstrip) // 8.5 # violinの場合
    print("fs:", fs)
    Pxx, freqs, bins, im = plt.specgram(lstrip, Fs=fs, cmap = 'jet', mode='magnitude')
    print(Pxx.shape)
    #print(Pxx)
    print("freqs", freqs.shape)
    print(freqs)
    #print(freqs)
    print("bins", bins.shape)
    #print(bins)

    print(Pxx.sum(axis=1).shape)
    print(Pxx.sum(axis=0).shape)

    # print(Pxx.sum(axis=1))
    # print(pd.Series(Pxx.sum(axis=1)))

    # pd.Series(Pxx.sum(axis=1)).to_csv(f"stftdata-{DATE}/{angle}.csv", index=False)

    #print(bins)
    x1, x2, y1, y2 = plt.axis()
    print(x1)
    print(x2)
    plt.axis((x1, x2, y1, y2))
    print(plt.xticks())
    #plt.xticks([ 0. ,  2.5,  5. ,  7.5, 10. , 12.5, 15. , 17.5, 20. ], ["0", "0.25", "0.5", "0.75", "1.0", "1.25", "1.5", "1.75", "2.0"])
    plt.xlabel("time [s]")
    plt.ylabel("frequency [Hz]")
    plt.colorbar(im).set_label('Intensity [dB]')
    plt.title(f"STFT Analysis of Waveform ({angle} Degrees)")
    # plt.title(f"STFT Analysis of Waveform (0 Degrees)")
    #plt.savefig(f"visualizations/stftvis_{angle}.png")
    plt.show()
    plt.close()
