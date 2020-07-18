# !/usr/bin/env python
#! -*- coding:utf-8 -*-
# Author:   wolfanature
# filename: 977.SquaresOfASortedArray.py


# Given an array of integers A sorted in non-decreasing order, 
# return an array of the squares of each number, 
# also in sorted non-decreasing order.


# Example 1:

# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Example 2:

# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
import cProfile

# my version
class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted([x*x for x in A])
 
# other's version
class Solution2(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = [None for _ in A]
        left, right = 0, len(A) - 1
        for index in range(len(A)-1, -1, -1):
        	if abs(A[left]) > abs(A[right]):
        		result[index] = A[left]**2
        		left += 1
        	else:
        		result[index] = A[right]**2
        		right -= 1
        return result


def testCase():
	s = Solution2()
	a = [-4,-1,0,3,10]
	output = s.sortedSquares(a)
	print a, output
	b = [-7,-3,2,3,11]
	output = s.sortedSquares(b)
	print b, output
	print("test done")

if __name__ == '__main__':
	testCase()


# 总结
# 考察的知识点 1:使用了列表推导式 + sorted

# 不过使用了内部函数sorted













