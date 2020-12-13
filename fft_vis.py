# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use("ggplot")

def wav_read(angle):
    print(angle)
    #print(pd.read_csv(f"fftdata-1212/{angle}_fft.csv", index_col=0).head()["0"])
    df = pd.read_csv(f"fftdata-1212/{angle}_fft.csv", index_col=0)
    df["0"].plot()


# データのパラメータ
#N = 256            # サンプル数
dt = 0.01          # サンプリング間隔
f1, f2 = 10, 20    # 周波数

for i in range(0, 19, 1):
    num = i * 10
    angle = str(num)
    f = wav_read(angle)

plt.show()
