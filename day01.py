#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

elf_calories = [0]
with open(sys.argv[1]) as file:
    for line in file:
        try:
            elf_calories[-1]+=int(line.strip())
        except ValueError:
            elf_calories.append(0)

elf_calories.sort(reverse=True)
print("Max calories carried by an elf is {}".format(elf_calories[0]))
print("Max calories carried by top 3 elves is {} ({})".format(sum(elf_calories[0:3]),elf_calories[0:3]))


