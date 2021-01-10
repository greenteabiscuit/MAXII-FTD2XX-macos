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

def wav_read():
    l_strip = [500 for i in range(40960)]
    return l_strip


if __name__ == "__main__":
    fs = 20000
    lstrip = wav_read()
    for i in range(36):
        angle = str(i * 10)
        print(angle)
        Pxx, freqs, bins, im = plt.specgram(lstrip, Fs=fs, cmap = 'jet', mode='magnitude')

        pd.Series(Pxx.sum(axis=1)).to_csv(f"stftdata-{DATE}/{angle}.csv", index=False)
