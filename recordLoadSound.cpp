#include "ftd2xx.h"
#include <stdio.h>
#include "stdlib.h"
#include <iostream>
#include <fstream>
#include <unistd.h>
#include <signal.h> 
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
double average;
int i, j, k, stop;
unsigned char tmp_even, tmp_odd;

using namespace std;

void my_handler(int s){
    cout << "buffer" << buf[0] << endl;
    buf[0] = 0x04;
    ftStatus = FT_Write(ftHandle[devcnt], buf, WriteNum, &TransNum);
    cout << "closing device no. " << devcnt << endl;
    devcnt = 0;
    ftStatus = FT_Close(ftHandle[devcnt]);  // USB Device CLOSE
    exit(1); 

}


int main(){
    struct sigaction sigIntHandler;

    sigIntHandler.sa_handler = my_handler;
    sigemptyset(&sigIntHandler.sa_mask);
    sigIntHandler.sa_flags = 0;

    sigaction(SIGINT, &sigIntHandler, NULL);


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
                ofstream ofs("soundrecord.txt");
                while (1) {
                    devcnt = 0;
                    TransNum = 0; WriteNum = 1;
                    buf[0] = 0x03;
                    // write into memory
                    cout << "start recording for 3 seconds" << endl;
                    ftStatus = FT_Write(ftHandle[devcnt], buf, WriteNum, &TransNum);
                    sleep(3);
                    cout << "stopping and processing" << endl;
                    buf[0] = 0x04;
                    ftStatus = FT_Write(ftHandle[devcnt], buf, WriteNum, &TransNum);
                    sleep(3);
                    for (i=0;i<640;i++){
                        //cout << "set transfer len to 128" << endl;
                        TransNum = 0; WriteNum=1; 
			            buf[0]=0x08; // transfer len set to be 128
                        ftStatus = FT_Write(ftHandle[devcnt],buf,WriteNum,&TransNum);
                        for (j=0;j<128;j++) bufc[j]=buf[j];
                        //sleep(1);

                        //cout << "USB FIFO data load command" << endl;
                        buf[0]=0x05; // USB FIFO data load command
                        ftStatus = FT_Write(ftHandle[devcnt],buf,WriteNum,&TransNum);
                        for (j=0;j<128;j++) bufc[j]=buf[j];
                        //sleep(1);

                        //cout << "Reading USB data" << endl;
                        TransNum = 0; WriteNum=0; ReadNum=128; 
                        ftStatus = FT_Read(ftHandle[devcnt],bufc,ReadNum,&TransNum);		   
                        for (j=0;j<64;j++) {
                            a[j+i*64]=bufc[2*j]+bufc[2*j+1]*256;
                            average += a[j+i*64];
                            //cout << j + i * 64 << ": " << a[j+i*64] << endl;
                            ofs << a[j+i*64] << endl;
                        }
                    }
                    cout << "average: " << average / (j + i * 64 + 1) << endl;
                    cout << "write finished" << endl;
                    sleep(3);
                }
                ofs.close();
            }

            cout << "closing" << endl;
            ftStatus = FT_Close(ftHandle[devcnt]);  // USB Device CLOSE
            break;
        }
    }

    return 0;
}