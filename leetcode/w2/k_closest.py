#!/bin/env python3
# 973. K Closest Points to Origin

#I am not going to use camelCase in Python.
def k_closest(points: List[List[int]], k: int) -> list[list[int]]:
  min_dist = [ points[0][0]**2 + points[0][1] ** 2]
  min_points = [ points[0] ]
  min_dist_len = 0
  for point in points[1:]:
    cur_min = point[0]**2 + point[1]**2
    if cur_min < min_dist[len(min_dist)//2]:
        start = 0
        end = len(min_dist)//2
    else:
        start = len(min_dist)//2
        end = len(min_dist)
    for i in range(start,end):
        if cur_min > min_dist[i]:
          idx = i
          break
    else:
        idx = end
    min_dist_len += 1
    min_dist.insert(idx, cur_min)
    min_points.insert(idx,point)
    if min_dist_len > k:
      min_dist.pop()
      min_points.pop()
      min_dist_len = k
    
  return min_points
