#include <stdio.h>
typedef unsigned long long ull;

unsigned long long* productFib(ull prod){
  ull a=0;
  ull b=1;
  ull f=0;
  ull f_p=0;
  ull f_prod=0;
  static ull arr[3]={0,0,0};
  while(f_prod < prod){
    f=(a+b);
    f_p=a;
    a=b;
    b=f;
    f_prod=(b*a);
  }
  
  arr[0]=a;
  arr[1]=b;
  if(f_prod == prod)
    arr[2]=1;
  else
  	arr[2]=0;
  return arr;
}

int main(int argc, char **argv){
	ull *ans;
	ans=productFib(4895);
	printf("%llu * %llu == 4895? %llu\n",ans[0],ans[1],ans[2]);
	ans=productFib(5895);
	printf("%llu * %llu == 5895? %llu\n",ans[0],ans[1],ans[2]);	
	return 0;
}
