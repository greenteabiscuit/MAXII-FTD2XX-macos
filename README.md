# MAXII-FTD2XX-macos

## Environment & Prerequisites

MacOS Catalina

You might have to disable csrutil to copy the files in to `usr/local/lib`

Look here: https://qiita.com/iwaseasahi/items/9d2e29b02df5cce7285d

## Installing the library

Install the driver for MacOS here: https://www.ftdichip.com/Drivers/D2XX.htm

You might have to run `brew upgrade` on your local Mac machine.

```
sudo cp Desktop/D2XX/libftd2xx.1.4.16.dylib /usr/local/lib/
sudo ln -sf /usr/local/lib/libftd2xx.1.4.16.dylib /usr/local/lib/
sudo cp Desktop/D2XX/ftd2xx.h /usr/local/include/ftd2xx.h
sudo cp Desktop/D2XX/WinTypes.h /usr/local/include/WinTypes.h
```

## To compile && run

When compiling:

```
$ gcc libftd2xx.1.4.16.dylib recordLoadSound.cpp -o recordLoadSound
or
$ g++ libftd2xx.1.4.16.dylib recordLoadSound.cpp -o recordLoadSound
```

To run:

```
./test1
```
