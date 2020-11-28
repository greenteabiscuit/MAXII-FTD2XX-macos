#include "ftd2xx.h"
#include <stdio.h>
#include "stdlib.h"
#include <iostream>
#include <fstream>

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
int i, j, k;
unsigned char tmp_even, tmp_odd;

using namespace std;

int main(){
    numDevs = 0;
    ftStatus = FT_ListDevices(&numDevs,NULL,FT_LIST_NUMBER_ONLY);
    printf("%u\n", ftStatus);
    printf("%d\n", numDevs);
    devlast = numDevs;
    printf("loop starting\n");
	for(devcnt = 0;devcnt != devlast; devcnt++){
        devIndex = (DWORD)devcnt;
        ftStatus = FT_ListDevices((PVOID)devIndex, buf, FT_LIST_BY_INDEX|FT_OPEN_BY_SERIAL_NUMBER);
        if (ftStatus==FT_OK) {
            ftStatus = FT_OpenEx(buf, FT_OPEN_BY_SERIAL_NUMBER, &ftHandle[devcnt]);
            if (ftStatus==FT_OK) {
                printf("Open ok\n");
            }
            devcnt=0;	// device #0		
            TransNum = 0; WriteNum=1; 
			buf[0]=0x02; //address counter clear command 0x02
            ftStatus = FT_Write(ftHandle[devcnt],buf,WriteNum,&TransNum);
            if (ftStatus==FT_OK) {
                printf("address clear successful\n");
            }
            TransNum = 0; WriteNum=1; 
			buf[0]=0x04; //read initialization
            ftStatus = FT_Write(ftHandle[devcnt],buf,WriteNum,&TransNum);
            if (ftStatus==FT_OK) {
                printf("read initialization successful\n");

                for (k = 0; k < 16; k++) {
                    printf("loop %d\n", k);
                    for (i = 0; i < 64; i++) {
                        TransNum = 0; WriteNum = 1;
                        buf[0] = 0x08; // transfer len set to be 128
                        ftStatus = FT_Write(ftHandle[devcnt], buf, WriteNum, &TransNum);
                        for (j = 0; j < 128; j++) bufc[j] = buf[j];

                        buf[0] = 0x05; // USB FIFO data load command
                        ftStatus = FT_Write(ftHandle[devcnt], buf, WriteNum, &TransNum);
                        for (j = 0; j < 128; j++) bufc[j] = buf[j];

                        TransNum = 0; WriteNum = 0; ReadNum = 128;

                        ftStatus = FT_Read(ftHandle[devcnt], bufc, ReadNum, &TransNum);
                        for (j = 0; j < 64; j++) a[j + i * 64 + k * 4096] = bufc[2 * j] + bufc[2 * j + 1] * 256;
                    }
                }
                printf("finished loop\n");
                array_cnt = j + i * 64 + k * 4096;
                //printf("%d\n", array_cnt);
                ofstream ofs("test.txt");
                for (i = 0; i < 4000; i++)
                {
                    //printf("%f\n", a[i]);
                    ofs << a[i] << endl;
                }
                ofs.close();

                cout << "second loop start" << endl;
                for (i=0; i<64; i++){
                    if (i % 10 == 0) cout << i << endl;
                    TransNum = 0; WriteNum=1; 
                    buf[0]=0x08; // transfer len set to be 128
                    ftStatus = FT_Write(ftHandle[devcnt],buf,WriteNum,&TransNum);

                    for (j=0;j<128;j++) bufc[j]=buf[j];

                    buf[0]=0x05; // USB FIFO data load command
                    ftStatus = FT_Write(ftHandle[devcnt],buf,WriteNum,&TransNum);

                    //for (j=0;j<128;j++) bufc[j]=buf[j];
                    for (j=0;j<128;j++) {
                        bufc[j]=buf[j];
                        //cout << +bufc[j] << "\t" << buf[j] << endl;
                    }
                    TransNum = 0; WriteNum=0; ReadNum=128; 
                    ftStatus = FT_Read(ftHandle[devcnt],bufc,ReadNum,&TransNum);			   
                    //for (j=0;j<64;j++) a[j+i*64]=bufc[2*j]+bufc[2*j+1]*256;
                    for (j=0; j<64; j++) {
                        a[j + i * 64] = bufc[2 * j] + bufc[2 * j + 1] * 256;
                        cout << +bufc[2 * j] << "\t" << +bufc [2 * j + 1] << "\t" << a[j + i * 64] << endl;
                    } 
                }
                ofstream ofs2("test2.txt");
                for (i = 0; i < 2000; i++)
                {
                    tmp_even = bufc[2 * i];
                    tmp_odd = bufc[2 * i + 1];
                    a_copy[i] = tmp_even + tmp_odd * 256;
                    
                    //cout << +tmp_even << "\t" << +tmp_odd << "\t" << a_copy[i] << "\t" << a[i] << endl;
                    ofs2 << a[i] << endl;
                    
                }
                ofs2.close();
            }
            cout << "closing" << endl;
            ftStatus = FT_Close(ftHandle[devcnt]);  // USB Device CLOSE
            break;
        }
    }

    return 0;
}