def fast_lcm(a,b):
	lcm=0;
	gcd=0;

	if a==0 or b==0:
		return 0
	elif a==1:
		return b
	elif b==1:
		return a

	gcd=gcd_fast(a,b)[0]
	lcm=(a//gcd)*b

	return lcm
	
def gcd_fast(a,b):
	gcd=0;
	x=0;
	y=0;
	x=0
	#if a or b is zero return the other value and the coeffecient's accordingly.
	if a==0:
		return (b,0,1)
	elif b==0:
		return (a,0,1)
	#otherwise actually perform the calculation.
	else:
		#set the gcd x and y according to the outputs of the function.
		# a is b (mod) a. b is just a.
		gcd, x, y = gcd_fast(b % a, a)
		#we're returning the gcd, x equals y - floor(b/a) * x
		# y is thus x.
		return (gcd, y - ( b // a ) * x, x)	
		
def find_minimum_multiple(start,end):
	final=1
	for i in range(start,end+1):
		final=fast_lcm(final,i)
	
	print("The minimum value is {} for the numbers in the range of {}...{}".format(final,start,end))
	
find_minimum_multiple(2,20)
