11#!/usr/bin/env python3

import sys
import json
import copy
import functools

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
def cmp_func(x,y):
    value = compare_pair([copy.deepcopy(x),copy.deepcopy(y)])
    if value is None:
        return 0
    else:
        return -1 if value else 1

elements = [[[2]],[[6]]]
for line in lines:
    if line.strip():
        elements.append(json.loads(line.strip()))

elements.sort(key=functools.cmp_to_key(cmp_func))
print("Combined index of [[2]] and [[6]] is {}".format((elements.index([[2]])+1)*(elements.index([[6]])+1)))
