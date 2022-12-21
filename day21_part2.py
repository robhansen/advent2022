#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

values = {}
operations = {}

with open(sys.argv[1]) as file:
    for line in file.readlines():
        tokens = line.strip().split(": ")
        if tokens[1].isdigit():
            values[tokens[0]] = int(tokens[1])
        else:
            toks = tokens[1].split(" ")
            operations[tokens[0]] = {"nums": [toks[0], toks[2]]}
            if toks[1]=="+":
                operations[tokens[0]]["operation"] = lambda a,b:a+b
                operations[tokens[0]]["reverse"] = [lambda b,c:c-b, lambda a,c:c-a]
            elif toks[1]=="-":
                operations[tokens[0]]["operation"] = lambda a,b:a-b
                operations[tokens[0]]["reverse"] = [lambda b,c:b+c, lambda a,c:a-c]
            elif toks[1]=="*":
                operations[tokens[0]]["operation"] = lambda a,b:a*b
                operations[tokens[0]]["reverse"] = [lambda b,c:c/b, lambda a,c:c/a]
            elif toks[1]=="/":
                operations[tokens[0]]["operation"] = lambda a,b:a/b
                operations[tokens[0]]["reverse"] = [lambda b,c:c*b, lambda a,c:a/c]
del values["humn"]

while True:
    found = False
    for key in operations:
        if operations[key]["nums"][0] in values and operations[key]["nums"][1] in values:
            values[key] = operations[key]["operation"](values[operations[key]["nums"][0]],values[operations[key]["nums"][1]])
            del operations[key]
            found = True
            break
    if not found:
        break

values["root"] = values[operations["root"]["nums"][0]] if (operations["root"]["nums"][0] in values) else values[operations["root"]["nums"][1]]
print("got as far as possible - now run the remainder in reverse to find root = {}".format(values["root"]))

while True:
    for key in operations:
        if key in values:
            reverse_to = operations[key]["nums"][0] if (operations[key]["nums"][1] in values) else operations[key]["nums"][1]
            i = 0 if (operations[reverse_to]["nums"][1] in values) else 1 
            values[reverse_to] = operations[reverse_to]["reverse"][i](values[operations[reverse_to]["nums"][1-i]],values[key])
            del operations[key]
            break
    if len(operations)==1:
        print("yell {} to equal root's value of {}".format(values[list(operations.keys())[0]], values["root"]))
        break
