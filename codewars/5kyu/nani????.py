#!/usr/bin/env python3
"""
Can I be considered a Pytohn programmer now?
This only works for single digits sadly. As in one digit input, 
one digit output because I'm being lazy.

"""

#basically this is the heart of the program. We set op to be none.
def exp(num,op=None):
	#if it was called with one arg we just return the num.
	if op is None:
	#otherwise we run the lambda.
		return num

	return op(num)

def zero(op=None):
	#if we've got an op we pass it otherwise we pass None.
    return exp(0,op)

def one(op=None):
    return exp(1,op)

def two(op=None):
    return exp(2,op)

def three(op=None):
    return exp(3,op)

def four(op=None):
    return exp(4,op)

def five(op=None):
    return exp(5,op)

def six(op=None):
    return exp(6,op)

def seven(op=None):
    return exp(7,op)

def eight(op=None):
    return exp(8,op)

def nine(op=None):
    return exp(9,op)

#this is the lambdas that handle the math.
def plus(x):
	#we return a pointer to the lambda that holds the values we're going to work with.
	#basically we set y to be the current x value. Then we run it as x+y once it's evaluated.
    return lambda x,y=x: x+y

#same as it is down here.
def minus(x):
    return lambda x,y=x: x-y

def times(x):
    return lambda x,y=x: x*y

def divided_by(x):
    return lambda x,y=x: x // y

def raised_to(x):
	return lambda x,y=x: x**y
def bitwise_and(x):
	return lambda x,y=x: x&y
def bitwise_xor(x):
	return lambda x,y=x: x^y
def bitwise_or(x):
	return lambda x,y=x: x|y

def bitwise_shiftl(x):
	return lambda x,y=x: x << y

def bitwise_shiftr(x):
	return lambda x,y=x: x >> y

def main():
	print("6+7=",six(plus(seven())))
	print("7*5=",seven(times(five())))
	print("3*1=",three(times(one())))
	print("4*2=",four(times(two())))
	print("9//4=",nine(divided_by(four())))
	print("1-2=",one(minus(two())))
	print("2**8=",two(raised_to(eight())))
	print("9&1=",nine(bitwise_and(one())))
	print("3^5=",three(bitwise_xor(five())))
	print("6|3=",six(bitwise_or(three())))
	print("9<<7=",nine(bitwise_shiftl(seven())))
	print("8>>2=",eight(bitwise_shiftr(two())))

if __name__ == "__main__":
	main()
