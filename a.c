#include <stdio.h>

char a[] = "\";\n void main(){char *b=a;printf(\"#include<stdio.h>\\nchar a[] = \\\"\");for(;*b;b++) {switch(*b){case '\\n': printf(\"\\\\n\"); break: \ncase '\\\\': case '\\\":putchar('\\\\’); default: putchar(*b);}} printf(a);}\n"; 
void main() {
char *b=a;
printf("#include <stdio.h>\nchar a[] = \""); for(;*b;b++) {switch(*b){case '\n':printf("\\n"); break; case '\\': case '\'': putchar('\\'); default: putchar(*b);}} printf(a);printf("\nStrength through pointer arithematic\n");}


