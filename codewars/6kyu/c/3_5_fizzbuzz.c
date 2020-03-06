int solution(int number) {
  int sum=0;
  int i=2;
  number--;
	while(i++<number){
    if (i % 3 == 0 || (i>=5 && i % 5 == 0)){
      sum+=i;
    }
  }
  return sum;
}
