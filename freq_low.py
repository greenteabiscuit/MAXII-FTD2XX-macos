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


if __name__ == "__main__":
    print(DATE)
    right = 10
    maximum = 200
    lstrip= np.sin(1 / 8 * np.linspace(0, right * np.pi, maximum))
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
    #y2 = np.sin(2 * np.linspace(0, right * np.pi, 200))
    #plt.plot(x, y2)
    # plt.ylim(0, 900)
    for i in range(right + 1):
        print(maximum // right)
        plt.vlines([20 * i], -1, 1, "blue", linestyles='dashed')
    plt.xlabel("time [ms]")
    plt.ylabel("Amplitude")
    plt.title(f"Low Frequency Wave")
    plt.show()
    plt.close()
