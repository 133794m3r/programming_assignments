def assertion_test(test_data,function,should_be):
	"""
	assertion_test function.
	arguments:
		{list} test_data the data to test.
		{int} should_be the integer representing the data.
	returns:
		Nothing.
	
	This function will analyze the data given to it along with what the values should be.
	It will say whether the test was successful or not.
	"""
	result=function(test_data)
	try:
		assert result == should_be
		print(f"Test Passed: result({result}) == expected({should_be})")
	except AssertionError:
		print(f"Test Failed: Expected {should_be} but got {result}.")
