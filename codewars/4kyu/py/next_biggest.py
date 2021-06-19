def next_bigger(number):
	num_ls = list(map(int, list(str(number))))
	n = len(num_ls)
	i = 0
	for i in range(n-1,0,-1):
		if num_ls[i] > num_ls[i - 1]:
			break
	if i == 1 and num_ls[i] <= num_ls[i - 1]:
		return -1
	x = num_ls[i - 1]
	smallest = i
	for j in range(i+1,n):
		if x < num_ls[j] < num_ls[smallest]:
			smallest = j
	num_ls[smallest], num_ls[i - 1] = num_ls[i - 1], num_ls[smallest]
	x = 0
	for j in range(i):
		x = x * 10 + num_ls[j]
	num_ls = sorted(num_ls[i:])
	for j in range(n-i):
		x = x * 10 + num_ls[j]
	if x == number:
		return -1
	return x
print(
next_bigger(6)
)

