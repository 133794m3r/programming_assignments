#include <stdio.h>
#include <stdlib.h>

int main(void){
	//char characters[64]="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-~";
	char characters[64]={48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90,37,35};
	int numbers=0;
	//char character=malloc(255);
	int i=0;
	int j=0;
	int j_max=0;
	printf("Enter the number of lines to use to make each triangle: ");
	scanf("%d",&numbers);
	numbers=numbers&63;
	//top triangle.
	for(i=0;i<=numbers;i++){

		j_max=(numbers*2)-i;
		for(j=0;j<=j_max;j++){
			putchar(32);
		}
		j_max=(i*2)+1;
		for(j=0;j<j_max;j++){
			putchar(characters[i]);
		}
		putchar('\n');
	}
	//second & third triangle.
	for(i=0;i<=numbers;i++){
		j_max=(numbers - i);
		for(j=0;j<j_max;j++){
			putchar(' ');
		}
	
		j_max=(i*2)+1;
		for(j=0;j<j_max;j++){
			putchar(characters[i]);
		}
		putchar(' ');
		j_max=(numbers-i)*2;
		for(j=0;j<j_max;j++){
			putchar(' ');
		}
		j_max=(i*2)+1;
		for(j=0;j<j_max;j++){
			putchar(characters[i]);
		}
		putchar('\n');
	}
	return 0;
}
