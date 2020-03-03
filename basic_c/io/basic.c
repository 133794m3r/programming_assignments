/*
* C input handling the right way. 
* By Someone with Less sense than Sansity.
*/
/*
* A simple program showing the fix. It was to just add a space before 
*%c to get it compile right.
* This works even with c89 aka K&R C so even if your professor was to force your
*code to compile it for such an old version of C(most compilers default to c99) it'd still work.
* So that's all really.
*/
#include <stdio.h>
/*
*this is solely here so that I can do my dynamic array the right way.
* Basically stdlib is where malloc lives.
* Also the stdio.h is so that I can show you that this works even with file descriptors.
*/
#include <stdlib.h>
int main(int argc, char **argv){
/*
* and here is the right way to do a dynamically allocated string in C.
* This is what your fancy C++ compiler was doing behind the scenes 
* for you when you had a dynamic string.
* C doesn't hide what's under the hood it makes you deal with it. 
* C++ is more than happy to squirrel it away to protect you.
*/
	char *shape=(char *)malloc(sizeof(char));
	int height=1;
	int width=1;
	char draw=0;
/*
*now even with prompting.
*/
/*
* The code below in C++. I think I'm not a C++ expert but I think it's similar enough.
* std:cout << "Enter shape: ";
* std:cin >> shape;
* And repeatead for each option.
*
* the fprintf is just there to show you that stdout is just a file in linux. So is stdin, and so is stderr.
*/
	printf("Enter shape: ");
	scanf( "%s", shape);
	printf( "Enter height: ");
	scanf( "%d", &height);
	printf( "Enter Width: ");
	scanf( "%d", &width);
	printf("Enter Input Char: ");
	scanf( " %c",&draw);
	printf("shape:%s\nheight:%d\nwidth:%d\ncharacter to draw:%c\n",shape,height,width,draw);
	fprintf(stderr,"The program was called as '%s'. You can change the name and it will always print the right name!\n",argv[0]);
	return 0;
}
