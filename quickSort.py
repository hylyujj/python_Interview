#encoding=utf-8

#快速排序
#算法分析：一列无序的列表中，取列表第一个元素为基准数据。
#设置两个变量，i = 0, j = len(list) - 1。
#从后面向前比较(j = j - 1)，如果该数据比基准数据小，则将该数据跟基准数据交换。
#从前面向后比较(i = i + 1)，如果该数据比基准数据大，则将该数据跟基准数据交换。
#然后递归执行。
def QuickSort(listValue, start, end):
	"""

	"""
	if start < end:
		i, j = start, end
		baseNumber = listValue[i]

		while i < j:
			while (i < j) and (listValue[j] >= baseNumber):
				j = j - 1

			listValue[i] = listValue[j]

			while (i < j) and (listValue[i] < baseNumber):
				i = i + 1
			listValue[j] = listValue[i]
		# 将第一轮走完的i位置的值设置为基准数据
		listValue[i] = baseNumber
		QuickSort(listValue, start, i - 1)
		QuickSort(listValue, j + 1, end)

if __name__ == "__main__":
	listValue = [49, 38, 65, 97, 76, 13, 27, 49]
	print("Quick Sort")
	QuickSort(listValue, 0, len(listValue) - 1)
	print(listValue, 2222222)