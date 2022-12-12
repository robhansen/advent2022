1#!/usr/bin/env python3

import sys
import numpy as np

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

locations = []
class Location:
	def __init__(self, x, y, row_size, column_size, height, is_end, is_start):
		self.pos = np.array([x,y])
		self.row_size = row_size
		self.column_size = column_size
		self.height = height
		self.cost_to_reach = 0 if is_start else 999999
		self.visited = False
		self.is_end = is_end
	def check_surroundings(self): # return cost of E if found, otherwise Null
		global locations
		cardinalities = [np.array([0,1]),np.array([0,-1]),np.array([1,0]),np.array([-1,0])]
		for direction in cardinalities:
			pos = self.pos + direction
			if pos[0]<0 or pos[1]<0 or pos[0]>=self.row_size or pos[1]>=self.column_size:
				continue
			index = (pos[1]*self.row_size)+pos[0]
			if not locations[index].visited and locations[index].cost_to_reach > self.cost_to_reach+1 and locations[index].height <= self.height + 1:
				locations[index].cost_to_reach = self.cost_to_reach+1
				if locations[index].is_end:
					return locations[index].cost_to_reach # no need to continue
				#print("location {} has cost {} to reach".format(index, locations[index].cost_to_reach))
		self.visited = True
		return None

with open(sys.argv[1]) as file:
    lines = file.readlines()

for y, line in enumerate(lines):
	for x, value in enumerate(line.strip()):
		height = ord(value)
		if value == "S":
			height = ord("a")
		if value == "E":
			height = ord("z")
		locations.append(Location(x,y,len(line.strip()),len(lines),height,value == "E",value == "S"))

while True:
	sorted_locations = sorted(locations, key=lambda x: x.cost_to_reach + (999999 if x.visited else 0))
	cost_of_end = locations[(sorted_locations[0].pos[1]*len(lines[0].strip()))+sorted_locations[0].pos[0]].check_surroundings()
	if cost_of_end:
		print("{} steps to reach the end".format(cost_of_end))
		break
