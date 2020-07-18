# !/usr/bin/env python
#! -*- coding:utf-8 -*-
# Author:   wolfanature
# filename: 905.SortArrayByParity.py


# https://leetcode.com/problems/sort-array-by-parity/description/


class Solution(object):
	def sortArrayByParity(self, A):
		"""
        :type A: List[int]
        :rtype: List[int]
        """
		# 使用列表推导式， 不过循环了两遍，还是不够好
		return [x for x in A if x%2==0] + [x for x in A if x%2!=0]


class Solution2(object):
	# other's version
	# 使用了sort方法和lambda
	def sortArrayByParity(self, A):
		A.sort(key = lambda x: x % 2)
		return A


def testCase():
	S = Solution()
	TestList= [3,1,2,4]
	Target=[2,4,3,1]
	result = S.sortArrayByParity(TestList)
	print("result = {S}".format(S=result))
	print("test done")

if __name__ == '__main__':
	testCase()


# 总结
# 考察的知识点 1:array的sort方法 2.lambda的使用













