int solve(const char* string) {
	int max_score=0;
	int cur_score=0;
	int vowel=0;
	for(;*string;string++){
	switch(*string){
		case 'a':
		vowel=1;
		break;
		case 'e':
		vowel=1;
		break;
		case 'i':
		vowel=1;
		break;
		case 'o':
		vowel=1;
		break;
		case 'u':
		vowel=1;
		break;
		default:
		vowel=0;
		break;
	}
	if(vowel == 0){
		cur_score+=(*string-96);
	}
	else{
		max_score=(cur_score>max_score)?cur_score:max_score;
		cur_score=0;
	}
	}
	
	return (cur_score>max_score)?cur_score:max_score;
}
