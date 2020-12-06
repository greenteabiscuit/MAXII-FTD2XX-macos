import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np


def wav_read():
    with open('./soundrecord.txt') as f:
        l_strip = [int(s.strip()) for s in f.readlines()]
    return l_strip


if __name__ == "__main__":
    lstrip= wav_read()
    """
    time = np.arange(0,len(wave))/fs
    plt.plot(time, wave)
    plt.show()
    plt.close()
    """
    x = np.arange(0, len(lstrip), 1)
    print(len(lstrip))
    y = lstrip
    plt.plot(x, y)
    plt.ylim(0, max(lstrip)+100)
    plt.xlabel("time")
    plt.ylabel("frequency")
    plt.show()
    plt.close()
