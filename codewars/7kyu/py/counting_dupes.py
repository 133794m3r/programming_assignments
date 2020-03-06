#!/usr/bin/env python3
"""
Code Wars 7Kyu Challenge Python Version
By Macarthur Inbody
This script will solve the challenge "duplicates"
It is only guaranted to work with Python3
"""
import sys
#since it's one level above gotta make python do this.
sys.path.insert(0, '..')
from lib import assertion_test

def duplicates(input_string):
"""
duplicates function
It's very simple and simply looks through the string creating a table of previously
found items. If they are found it also adds it to the second seen item. After this it
increases the number of repeated characters case insensitively.
It does this by seeing if it's already been seen once before and also a second time. If it
is in both then it doesn't increment our counter.
arguments:
	{string} input_string the string to search.
returns:
	{num} the number of duplicates found.
"""
	occurences={}
	seen_items={}
	repeats=0
	input_string=input_string.lower()
	for char in input_string:
		if char in occurences:
			if char not in seen_items:
				seen_items[char]=1
				repeats+=1
		else:
			occurences[char]=0
	return repeats

def duplicates_tests():
"""
This function will perform all of the test cases
and verify that the code works the way that it should.
assertion_test function takes the test_data,<function>,expected_value
"""
	assertion_test("abcde",duplicates,0)
	assertion_test("aabbcde",duplicates,2)
	assertion_test("aabBcde",duplicates,2)
	assertion_test("indivisibility",duplicates,1)
	assertion_test("Indivisibilities",duplicates,2)
	assertion_test("aA11",duplicates,2)
	assertion_test("ABBA",duplicates,2)


duplicates_tests()


