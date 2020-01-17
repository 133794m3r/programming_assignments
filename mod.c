#include <stdio.h>
#include <stdlib.h>
int *gcd_fast(int a,int b){
    int gcd=0;
    int x=0;
    int y=0;
    int *triplet=malloc(sizeof(int)*3);
    if(b==0){
        triplet[0]=a;triplet[1]=0;triplet[2]=1;
        return triplet;
    }
    else{
        triplet= gcd_fast(b,a % b);
        x=triplet[1];
        y=triplet[2];
        triplet[1]=triplet[2];
        triplet[2]=x - a/b * y;
        return triplet;
    }
}
int main(){
    int a = -3;
    int m = 8;
    int *ptr=malloc(sizeof(int)*3);
    int mod_inv=0;
    printf("%d\n",a%m+m);
    ptr=gcd_fast(a,m);
    printf("gcd:%d x:%d y:%d\n",ptr[0],ptr[1],ptr[2]);
    if(ptr[0] == 1 || ptr[0] == -1){
        mod_inv = ptr[1] % m;
    }
    printf("mod_inv:%d\n",mod_inv );
    return 0;
}
