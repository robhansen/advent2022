#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

sum_of_small_dirs = 0
dir_sizes = []
def set_dir_size(size):
    global sum_of_small_dirs
    global dir_sizes
    dir_sizes.append(size)
    if size < 100000:
        sum_of_small_dirs += size

def process_instructions(instructions, is_base=False):    
    total_size = 0
    while len(instructions) > 0:
        tokens = instructions.pop(0).strip().split()
        if tokens[0] == "$":
            if tokens[1] == "cd":
                if tokens[2].isalpha():
                    dir_size,to_base,instructions = process_instructions(instructions)
                    total_size += dir_size
                    if to_base and not is_base:
                        set_dir_size(total_size)
                        return total_size, True, instructions
                elif tokens[2]!="/" or not is_base:
                    set_dir_size(total_size)
                    return total_size, tokens[2]=="/", instructions
        elif tokens[0].isdigit():
            total_size += int(tokens[0])
    set_dir_size(total_size)
    return total_size, True, [] 

with open(sys.argv[1]) as file:
    total_size, is_base, instructions = process_instructions(file.readlines(), True)
    dir_sizes.sort()
    for size in dir_sizes:
        if size + 40000000 > total_size:
            print("Size of summed small dirs: {}, size of smallest dir to delete: {}".format(sum_of_small_dirs, size))
            break
