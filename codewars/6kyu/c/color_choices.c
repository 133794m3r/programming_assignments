#include <stdio.h>
#include <stdlib.h>
long long checkChoose(long long m,int k) {
	int i=1;
	long long result=1;
  if(m == 1)
    return 0;
	for(i=1;i<k;++i){
		result=((result*(k+1-i))/i);
		if(result == m)
			return i;
	}
	return -1;
}
