#!/usr/bin/env python3
import sys
#since it's one level above gotta make python do this.
sys.path.insert(0, '..')
from lib import assertion_test
def number_months(params):
	import math
	car_value,new_value,can_save,change=params
	cur_month=0
	savings=0
	decrease=1-(change/100)
	money_avail=car_value - new_value
	while money_avail < 0:
		if cur_month & 1 == 1  and cur_month >= 1:
			change+=0.5
			decrease=1-(change/100)
		car_value*=decrease
		new_value*=decrease
		savings+=can_save
		money_avail = (savings + car_value) - new_value
		cur_month+=1
		print(f'old_car: {car_value} new_car:{new_value} savings:{savings}')
		print('month: {} change percent: {} money_available: {}'.format(cur_month,change,money_avail))
	return cur_month,round(money_avail)

def test_cars():
	assertion_test([2000,8000,1000,1.5],number_months,[6,766])
	assertion_test([12000,8000,1000,1.5],number_months[0,4000])
	assertion_test([
