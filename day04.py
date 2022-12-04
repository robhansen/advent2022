#!/usr/bin/env python3

import sys
import re

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

fully_contained = 0
overlap = 0
with open(sys.argv[1]) as file:
    for line in file:
        vals = re.split("[,|-]", line.strip())
        ranges = [set(range(int(vals[0]),int(vals[1])+1)),set(range(int(vals[2]),int(vals[3])+1))]
        if ranges[0].issubset(ranges[1]) or ranges[1].issubset(ranges[0]):
            fully_contained += 1
        if ranges[0].intersection(ranges[1]):
            overlap += 1
print("{} pairs have one fully contained by the other, {} have overlap".format(fully_contained, overlap))