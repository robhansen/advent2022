#!/usr/bin/env python3

import sys
import numpy as np

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

cubes = set()
with open(sys.argv[1]) as file:
    for line in file.readlines():
        cubes.add(line.strip())

exposed_sides = 0
adjacencies = [np.array([1,0,0], dtype=np.int32),np.array([-1,0,0], dtype=np.int32),
               np.array([0,1,0], dtype=np.int32),np.array([0,-1,0], dtype=np.int32),
               np.array([0,0,1], dtype=np.int32),np.array([0,0,-1], dtype=np.int32)]
for cube in list(cubes):
    coords = np.array(cube.split(","), dtype=np.int32)
    for adjacent in adjacencies:
        if (",".join([str(x) for x in list(coords+adjacent)])) not in cubes:
            exposed_sides+=1

print("{} exposed sides".format(exposed_sides))


