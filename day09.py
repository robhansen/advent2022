#!/usr/bin/env python3

import sys
import numpy as np

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

rope = [ np.array([0,0], dtype=np.int32) for x in range(10) ]
visited = [ {tuple(rope[x])} for x in range(len(rope)) ]

def move_rope(move_vector, rope, visited):
    rope[0]+=move_vector
    for i in range(len(rope)-1):
        distance = np.linalg.norm(rope[i]-rope[i+1])
        if distance > 1.75:
            rope[i+1]+=np.array(np.clip(rope[i]-rope[i+1], -1, 1), dtype=np.int32)
        visited[i+1].add(tuple(rope[i+1]))

with open(sys.argv[1]) as file:
    for line in file:
        for i in range(int(line[2:].rstrip())):
            if line[0] == 'U':
                move_rope(np.array([0,-1]), rope, visited)
            elif line[0] == 'D':
                move_rope(np.array([0,1]), rope, visited)
            elif line[0] == 'L':
                move_rope(np.array([-1,0]), rope, visited)
            elif line[0] == 'R':
                move_rope(np.array([1,0]), rope, visited)
print("Initial tail visited {} locations, final tail visited {} locations".format(len(visited[1]),len(visited[9])))
