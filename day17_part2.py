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

tower = np.zeros((1000, 9), dtype=np.int8)
side = np.ones(tower.shape[0])
bottom = np.ones(tower.shape[1])
tower[:,0] = side
tower[:,-1] = side
tower[-1,:] = bottom

def collide(tower,rock,pos):
    return np.sum(np.multiply(tower[pos[0]:pos[0]+rock.shape[0],pos[1]:pos[1]+rock.shape[1]], rock)) > 0

floor = tower.shape[0]-1
fallen_off_the_bottom = 0
jet_index = 0
num_rocks = -1
unique_states = {}
while True:
    num_rocks+=1
    rock = rocks[num_rocks % len(rocks)]
    pos = np.array([floor-rock.shape[0]-3, 3], dtype=np.int32)    
    while True:        
        if not collide(tower,rock,pos+jets[jet_index % len(jets)]):
            pos = pos + jets[jet_index % len(jets)]
        jet_index+=1
        if collide(tower,rock,pos+np.array([1, 0], dtype=np.int32)):
            tower[pos[0]:pos[0]+rock.shape[0],pos[1]:pos[1]+rock.shape[1]] = np.maximum(tower[pos[0]:pos[0]+rock.shape[0],pos[1]:pos[1]+rock.shape[1]], rock)
            floor = min(pos[0],floor)

            if num_rocks > 500: # let things settle down
                # find the height of all 7 columns relative to floor and store those alongside the rock index and jet index
                state_string = "{}-{}".format(num_rocks % len(rocks), jet_index % len(jets))
                for i in range(7):
                    depth = 0
                    while tower[floor+depth][i+1] == 0:
                        depth += 1
                    state_string+="-{}".format(depth)
                if state_string in unique_states:
                    cycle_length = num_rocks-unique_states[state_string][0]
                    if (1000000000000-num_rocks) % cycle_length == 0:
                        height_now = tower.shape[0]-floor-1+fallen_off_the_bottom
                        total_height = ((height_now-unique_states[state_string][1]) * int((1000000000000-num_rocks)/cycle_length))+height_now-1
                        print("Predicted height after 1000000000000 rocks = {}".format(total_height))
                        sys.exit(0)
                else:
                    unique_states[state_string] = (num_rocks, tower.shape[0]-floor-1+fallen_off_the_bottom)

            if floor < 20:
                MOVE_DOWN = 20
                # move everything down MOVE_DOWN and then blank the new bit at the top
                floor += MOVE_DOWN
                fallen_off_the_bottom += MOVE_DOWN
                tower = np.roll(tower, MOVE_DOWN, axis=0)
                tower[0:MOVE_DOWN,1:8] = np.zeros((MOVE_DOWN, 7), dtype=np.int8)
            break
        else:
            pos = pos + np.array([1, 0], dtype=np.int32)
