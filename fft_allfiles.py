# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

date = "0101"

def wav_read(angle):
    print(angle)
    with open(f'./rawdata-{date}/{angle}.txt') as f:
        l_strip = [int(s.strip()) for s in f.readlines()]
    return l_strip


# データのパラメータ
#N = 256            # サンプル数
dt = 0.01          # サンプリング間隔

for i in range(0, 36, 1):
    num = i * 10
    angle = str(num)
    f = wav_read(angle)
    N = len(f)
    t = np.arange(0, 3, dt) # 時間軸
    # 高速フーリエ変換
    F = np.fft.fft(f)

    # 振幅スペクトルを計算
    Amp = np.abs(F)
    #print(Amp.shape)
    #print(Amp)
    freq = np.linspace(0, 100.0, N) # 周波数軸
    # plt.plot(freq, Amp)


    pd.DataFrame(Amp[1:], index=freq[1:]).to_csv(f"fftdata-{date}/{angle}_fft.csv")
#plt.show()