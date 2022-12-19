#!/usr/bin/env python3

import sys
import numpy as np
import copy

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

cubes = set()
min_vals = np.array([9999,9999,9999], dtype=np.int32)
max_vals = np.array([-9999,-9999,-9999], dtype=np.int32)
with open(sys.argv[1]) as file:
    for line in file.readlines():
        cubes.add(line.strip())
        coords = np.array(line.strip().split(","), dtype=np.int32)
        min_vals = np.minimum(coords, min_vals)
        max_vals = np.maximum(coords, max_vals)

adjacencies = [np.array([1,0,0], dtype=np.int32),np.array([-1,0,0], dtype=np.int32),
               np.array([0,1,0], dtype=np.int32),np.array([0,-1,0], dtype=np.int32),
               np.array([0,0,1], dtype=np.int32),np.array([0,0,-1], dtype=np.int32)]

def create_cube(coords, cubes):
    for i in range(3): # new cube is outside the hull of the originals
        if coords[i] < min_vals[i] or coords[i] > max_vals[i]:
            return True
    cubes.add(",".join([str(x) for x in list(coords)]))
    for adjacent in adjacencies:
        if (",".join([str(x) for x in list(coords+adjacent)])) not in cubes:
            if create_cube(coords+adjacent, cubes):
                return True
    return False

exposed_sides = 0
for cube in list(cubes):
    coords = np.array(cube.split(","), dtype=np.int32)
    for adjacent in adjacencies:
        if (",".join([str(x) for x in list(coords+adjacent)])) not in cubes:
            if create_cube(coords+adjacent, copy.deepcopy(cubes)):
                exposed_sides += 1          

print("{} exposed to outside sides".format(exposed_sides))


