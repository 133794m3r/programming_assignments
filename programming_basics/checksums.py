import re
def sep_and_digits(digits):
	nums=re.findall('[0-9]',digits)
	sep=re.search('[^0-9]',digits)
	sep=(sep.group(0) if sep != None else '')
	return sep,nums

def isbn13(digits,check=True):
	sep,nums = sep_and_digits(digits)
	total_nums=len(nums)-1
	if check==True:
		checksum=nums[total_nums]
		nums=nums[0:total_nums]
	final_sum=0
	for idx,num in enumerate(nums):
		if idx & 1:
			final_sum+=int(num)*3
		else:
			final_sum+=int(num)

	to_check=10-(final_sum % 10)
	if check == True:
		return str(to_check) == checksum
	else:
		return digits+sep+str(to_check)


def isbn10(digits,check=True):
	sep,nums = sep_and_digits(digits)
	total_nums=len(nums)-1
	if check==True:
		checksum=nums[total_nums]
		nums=nums[0:total_nums]
	final_sum=0
	weight=10
	for idx,num in enumerate(nums):
		final_sum+=int(num)*(weight-idx)


	to_check=11-(final_sum % 11)
	if check == True:
		return str(to_check) == checksum
	else:
		return digits+sep+str(to_check)

def tests():
	#TODO: Actually write some tests for isnb10 and isbn13.
	pass

if name == "__main__":
	tests()

