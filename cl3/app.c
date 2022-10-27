#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include<string.h>
#include "common.h"

int main()
{

	int fd = init();
	
	if(fd < 0) {
		
		printf("ERROR\n");
		finalization(fd);
		return 0;
		
	}
	
	char buf[10];
	while(1) {
		printf("order>> ");
		scanf("%s", buf);

		if(strcmp(buf, "ledon") == 0) {
			ledon(fd);
		}
		if(strcmp(buf, "lefoff") == 0){
			ledoff(fd);
		}
		if(strcmp(buf, "ledblink") == 0) {
			for(int i = 0 ; i <5 ; i++) {
				ledon(fd);
				usleep(1000 * 1000);
				ledoff(fd);
				usleep(1000 * 1000);
			}
		}
		if(strcmp(buf, "exit") == 0) {
			printf("quit!\n");
			finalization(fd);
			exit(1);
		}
	}
	finalization(fd);

	return 0;
}
