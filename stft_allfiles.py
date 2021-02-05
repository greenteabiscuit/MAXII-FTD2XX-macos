import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from dotenv import load_dotenv
import os
from os.path import join, dirname


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

DATE = os.environ.get("DATE")
FS_DIV = int(os.environ.get("FS_DIV"))
print(DATE)
print(FS_DIV)


def wav_read(angle):
    with open(f'rawdata-{DATE}/{angle}.txt') as f:
        l_strip = [int(s.strip()) for s in f.readlines()]
        # データの長さは 12900にしないといけない。
        # specgramの出力されるアウトプットが129になるので。
        # l_strip = l_strip[::3][:12900]
    return l_strip


if __name__ == "__main__":
    """
    time = np.arange(0,len(wave))/fs
    plt.plot(time, wave)
    plt.show()
    plt.close()
    """
    path = f"stftdata/stftdata-{DATE}-fs-12900-div-2.5"
    print(path)
    for i in range(36):
        angle = str(i * 10)
        lstrip = wav_read(angle)
        # fs = len(lstrip) // FS_DIV # 音声の場合
        fs = len(lstrip) // 2.5 # violinの場合
        print("fs:", fs)
        Pxx, freqs, bins, im = plt.specgram(lstrip, Fs=fs, cmap = 'jet', mode='magnitude')
        #print(Pxx.shape)
        #print(Pxx)
        #print("freqs", freqs.shape)
        #print("bins", bins.shape)

        #print(Pxx.sum(axis=1).shape)
        #print(Pxx.sum(axis=0).shape)

        # print(Pxx.sum(axis=1))
        # print(pd.Series(Pxx.sum(axis=1)))

        if not os.path.isdir(path):
            os.makedirs(path)

        pd.Series(Pxx.sum(axis=1)).to_csv(f"{path}/{angle}.csv", index=False)
