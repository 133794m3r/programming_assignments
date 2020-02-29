def check_palindrome(candidates):
	cur_len=0
	cur_len_2=0
	palindromes=[]
	candidates_len=len(candidates)
	tmp_str2=''
	for i in range(candidates_len):
		cur_len = len(candidates[i])
		cur_len_2 = cur_len //2
		if cur_len % 2:
			tmp_str2=candidates[i][cur_len_2+1:][::-1]
			
		else:
			tmp_str2=candidates[i][cur_len_2:][::-1]
		if candidates[i][0:cur_len_2] == tmp_str2:
			palindromes.append(candidates[i])
		else:
			#print(candidates[i][0:cur_len],candidates[i][cur_len-1::-1])
			pass
	return palindromes
	
def try_all_palindromes():
	candidates=[]
	for i in range(1000):
		for j in range(1000):
			candidates.append(str(i*j))
	palindromes=check_palindrome(candidates)
	palindromes=[int(x) for x in palindromes ]
	return max(palindromes)

print(try_all_palindromes())
