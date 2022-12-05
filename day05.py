#!/usr/bin/env python3

import sys
import re

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

def get_crates(text):
	num_crates = int((len(text[-1].rstrip())+1)/4) # len = 3N+(N-1)
	crates = [ [] for x in range(num_crates) ]
	for i in range(0,num_crates):
		for line in reversed(text):
			val = line[(4*i)+1]
			if val.isalpha():
				crates[i].append(val)
	return crates

with open(sys.argv[1]) as file:
	lines = file.readlines()
	for i, line in enumerate(lines):
		if any(char.isdigit() for char in line):
			crates_text = lines[:i]
			instructions = lines[i+2:]
			break

cm_9000 = get_crates(crates_text)
cm_9001 = get_crates(crates_text)
for instruction in instructions:
	vals = [int(x) for x in re.findall(r'\b\d+\b', instruction)] # iterations, from, to
	for i in range(vals[0]):
		cm_9000[vals[2]-1].append(cm_9000[vals[1]-1].pop())
	cm_9001[vals[2]-1].extend(cm_9001[vals[1]-1][-vals[0]:])
	cm_9001[vals[1]-1] = cm_9001[vals[1]-1][:-vals[0]]
print("Cratemaster 9000: {}, Cratemaster 9001: {}".format(''.join([x[-1] for x in cm_9000]),''.join([x[-1] for x in cm_9001])))
