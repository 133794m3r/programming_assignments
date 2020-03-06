"""
Irridecubile Sum of Rationals Solver.
AGPLv3 or Later
Macarthur Inbody
"""
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
	return [n//g,d//g]
print(sum_fracts([[1, 2], [1, 3], [1, 4]]))
