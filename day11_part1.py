#!/usr/bin/env python3

import sys
import math

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

class Monkey():
    def __init__(self, items, operation, divisor, on_true, on_false):
        self.items = items
        self.divisor = divisor
        self.on_true = on_true
        self.on_false = on_false
        self.inspections = 0

        if operation[1].isdigit():
            if operation[0] == "+":
                self.operation = lambda a: a+int(operation[1])
            else:
                self.operation = lambda a: a*int(operation[1])
        else:
            self.operation = lambda a: a*a

    def take_turn(self, monkeys):
        self.inspections += len(self.items)
        for item in self.items:
            item = math.floor(self.operation(item)/3)
            if item % self.divisor == 0:
                monkeys[self.on_true].items.append(item)
            else:
                monkeys[self.on_false].items.append(item)
        self.items = []

monkeys = []
with open(sys.argv[1]) as file:
    lines = [x.strip().replace(',', '') for x in file.readlines()]
    for i in range(int((len(lines)+1)/7)):
        monkeys.append(Monkey([int(x.strip()) for x in lines[(i*7)+1].split(" ")[2:]], 
                              lines[(i*7)+2].split()[4:],
                              int(lines[(i*7)+3].split()[3]),
                              int(lines[(i*7)+4].split()[5]),
                              int(lines[(i*7)+5].split()[5])))

for i in range(20):
    for monkey in monkeys:
        monkey.take_turn(monkeys)
monkeys.sort(key=lambda x: x.inspections, reverse=True)
print("Monkey business value: {}".format(monkeys[0].inspections*monkeys[1].inspections))
