/*
* Area of a rectangle calculator.
* Done entirely in C.
* By Macarthur Inbody
*/
//Have to include the IO functions.
#include <stdio.h>
//main either should be void or an int.
int main(){
	//initialize base as an unsigned long integer and set the value to 0.
	unsigned long base=0;
	//same for height.
	unsigned long height=0;
	//same again.
	unsigned long area=0;
	//Print out to the console the the sentence.
	printf("Rectangle area calculator.\n");
	//Print out the "prompt".
	printf("Enter the base: ");
	//We're going to look for user input then we'll pass
	//the result to the value pointed to at the address that we give it.
	//Also it casts it to an unsigned long value.
	scanf("%lu",&base);
	//We do the same thing again for height.
	printf("Enter the height: ");
	scanf("%lu",&height);
	//get the area value.
	area=base*height;
	//Here we'll print out the area. the %lu is the formatter like in python
	//you can format the output of any value given to it. But in C you have
	//pass it after a comma. We also print out a new line.
	printf("The area is %lu square units.\n",area);
	//return zero because it exited OK.
	return 0;
}
