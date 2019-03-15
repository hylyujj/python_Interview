#-*- coding: utf-8 -*-

def triangles(n):
	triangleList, index = [1], 0
	while index < n:
		yield triangleList
		triangleList = [1] + [triangleList[i] + triangleList[i + 1] for i in range(len(triangleList) - 1)] + [1]
		index += 1
		
for i in triangles(6):
	print(i)

def secondTriangles():
	triangleList = [1]
	while True:
		yield triangleList
		print(triangleList)
		triangleList.append(0)
		triangleList = [triangleList[index - 1] + triangleList[index] for index in range(len(triangleList))]
		
def produceTriangles(intex):
	intex.send(None)
	for i in range(6):
		intex.send(i)
	intex.close()

ccc = secondTriangles()
produceTriangles(ccc)