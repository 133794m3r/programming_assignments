"""
For every bar ‘x’, we calculate the area with ‘x’ as the smallest bar in the
rectangle. If we calculate such area for every bar ‘x’ and find the maximum of
all areas, our task is done. How to calculate area with ‘x’ as smallest bar?
We need to know index of the first smaller (smaller than ‘x’) bar on left of ‘x’
and index of first smaller bar on right of ‘x’. Let us call these indexes as
‘left index’ and ‘right index’ respectively.

We traverse all bars from left to right, maintaining a stack of bars. Every bar
is pushed to the stack once. A bar is popped from stack when we see a bar of
smaller  height. When a bar is popped, we calculate the area with the popped bar
as smallest bar. How do we get left and right indexes of the popped bar? The
current index tells us the ‘right index’ and index of previous item in stack is
the ‘left index’.
"""


def largestRectangleArea(heights):
	pass
