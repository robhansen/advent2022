#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

OUTCOME_SCORES = [[3,0,6],[6,3,0],[0,6,3]] # array of scores of their plays in an array of my plays
def get_first_score(their_play, my_play):
    return (OUTCOME_SCORES[my_play][their_play])+my_play+1

CHOOSE_SCORES = [[3,1,2],[1,2,3],[2,3,1]] # array of what lose/draw/win is worth in an array of their plays (rock, paper, scissors)
def get_second_score(their_play, my_play):
    return (CHOOSE_SCORES[their_play][my_play])+([0,3,6][my_play])

first_score = 0
second_score = 0
with open(sys.argv[1]) as file:
    for line in file:
        first_score += get_first_score(ord(line[0])-65, ord(line[2])-88)
        second_score += get_second_score(ord(line[0])-65, ord(line[2])-88)
print("First score: {}, second score: {}".format(first_score, second_score))