#encoding=utf-8

class Node(object):
	def __init__(self, value):
		self.value = value
		self.leftChild = None
		self.rightChild = None
		self.father = None
		
class Tree(object):
	def __init__(self):
		self.root = None
		
	def createTree(self, node):
		if self.root:
			if self.root.value > node.value:
				# 左子树
				self.insertIntoLeft(self.root, node)
			elif self.root.value < node.value:
				# 右子树
				self.insertIntoRight(self.root, node)
			else:
				print("Node already in tree")
		else:
			# 根节点
			self.root = node
			
	def insertIntoLeft(self, fatherNode, Sonnode):
		if fatherNode.leftChild:
			leftChildValue = fatherNode.leftChild.value
			if leftChildValue > Sonnode.value:
				self.insertIntoLeft(fatherNode.leftChild, Sonnode)
			elif leftChildValue < Sonnode.value:
				self.insertIntoRight(fatherNode.leftChild, Sonnode)
			else:
				print("Node already in tree")
		else:
			fatherNode.leftChild = Sonnode
			Sonnode.father = fatherNode
	
	def insertIntoRight(self, fatherNode, Sonnode):
		if fatherNode.rightChild:
			rightChildValue = fatherNode.rightChild.value
			if rightChildValue > Sonnode.value:
				self.insertIntoLeft(fatherNode.rightChild, Sonnode)
			elif rightChildValue < Sonnode.value:
				self.insertIntoRight(fatherNode.rightChild, Sonnode)
			else:
				print("Node already in tree")
		else:
			fatherNode.rightChild = Sonnode
			Sonnode.father = fatherNode
	
	def ergodicTree(self):
		if self.root:
			self.ergodicMiddle(self.root)
		else:
			print("Tree is None")
	
	def ergodicBefore(self, node):
		# 前序遍历
		if node:
			print(node.value)
			self.ergodicBefore(node.leftChild)
			self.ergodicBefore(node.rightChild)
		
	def ergodicMiddle(self, node):
		# 中序遍历
		if node:
			self.ergodicMiddle(node.leftChild)
			print(node.value)
			self.ergodicMiddle(node.rightChild)
		
	def ergodicAfter(self, node):
		# 后序遍历
		if node:
			self.ergodicAfter(node.leftChild)
			self.ergodicAfter(node.rightChild)
			print(node.value)

	def ergodicCeng(self, node):
		# 层序遍历
		stack = [node]
		while stack:
			currentNode = stack.pop(0)
			print(currentNode.value)
			if currentNode.leftChild:
				stack.append(currentNode.leftChild)
			if currentNode.rightChild:
				stack.append(currentNode.rightChild)

if __name__ == "__main__":
	testTree = Tree()
	testTree.createTree(Node(100))
	nodeList = [eval("Node(%s)" % i) for i in (50, 150, 40, 70, 20, 45, 90, 120, 140, 170)]
	for eachNode in nodeList:
		testTree.createTree(eachNode)
	testTree.ergodicTree()
	print("EnD")