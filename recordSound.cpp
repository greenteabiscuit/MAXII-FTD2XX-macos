#include "ftd2xx.h"
#include <stdio.h>
#include "stdlib.h"
#include <iostream>
#include <fstream>
#include <unistd.h>

FT_HANDLE   ftHandle[4];
FT_STATUS   ftStatus;
DWORD       numDevs;
DWORD		devIndex;
int			devcnt, devlast;
int         array_cnt;
char        buf[256]; // -127 to 127
DWORD       WriteNum, TransNum;
DWORD       ReadNum;
unsigned char bufc[128]; //保存できるのは0-255
double a[1986560];
double a_copy[1986560];
int i, j, k, stop;
unsigned char tmp_even, tmp_odd;

using namespace std;

int main(){
    numDevs = 0;
    ftStatus = FT_ListDevices(&numDevs,NULL,FT_LIST_NUMBER_ONLY);
    cout << ftStatus << endl;
    printf("%d\n", numDevs);
    devlast = numDevs;
    cout << "loop starting" << endl;
	for(devcnt = 0;devcnt != devlast; devcnt++){
        devIndex = (DWORD)devcnt;
        ftStatus = FT_ListDevices((PVOID)devIndex, buf, FT_LIST_BY_INDEX|FT_OPEN_BY_SERIAL_NUMBER);
        if (ftStatus==FT_OK) {
            ftStatus = FT_OpenEx(buf, FT_OPEN_BY_SERIAL_NUMBER, &ftHandle[devcnt]);
            if (ftStatus==FT_OK) {
                cout << "Open ok" << endl;
            }
            devcnt=0;	// device #0		
            TransNum = 0; WriteNum=1; 
			buf[0]=0x02; //address counter clear command 0x02
            ftStatus = FT_Write(ftHandle[devcnt],buf,WriteNum,&TransNum);
            if (ftStatus==FT_OK) {
                cout << "address clear successful" << endl;
            }
            TransNum = 0; WriteNum=1; 
			buf[0]=0x04; //read initialization
            ftStatus = FT_Write(ftHandle[devcnt],buf,WriteNum,&TransNum);
            stop = 0;
            if (ftStatus==FT_OK) {
                cout << "print initialization successful" << endl;

                while (1) {
                    devcnt = 0;
                    TransNum = 0; WriteNum = 1;
                    buf[0] = 0x03;
                    // write into memory
                    ftStatus = FT_Write(ftHandle[devcnt], buf, WriteNum, &TransNum);

                    // とりあえず 0 以外の数字が入ってきたら録音を終了するようにする
                    cin >> stop;
                    if (stop) cout << stop << endl;
                    if (stop!=0) {
                        cout << "stopping" << endl;
                        buf[0] = 0x04;
                        ftStatus = FT_Write(ftHandle[devcnt], buf, WriteNum, &TransNum);
                        break;
                    }
                }
            }

            cout << "closing" << endl;
            ftStatus = FT_Close(ftHandle[devcnt]);  // USB Device CLOSE
            break;
        }
    }

    return 0;
}