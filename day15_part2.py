#!/usr/bin/env python3

import sys
import numpy as np
import re

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

sensors = [] #  each sensor is a tuple of (x,y,distance)
with open(sys.argv[1]) as file:
    for line in file.readlines():
        vals = [int(x) for x in re.findall(r'[-\d]+', line)]
        dist = abs(vals[0]-vals[2])+abs(vals[1]-vals[3])
        sensors.append((vals[0],vals[1],dist))

for y in range(0,4000001):
    if y % 100000 == 0:
        print("Check {}".format(y)) # takes a little while to run, so just gives an idea of how it's doing
    spaces_without_beacons = []
    for sensor in sensors:
        minmax_x = [sensor[0]-(sensor[2]-abs(sensor[1]-y)),sensor[0]+(sensor[2]-abs(sensor[1]-y))]
        if minmax_x[0] <= minmax_x[1]:
            spaces_without_beacons.append(minmax_x)
    spaces_without_beacons.sort(key=lambda x: x[0])
    # walk the list and look for a gap
    max_x = None
    for space in spaces_without_beacons:
        if max_x is not None:
            if max_x > 4000000:
                break
            if max_x+1 < space[0]:
                print("gap found! x={},y={}, tuning freq = {}".format(max_x+1,y,((max_x+1)*4000000)+y))
            max_x = max(max_x, space[1])
        else:
            max_x = space[1]
