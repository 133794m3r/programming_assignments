def sum_square_difference(start,end):
	summed_squares=0
	squared_sum=0
	for i in range(start,end+1):
		summed_squares+=pow(i,2)
		squared_sum+=i
	

	return pow(squared_sum,2) - summed_squares
	
print(sum_square_difference(1,100))
