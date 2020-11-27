# MAXII-ftdi-macos


Install the driver for MacOS here: https://www.ftdichip.com/Drivers/D2XX.htm

You might have to run brew upgrade on your local Mac machine.

sudo cp Desktop/D2XX/libftd2xx.1.4.16.dylib /usr/local/lib/
sudo ln -sf /usr/local/lib/libftd2xx.1.4.16.dylib /usr/local/lib/
sudo cp Desktop/D2XX/ftd2xx.h /usr/local/include/ftd2xx.h
sudo cp Desktop/D2XX/WinTypes.h /usr/local/include/WinTypes.h


When compiling:

gcc libftd2xx.1.4.16.dylib test1.cpp -o test1

./test1

マークダウンを直すのは明日以降
