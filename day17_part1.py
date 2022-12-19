#!/usr/bin/env python3

import sys
import numpy as np

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

rocks = [np.array([[1, 1, 1, 1]], dtype=np.int8), 
         np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], dtype=np.int8),
         np.array([[0, 0, 1], [0, 0, 1], [1, 1, 1]], dtype=np.int8),
         np.array([[1], [1], [1], [1]], dtype=np.int8),
         np.array([[1, 1], [1, 1]], dtype=np.int8)]

with open(sys.argv[1]) as file:
    jets = [(np.array([0, 1], dtype=np.int32) if x==">" else np.array([0, -1], dtype=np.int32)) for x in file.readlines()[0].strip()]

tower = np.zeros((2022*4, 9), dtype=np.int8) # overly high but doesn't matter
side = np.ones(tower.shape[0])
bottom = np.ones(tower.shape[1])
tower[:,0] = side
tower[:,-1] = side
tower[-1,:] = bottom

def collide(tower,rock,pos):
    return np.sum(np.multiply(tower[pos[0]:pos[0]+rock.shape[0],pos[1]:pos[1]+rock.shape[1]], rock)) > 0

floor = tower.shape[0]-1
jet_index = 0

for i in range(2022):
    rock = rocks[i % len(rocks)]
    pos = np.array([floor-rock.shape[0]-3, 3], dtype=np.int32)    
    while True:        
        if not collide(tower,rock,pos+jets[jet_index % len(jets)]):
            pos = pos + jets[jet_index % len(jets)]
        jet_index+=1
        if collide(tower,rock,pos+np.array([1, 0], dtype=np.int32)):
            tower[pos[0]:pos[0]+rock.shape[0],pos[1]:pos[1]+rock.shape[1]] = np.maximum(tower[pos[0]:pos[0]+rock.shape[0],pos[1]:pos[1]+rock.shape[1]], rock)
            floor = min(pos[0],floor)
            break
        else:
            pos = pos + np.array([1, 0], dtype=np.int32)

print("Total height = {}".format(tower.shape[0]-floor-1))
