import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd
import math
import matplotlib.ticker as mticker
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

DATE = os.environ.get("DATE")
print(DATE)

x = np.linspace(0, 10*np.pi, 40960)
sin_signal = np.sin(1000*x) + np.random.rand(40960) * 0.8

for i in range(36):
    fs = 20000
    angle = str(i * 10)
    #amplitude =  1 + np.random.rand(1)[0]
    amplitude = 2
    print("angle:", angle, "\t", "amplitude:", amplitude)
    data = amplitude * sin_signal
    lstrip = data.tolist()
    Pxx, freqs, bins, im = plt.specgram(lstrip, Fs=fs, cmap = 'jet', mode='magnitude')

    pd.Series(Pxx.sum(axis=1)).to_csv(f"stftdata-{DATE}/{angle}.csv", index=False)


