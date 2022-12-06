#!/usr/bin/env python3

import sys
import re

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

with open(sys.argv[1]) as file:
    values = file.readline().strip()

eval_window = [values[0]] * 14 # hack so it will always be non-unique until fully filled from values
sequence_of_4_found = False
for i, value in enumerate(values):    
    eval_window.pop(0)
    eval_window.append(value)
    if not sequence_of_4_found and len(set(eval_window[-4:])) >= 4:
        print("unique sequence of 4 {} after {} characters".format(eval_window[-4:], i+1))
        sequence_of_4_found = True
    if len(set(eval_window)) >= 14:
        print("unique sequence of 14 {} after {} characters".format(eval_window, i+1))
        break
