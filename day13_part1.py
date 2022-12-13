1#!/usr/bin/env python3

import sys
import json

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

with open(sys.argv[1]) as file:
    lines = file.readlines()

def compare_pair(pair):
    while len(pair[0])>0 and len(pair[1])>0:
        compare = [pair[0].pop(0),pair[1].pop(0)]
        if type(compare[0])==int and type(compare[1])==int:
            if compare[0] > compare[1]:
                return False
            elif compare[0] < compare[1]:
                return True
        else:
            retval = compare_pair([([x] if type(x)==int else x) for x in compare])
            if retval is not None:
                return retval
    if len(pair[0])==0 and len(pair[1])==0:
        return None
    else:
        return (len(pair[0])==0)

sum_of_indices = 0
for i in range(0, len(lines), 3):
    if compare_pair([json.loads(lines[i].strip()), json.loads(lines[i+1].strip())]):
        sum_of_indices += int(i/3)+1
print("Sum of indices in right order = {}".format(sum_of_indices))