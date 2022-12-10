#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

display = ""
def add_to_display(register_values):
    global display
    position = ((len(register_values)-1) % 40)
    display += "#" if (register_values[-1] >= position-1 and register_values[-1] <= position+1) else "."
    if (position == 39):
        print(display)
        display = ""

register_values = [1]

with open(sys.argv[1]) as file:
    for line in file:
        add_to_display(register_values)
        register_values.append(register_values[-1])
        if line.strip() != "noop": #addx
            add_to_display(register_values)
            register_values.append(register_values[-1] + int(line.strip().split()[1]))

signal_strength_sum = 0
for val in [20,60,100,140,180,220]:
    signal_strength_sum += (register_values[val-1]*val)
print("Sum of signal strength = {}".format(signal_strength_sum))
print(display)