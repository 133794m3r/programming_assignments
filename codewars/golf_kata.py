#!/usr/bin/env python3

def golfScoreCalculator(pars,scores):
	total_score=0
	for score,par in tuple(zip(scores,pars)):
		total_score+=(int(score)-int(par))
	
	return total_score

print(golfScoreCalculator('443454444344544443','353445334534445344'))

