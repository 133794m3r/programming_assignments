#include <stdio.h>
#include <unistd.h> 
int main(int argc, char **argv){
	char *cmd = "ls";
	char *args[3];
	args[0] = "ls";
	args[1] = "-la";
	args[2] = NULL;
	execvp(cmd,args);
	return 0;
}
