def sum_fracts(lst):
	import math
	d=1
	out=0
	n=0
	if len(lst) == 0:
		return None
	for frac in lst:
		d*=frac[1]
	for frac in lst:
		n+=frac[0]*(d // frac[1])
	
	g=math.gcd(n,d)
	n=(n//g)
	d=(d//g)
	return [n,d] if d > 1 else n
