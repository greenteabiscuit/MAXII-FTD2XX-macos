import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np
from dotenv import load_dotenv
import os
from os.path import join, dirname


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

DATE = os.environ.get("DATE")
print(DATE)


def wav_read(angle):
    try:
        with open(f'rawdata-{DATE}/soundrecord.txt') as f:
            print("soundrecord")
            l_strip = [int(s.strip()) for s in f.readlines()]
    except:
        with open(f'rawdata-{DATE}/{angle}.txt') as f:
            l_strip = [int(s.strip()) for s in f.readlines()]
    return l_strip[:30000]


if __name__ == "__main__":
    print(DATE)
    angle = input('Enter angle: ')
    lstrip= wav_read(angle)
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
    plt.ylim(0, 900)
    plt.xlabel("time [ms]")
    plt.ylabel("Amplitude")
    plt.title(f"Waveform From FPGA ({angle} Degrees)")
    plt.show()
    plt.close()
