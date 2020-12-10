#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


def _update(frame, x, y):
    """グラフを更新するための関数"""
    # 現在のグラフを消去する
    plt.cla()
    # データを更新 (追加) する
    with open('./soundrecord.txt') as f:
        l_strip = [s.strip() for s in f.readlines()]
    # print(l_strip)
    print(frame)
    data_y = int(l_strip[frame])
    print(data_y)
    x.append(frame)
    y.append(data_y)
    plt.ylabel("amplitude")
    plt.xlabel("time")
    plt.title("real time sound data")
    # 折れ線グラフを再描画する
    plt.plot(x, y)


def main():
    # 描画領域
    fig = plt.figure(figsize=(10, 6))
    # 描画するデータ (最初は空っぽ)
    x = []
    y = []

    params = {
        'fig': fig,
        'func': _update,  # グラフを更新する関数
        'fargs': (x, y),  # 関数の引数 (フレーム番号を除く)
        'interval': 1000,  # 更新間隔 (ミリ秒)
        'frames': np.arange(0, 50, 1),  # フレーム番号を生成するイテレータ
        'repeat': False,  # 繰り返さない
    }
    anime = animation.FuncAnimation(**params)

    # グラフを表示する
    plt.show()


if __name__ == '__main__':
    main()