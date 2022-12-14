#!/usr/bin/env python3

import sys
import numpy as np

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

with open(sys.argv[1]) as file:
    lines = file.readlines()

min_x = 9999999 # we know the min y is 0
max_xy = [0,0]
rock_lines = []
with open(sys.argv[1]) as file:
    for line in file.readlines():
        points = [[int(y) for y in x.split(",")] for x in line.strip().split(" -> ")]
        for point in points:
            min_x = min(min_x, point[0])
            max_xy[0] = max(max_xy[0], point[0])
            max_xy[1] = max(max_xy[1], point[1])
        for i in range(len(points)-1):
            rock_lines.append([points[i],points[i+1]])
max_xy[1] += 2 # fllor
min_x = min(min_x,500-max_xy[1])
max_xy[0] = max(max_xy[0],500+max_xy[1])
rock_lines.append([[min_x,max_xy[1]],[max_xy[0],max_xy[1]]]) # floor

spaces = np.zeros((max_xy[1]+1,(max_xy[0]-min_x)+1))
for line in rock_lines:
    for i in range(abs(line[0][0]-line[1][0])+1):
        for j in range(abs(line[0][1]-line[1][1])+1):
            spaces[min(line[0][1],line[1][1])+j][min(line[0][0],line[1][0])+i-min_x] = 1

def drop_sand(spaces):
    positions = [np.array([1,0]),np.array([1,-1]),np.array([1,1])]
    grains = 0
    while True:
        sand_pos = np.array([0,500-min_x])
        steps = 0
        while True:
            sand_moved = False
            for position in positions:
                if not spaces[tuple(sand_pos + position)]:
                    sand_pos += position
                    sand_moved = True
                    steps += 1
                    break
            if not sand_moved:
                spaces[tuple(sand_pos)] = 8
                grains += 1
                if steps==0:
                    return grains
                break

print("Room for {} grains of sand".format(drop_sand(spaces)))
