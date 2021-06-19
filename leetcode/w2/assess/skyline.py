def get_skyline(buildings):
	from heapq import heappush as hpush, heappop as hpop
	if len(buildings) == 1:
		return [ [buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]

	h, res = [],[]
	cur_item, n = 0, len(buildings)
	points = []
	for building in buildings:
		l,r,h = building
		points.append(l)
		points.append(r)

	points.sort()
	points = set(points)


	def remove_building(b):
		while h:
			if h[0][1] > b > h[0][0]:
				hpop(h)
			else:
				break

	skyline_height = 0
	for point in points:
		for i in range(0,n):
			if buildings[i][1] > point > buildings[i][0]:
				break
			hpush(h,buildings[i])
		remove_building(point)
		if h and skyline_height != h[0][2]:
			skyline_height = h[0][2]
			res.append([point, skyline_height])
		elif not h and skyline_height != 0:
			res.append([point,0])
			skyline_height = 0

	return res