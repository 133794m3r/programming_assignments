#!/bin/env python3
'''
Python Area of a Rectangle Calculator.
In python it's way easier and requires less comments.
'''
#print the following string telling them what we're doing.
print("Rectangle area calculator.")
#We prompt the user with the string "Enter the base: "
#Then we take that input and make it an integer. Then we set it to base.
base=int(input("Enter the base: "))
#same as above but now for height.
height=int(input("Enter the height: "))
#just multiply them.
area=base*height
'''
then we print it. I'm using {} with .format but you could also do the following.
print("The area was %d square units." % area)
And get the same result.
'''
print("The area was {} square units".format(area))
