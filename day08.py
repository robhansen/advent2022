#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

trees = []
with open(sys.argv[1]) as file:
    for line in file:
        trees.append([int(x) for x in [*line.strip()]])
externally_visible = [0] * (len(trees)*len(trees[0]))
internal_visibility = [1] * (len(trees)*len(trees[0]))

class Walk():
    def __init__(self):
        self.height_from_outside = -1
        self.trees_to_see = []
    def step(self,x,y,trees,externally_visible,internal_visibility):
        height = trees[y][x]
        if height > self.height_from_outside:
            self.height_from_outside = height
            externally_visible[(y*len(trees[0]))+x] = 1
        visible = 0
        for tree in self.trees_to_see:
            visible += 1
            if tree >=height:
                break
        internal_visibility[(y*len(trees[0]))+x] = visible * internal_visibility[(y*len(trees[0]))+x]
        if height==9:
            self.trees_to_see = [9]
        else:
            self.trees_to_see.insert(0, height)

for x in range(len(trees[0])):
    walks = [Walk(), Walk()]
    for y in range(len(trees)):
        walks[0].step(x,y,trees,externally_visible,internal_visibility)
        walks[1].step(x,len(trees)-(y+1),trees,externally_visible,internal_visibility)   
for y in range(len(trees)):
    walks = [Walk(), Walk()]
    for x in range(len(trees[0])):
        walks[0].step(x,y,trees,externally_visible,internal_visibility)
        walks[1].step(len(trees[0])-(x+1),y,trees,externally_visible,internal_visibility)
print("{} trees are externally visible, the best tree has a score of {}".format(sum(externally_visible), max(internal_visibility)))
