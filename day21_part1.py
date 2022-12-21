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
            operations[tokens[0]] = {"num1": toks[0], "num2": toks[2]}
            if toks[1]=="+":
                operations[tokens[0]]["operation"] = lambda a,b:a+b
            elif toks[1]=="-":
                operations[tokens[0]]["operation"] = lambda a,b:a-b
            elif toks[1]=="*":
                operations[tokens[0]]["operation"] = lambda a,b:a*b
            elif toks[1]=="/":
                operations[tokens[0]]["operation"] = lambda a,b:a/b

while True:
    for key in operations:
        if operations[key]["num1"] in values and operations[key]["num2"] in values:
            values[key] = operations[key]["operation"](values[operations[key]["num1"]],values[operations[key]["num2"]])
            del operations[key]
            break
    if "root" in values:
        print("root = {}".format(values["root"]))
        break