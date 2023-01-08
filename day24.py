#!/usr/bin/env python3

import sys
import numpy as np

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

start = None
with open(sys.argv[1]) as file:
    lines = file.readlines()

def debug_display(map_to_print):
    for y in range(1, map_to_print.shape[0]-1):
        line = ""
        for x in range(1, map_to_print.shape[1]-1):
            if map_to_print[y,x] < 0:
                line += "#"
                continue
            matches = 0
            to_add = "."
            for key, value in MAP_LOOKUP.items():
                if map_to_print[y,x] & value:
                    to_add=key
                    matches += 1
            line += to_add if matches < 2 else str(matches)
        print(line)

def add_total_map(maps, next_map):
    full_map = np.pad(next_map, 2, 'constant', constant_values=-1)
    full_map[1,2] = 0
    full_map[full_map.shape[0]-2,full_map.shape[1]-3] = 0
    #debug_display(full_map)
    maps.append((next_map, full_map))
def add_next_map(maps):
    next_map = np.zeros((maps[-1][0].shape[0], maps[-1][0].shape[1]), dtype=np.int8)
    for blizzard_type in BLIZZARDS:
        and_map = np.full((maps[-1][0].shape[0], maps[-1][0].shape[1]), blizzard_type[0], dtype=np.int8)
        blizzes = np.bitwise_and(maps[-1][0], and_map)
        next_map += np.roll(blizzes, blizzard_type[1], axis=blizzard_type[2])
    add_total_map(maps, next_map)

maps = []
first_map = np.zeros((len(lines)-2, len(lines[0].strip())-2), dtype=np.int8)
BLIZZARDS = [(1, 1, 0), (2, -1, 0), (4, -1, 1), (8, 1, 1)] # bitwise match, shift amount, axis
MAP_LOOKUP = {"v": 1, "^": 2, "<": 4, ">": 8, ".": 0}
for y in range(first_map.shape[0]):
	for x in range(first_map.shape[1]):
		first_map[y,x] = MAP_LOOKUP[lines[y+1].strip()[x+1]]
add_total_map(maps, first_map)


MOVES = [np.array([-1,0], dtype=int),np.array([1,0], dtype=int),np.array([0,-1], dtype=int),np.array([0,1], dtype=int),np.array([0,0], dtype=int)]
def evaluate_move(pos, steps, visited, moves_to_take, maps, target):
    # have we reached the target?
    if np.array_equal(pos, target):
        return True

    # add all other options to moves_to_take if valid:
    steps += 1
    if steps >= len(maps):
        add_next_map(maps)
    for move in MOVES:
        new_pos = pos+move

        # check it's valid and not redundant
        if maps[steps][1][tuple(new_pos)]!=0:
            continue
        visit_string = "{}_{}".format(new_pos, steps)
        if visit_string in visited:
            continue
        visited.add(visit_string)
        
        cost = abs(target[0]-new_pos[0])+abs(target[1]-new_pos[1])+steps # use distance from target as part of cost
        moves_to_take.append((cost, new_pos, steps))
    return False

def get_steps(start_point, end_point, initial_step_count, maps):
    visited = set()
    moves_to_take = [(0, start_point, initial_step_count)]
    while True:
        moves_to_take.sort(key=lambda x: x[0])
        next_move = moves_to_take.pop(0)
        if evaluate_move(next_move[1], next_move[2], visited, moves_to_take, maps, end_point):
            return next_move[2]

TOP_POINT = np.array([1, 2], dtype=int)
BOTTOM_POINT = np.array([maps[0][1].shape[0]-2, maps[0][1].shape[1]-3], dtype=int)
there_steps = get_steps(TOP_POINT, BOTTOM_POINT, 0, maps)
there_and_back_steps = get_steps(BOTTOM_POINT, TOP_POINT, there_steps, maps)
there_and_back_and_there_steps = get_steps(TOP_POINT, BOTTOM_POINT, there_and_back_steps, maps)
print("Takes {} steps to get there, {} to get back, {} to get there again".format(there_steps, there_and_back_steps, there_and_back_and_there_steps))