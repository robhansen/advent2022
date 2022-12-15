#!/usr/bin/env python3

import sys
import numpy as np
import re

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

minmax_x = [None,None] # anything outside these bounds on *any* row could have a beacon
sensors = [] #  each sensor is a tuple of (x,y,distance)
with open(sys.argv[1]) as file:
    for line in file.readlines():
        vals = [int(x) for x in re.findall(r'[-\d]+', line)]
        dist = abs(vals[0]-vals[2])+abs(vals[1]-vals[3])
        sensors.append((vals[0],vals[1],dist))
        if minmax_x[0] is None or vals[0]-dist<minmax_x[0]:
            minmax_x[0] = vals[0]-dist
        if minmax_x[1] is None or vals[1]+dist>minmax_x[1]:
            minmax_x[1] = vals[1]+dist

spaces_without_beacons = 0
for x in range(minmax_x[0],minmax_x[1]):
    for sensor in sensors:
        if abs(x-sensor[0])+abs(2000000-sensor[1]) <= sensor[2]:
            spaces_without_beacons += 1
            break
print("There are {} positions where a beacon cannot be present".format(spaces_without_beacons-1))