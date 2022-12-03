#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

def getValue(c):
    val = ord(c)
    if val < 97:
        return val-38
    else:
        return val-96

individual_priorities = 0
trio_priorities = 0
trio = []
with open(sys.argv[1]) as file:
    for line in file:
        stripped = line.strip()
        trio.append(stripped)
        half1, half2 = stripped[:len(stripped)//2], stripped[len(stripped)//2:]
        individual_priorities += getValue(set(half1).intersection(half2).pop())
        if len(trio) >= 3:
            partial = set(trio[0]).intersection(trio[1])
            trio_priorities += getValue(partial.intersection(trio[2]).pop())
            trio = []
print("Summed individual priorities = {}, trio priorities = {}".format(individual_priorities,trio_priorities))