#!/usr/bin/env python3
"""
Can I be considered a Python programmer now?
Or Lambda Madness B/C JavaScript shouldn't get all of the anon's fun.
"""



#numbers
zero = lambda op=None: op(0) if op else 0
one = lambda op=None: op(1) if op else 1
two = lambda op=None: op(2) if op else 2
three = lambda op=None: op(3) if op else 3
four = lambda op=None: op(4) if op else 4
five = lambda op=None: op(5) if op else 5
six = lambda op=None: op(6) if op else 6
seven = lambda op=None: op(7) if op else 7
eight = lambda op=None: op(8) if op else 8
nine = lambda op=None: op(9) if op else 9

#operators
plus = lambda x,y=None: (lambda x,y=x:x+y) if not y else x+y
minus = lambda x,y=None: (lambda x,y=x:x-y) if not y else x-y
times = lambda x,y=None: (lambda x,y=x:x*y) if not y else x*y
divided_by = lambda x,y=None: (lambda x,y=x:x//y) if not y else x//y
raised_to=lambda x,y=None: (lambda x,y=x:x**y) if not y else x**y

#bitwise ops.
bitwise_and=lambda x,y=None: (lambda x,y=x:x & y) if not y else x & y
bitwise_xor= lambda x,y=None: (lambda x,y=x:x ^ y) if not y else x ^ y
bitwise_or = lambda x,y=None: (lambda x,y=x:x | y) if not y else x | y
bitwise_shiftl= lambda x,y=None: (lambda x,y=x:x << y) if not y else x << y
bitwise_shiftr= lambda x,y=None: (lambda x,y=x:x >> y) if not y else x >> y

#Main function showing off this insanity.
def main():
	print("6+7=", six(plus(seven())))
	print("7*5=", seven(times(five())))
	print("3*1=", three(times(one())))
	print("4*2=", four(times(two())))
	print("9//4=", nine(divided_by(four())))
	print("1-2=", one(minus(two())))
	print("2**8=", two(raised_to(eight())))
	print("9&1=", nine(bitwise_and(one())))
	print("3^5=", three(bitwise_xor(five())))
	print("6|3=", six(bitwise_or(three())))
	print("9<<7=", nine(bitwise_shiftl(seven())))
	print("8>>2=", eight(bitwise_shiftr(two())))


if __name__ == "__main__":
	main()
