#!/usr/bin/env python3

import sys
import unittest
import math

def move_element_in_array(elements, index, move_by):
	if move_by < 0:
		move_by = int(math.fmod(move_by, len(elements)-1))
	element = elements.pop(index)
	elements.insert((index+move_by)%(len(elements)), element)

# 50 lines of unit tests for a 4-line function seems about right...
def test_elements(index, move_by):
	elements = ["0","1","2","3","4","5","6"]
	move_element_in_array(elements, index, move_by)
	return "".join(elements)
class TestMoveElement(unittest.TestCase):
	def test1(self):
		self.assertEqual("0123456", test_elements(0, 0))
	def test1b(self):
		self.assertEqual("0123456", test_elements(3, 0))
	def test2(self):
		self.assertEqual("6012345", test_elements(6, 0))
	def test3(self):
		self.assertEqual("1023456", test_elements(0, 1))
	def test4(self):
		self.assertEqual("0124356", test_elements(3, 1))
	def test4b(self):
		self.assertEqual("0612345", test_elements(6, 1))
	def test5(self):
		self.assertEqual("1230456", test_elements(0, 3))
	def test6(self):
		self.assertEqual("0126345", test_elements(6, 3))
	def test7(self):
		self.assertEqual("3012456", test_elements(3, 3))
	def test8(self):
		self.assertEqual("0412356", test_elements(4, 3))
	def test9(self):
		self.assertEqual("0123456", test_elements(0, 6))
	def test10(self):
		self.assertEqual("0123456", test_elements(3, 6))
	def test11(self):
		self.assertEqual("6012345", test_elements(6, 6))
	def test12(self):
		self.assertEqual("1023456", test_elements(0, 7))
	def test13(self):
		self.assertEqual("0124356", test_elements(3, 7))
	def test14(self):
		self.assertEqual("0612345", test_elements(6, 7))
	def test15(self):
		self.assertEqual("1023456", test_elements(0, 13))
	def test16(self):
		self.assertEqual("0124356", test_elements(3, 13))
	def test17(self):
		self.assertEqual("0612345", test_elements(6, 13))
	def test18(self):
		self.assertEqual("1234506", test_elements(0, -1))
	def test19(self):
		self.assertEqual("0132456", test_elements(3, -1))
	def test20(self):
		self.assertEqual("0123465", test_elements(6, -1))
	def test21(self):
		self.assertEqual("1234506", test_elements(0, -7))
	def test22(self):
		self.assertEqual("0132456", test_elements(3, -7))
	def test23(self):
		self.assertEqual("0123465", test_elements(6, -7))

if len(sys.argv) != 2:
    print("Help: {} <filename>".format(sys.argv[0]))
    sys.exit(0)

elements = []
with open(sys.argv[1]) as file:
	for i, line in enumerate(file.readlines()):
		elements.append([int(line.strip())*811589153,i])

for m in range(10): # mix 10 times
	for i in range(len(elements)):
		for j in range(len(elements)):
			if isinstance(elements[j], list) and elements[j][1]==i:
				move_element_in_array(elements, j, elements[j][0])
				break

for i in range(len(elements)):
	if elements[i][0]==0:
		index0 = i
summed = 0
for i in [1000,2000,3000]:
	summed+=elements[(index0+i) % len(elements)][0]
print("0 is at index {}, sum of 1000th, 2000th and 3000th after that is {}".format(index0, summed))
