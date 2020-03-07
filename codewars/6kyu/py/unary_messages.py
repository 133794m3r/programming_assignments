def send(s):
	binary=''.join([ bin(ord(x))[2:].zfill(7) for x in s ])
	count=1
	prev=binary[0]
	cur='0'
	output=''
	tmp_bits='0'
	for bit in binary[1:]:
		if bit != prev:
			output+=('00' if prev == '0' else '0')
			output+=' '
			output+=tmp_bits
			output+=' '
			tmp_bits='0'
		else:
			tmp_bits+='0'
		
		prev=bit
	if prev == bit:
		output+=('00' if prev == '0' else '0')
		output+=' '
		output+=tmp_bits
		
	return output
	

def receive(s):
	import re
	re.compile('.{7}')
	arr=s.split(' ')
	arr_len=len(arr)
	output=''
	bit=''
	bits=''
	for i in range(0,arr_len,2):
		bit=('1' if arr[i] == '0' else '0')
		bits+=(bit*len(arr[i+1]))
	bit_split=re.findall('.{7}',bits)
	output=''.join(chr(int(x,2)) for x in bit_split)
	return output
