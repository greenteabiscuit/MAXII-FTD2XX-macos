#include "ftd2xx.h"
#include <stdio.h>
#include "stdlib.h"
#include <iostream>

FT_HANDLE   ftHandle[4];
FT_STATUS   ftStatus;
DWORD       numDevs;
DWORD		devIndex;
int			devcnt, devlast;
char        buf[256];
DWORD       WriteNum, TransNum;


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
            printf("%d\n", ftStatus);
            devcnt=0;	// device #0		address counter clear command 0x20;
            TransNum = 0; WriteNum=1; 
			buf[0]=0x02; //
            ftStatus = FT_Write(ftHandle[devcnt],buf,WriteNum,&TransNum);
            TransNum = 0; WriteNum=1; 
			buf[0]=0x04; // 
            ftStatus = FT_Write(ftHandle[devcnt],buf,WriteNum,&TransNum);
            
            ftStatus = FT_Close(ftHandle[devcnt]);  // USB Device CLOSE
            break;
        }
    }

    return 0;
}