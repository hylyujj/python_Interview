#-*- coding: utf-8 -*-

def firstFibFunc(n):
	before, after = 1, 1
	for i in range(n):
		yield before
		before, after = after, before + after

gen = firstFibFunc(5)
for i in gen:
	print(i)

def consumerFibFunc():
	before, after = 0, 1
	while True:
		yield before
		before, after = after, before + after
		print(before)

def producFibFunc(f):
	f.send(None)
	h = 0
	while h < 5:
		h += 1
		f.send(h)
	f.close()

f = consumerFibFunc()
producFibFunc(f)

def secondFibFunc(num):
	firstValue, secondValue, index = 0, 1, 0
	while index < num:
		yield secondValue
		firstValue, secondValue = secondValue, firstValue + secondValue
		index += 1

for i in secondFibFunc(5):
	print(i)