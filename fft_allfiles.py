# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def wav_read(angle):
    print(angle)
    with open(f'./rawdata-1210/{angle}.txt') as f:
        l_strip = [int(s.strip()) for s in f.readlines()]
    return l_strip


# データのパラメータ
#N = 256            # サンプル数
dt = 0.01          # サンプリング間隔
f1, f2 = 10, 20    # 周波数

for i in range(0, 36, 1):
    num = i * 10
    angle = str(num)
    f = wav_read(angle)
    N = len(f)
    t = np.arange(0, N*dt, dt) # 時間軸
    freq = np.linspace(0, 1.0, N) # 周波数軸

    # 高速フーリエ変換
    F = np.fft.fft(f)

    # 振幅スペクトルを計算
    Amp = np.abs(F)

    pd.DataFrame(Amp[1:], index=freq[1:]).to_csv(f"fftdata-1210/{angle}_fft.csv")
