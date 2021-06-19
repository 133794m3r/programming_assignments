"""
Test Cases
target 1, start_fuel = 1, stations = []
output 0

#2
target 100
start = 1
stations = [ [10,100] ]
output -1

#3
target = 100
startFuel = 10
stations = [[10,60],[20,30],[30,30],[60,40]]
"""


"""

"""

def min_refuels(target,start_fuel,stations):
	if target <= start_fuel:
		return 0
	from queue import PriorityQueue
	q = PriorityQueue()
	fuel_left = start_fuel
	ans = 0
	q.put(0)
	x = 0
	prev_station = (0,0)
	stations += [(target,0)]
	for station in stations:
		fuel_left -= (station[0] - prev_station[0])
		while not q.empty() and fuel_left < 0:
			ans+=1
			fuel_left -= q.get()
		if fuel_left < 0:
			return -1
		q.put(-station[1])
		prev_station = station
	return ans

print('#1')
print(min_refuels(1,1,[]))
print('#2')
print(min_refuels(100,1,[[10,100]]))
print('#3')
print(min_refuels(100,10,[[10,60],[20,30],[30,30],[60,40]]))