#include <stdio.h> 
#include <unistd.h> 
#include <sys/types.h>
#include <fcntl.h>
int main(){
	//normal buffer.
	char *buff[4];
	//open my test file for reading only.
	//for some reason it wants an int.
	int fp=open("test.txt",O_RDONLY);
	//seek ahead and put the fp to it's value.
	lseek(fp,3,SEEK_SET);
	//read in the bytes into my buffer.
	read(fp,&buff,4);
	//close it.
	close(fp);
	//print the results.
	//should be 1592
	printf("%s\n",buff);
	//always return 0.
	return 0;
}
