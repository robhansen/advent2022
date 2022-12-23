#!/usr/bin/env python3

import sys
import numpy as np
import json

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

with open(sys.argv[1]) as file:
    lines = file.readlines()

elves = set()
for y, line in enumerate(lines):
    for x, char in enumerate(list(line.strip())):
        if char=="#":
            elves.add(json.dumps([y,x]))
#print(elves)

#board = np.zeros((len(lines), len(lines[0].strip())), dtype=np.int8)
#for y, line in enumerate(lines):
#    for x, char in enumerate(list(line.strip())):
#        if char=="#":
#            board[y,x] = 1
#print(board)

MOVES = [np.array([-1,0]),np.array([1,0]),np.array([0,-1]),np.array([0,1])]
SCAN = [[np.array([-1,-1]),np.array([-1,0]),np.array([-1,1])],
        [np.array([1,-1]),np.array([1,0]),np.array([1,1])],
        [np.array([-1,-1]),np.array([0,-1]),np.array([1,-1])],
        [np.array([-1,1]),np.array([0,1]),np.array([1,1])]]
SURROUNDING = [np.array([-1,-1]),np.array([-1,0]),np.array([-1,1]),np.array([0,1]),np.array([1,1]),np.array([1,0]),np.array([1,-1]),np.array([0,-1])]
facing_index = 0

def is_empty(current, to_check, elves):
    for pos in to_check:
        if (json.dumps((current+pos).tolist())) in elves:
            return False
    return True

def show_elves(elves):
    OFFSET = [2,3]
    for y in range(12):
        display = ""
        for x in range(14):
            display += "#" if json.dumps([y-OFFSET[0],x-OFFSET[1]]) in elves else "."
        print(display)

rounds = 0
while True:
    rounds += 1
    #print("{} moves".format(r))    
    #show_elves(elves)
    proposed_moves = {}
    for elf_string in elves:
        elf = np.array(json.loads(elf_string))
        if is_empty(elf, SURROUNDING, elves):
            #print("{} cannot move".format(elf_string))
            continue # no elves in 8 positions around, so do nothing
        proposed_move = None
        #print("{} can move".format(elf_string))
        for i in range(len(MOVES)):
            if is_empty(elf, SCAN[(facing_index+i) % len(SCAN)], elves):
                #print("{} proposes move {}".format(elf_string, MOVES[(facing_index+i) % len(MOVES)]))
                proposed_move = elf+MOVES[(facing_index+i) % len(MOVES)]
                break
        if proposed_move is not None:
            proposed_string = json.dumps(proposed_move.tolist())
            if proposed_string in proposed_moves:
                proposed_moves[proposed_string]["allowed"] = False
            else:
                proposed_moves[proposed_string] = {"origin": elf_string, "allowed": True}

    any_moves = False
    for move, state in proposed_moves.items():
        if state["allowed"]:
            #print("move from {} to {}".format(state["origin"], move))
            any_moves = True
            elves.remove(state["origin"])
            elves.add(move)

    facing_index = (facing_index+1) % len(MOVES)

    if rounds == 10 or (rounds < 10 and not any_moves):
        mins = np.array([99999999,999999999])
        maxs = np.array([-99999999,-99999999])
        for elf_string in elves:
            elf = np.array(json.loads(elf_string))
            mins = np.minimum(mins,elf)
            maxs = np.maximum(maxs,elf)
        #print(mins, maxs)
        print("Number of empty spaces after {} rounds = {}".format(rounds, ((1+maxs[0]-mins[0])*(1+maxs[1]-mins[1]))-len(elves)))

    if not any_moves:
        print("No further moves after round {}".format(rounds))
        break

#print(elves)


