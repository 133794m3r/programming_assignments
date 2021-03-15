#include <stdio.h>
//Macarthur Inbody 2020. Fun with pointers.
//this version is commented to make it easier. The program won't print out the exact same thing because of the comments.
//First I create a dynamic buffer on the stack.
char a[] = "\";\nint main(){char *b=a;printf(\"#include<stdio.h>\\nchar a[] = \\\"\");for(;*b;b++) {switch(*b){case '\\n': printf(\"\\\\n\"); break; \ncase '\\\\': case '\\\"':putchar('\\\\'); default: putchar(*b);}} printf(a); return 0;}\n";
//first we have the main function which we call.
int main() {
//copy the string a into a pointer of chars named b.
	char *b=a;
//send the string to the terminal.
	printf("#include <stdio.h>\nchar a[] = \"");
//for each char pointed to by b
	for(;*b;b++) {
//a switch statement based upon the current value at the address pointed to by the dereferenced b.
	switch(*b){
		//if it's a newline escape it.
		case '\n':
			printf("\\n"); 
			//break from the switch.
			break; 
		case '\\': case '"':
			//escape whatever we have whether it's a \ or a ".
			putchar('\\'); 
		default: 
			//by default we just send the character to the terminal.
			putchar(*b);
		}
	}
	//print whatever value is left of a.
	printf(a);
	//print the final string.
	printf("\nStrength through pointer arithmetic.\n"); 
	//return 0 because it ended successfully.
	return 0;
}
