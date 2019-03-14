# -*- coding: utf-8 -*-

"""
一个列表a = [1,2,3,4,5,6,7,8,9,10]
一行代码实现列表a下表为偶数的元素每个+3，然后取和
"""

from functools import reduce

a = [1,2,3,4,5,6,7,8,9,10]
print(sum(map(lambda x: x+3, a[::2])))

# 如果要使用reduce，则需要事先定义1个函数
def getSumValue(x, y):
	return x + y
print(reduce(getSumValue, map(lambda x: x+3, a[::2])))

"""
有1个列表a格式
a = [{"company_id": "12"}, {"company_id": "123"}, {"company_id": "1234"}, {"company_id": "1245"}]
有1个列表b格式
a = [{"company_id": "1234"}, {"company_id": "125"}, {"company_id": "1245"}, {"company_id": "123"}]
计算a中存在，同时b中也存在的列表
计算b中存在，同时a中也存在的列表
a中存在，b中不存在的结果
b中存在，a中不存在的结果
"""

a = [{"company_id": "12"}, {"company_id": "123"}, {"company_id": "1234"}, {"company_id": "1245"}]
b = [{"company_id": "1234"}, {"company_id": "125"}, {"company_id": "1245"}, {"company_id": "123"}]

# a中存在，同时b中也存在
print(list(filter(lambda x: x in b, a)))
# b中存在，同时a中也存在
print(list(filter(lambda x: x in a, b)))
# a中存在，b中不存在
print(list(filter(lambda x: x not in b, a)))
# b中存在，a中不存在
print(list(filter(lambda x: x not in a, b)))

