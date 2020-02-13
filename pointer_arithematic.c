#include <stdio.h>
char a[] = "\";\nint main(){char *b=a;printf(\"#include<stdio.h>\\nchar a[] = \\\"\");for(;*b;b++) {switch(*b){case '\\n': printf(\"\\\\n\"); break; \ncase '\\\\': case '\\\"':putchar('\\\\'); default: putchar(*b);}} printf(a); return 0;}\n";
int main() {char *b=a;printf("#include <stdio.h>\nchar a[] = \"");for(;*b;b++) {switch(*b){case '\n':printf("\\n"); break; case '\\': case '"':putchar('\\'); default: putchar(*b);}}printf(a);printf("\nStrength through pointer arithmetic\n"); return 0;}
