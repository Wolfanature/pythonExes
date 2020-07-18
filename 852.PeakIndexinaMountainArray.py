# !/usr/bin/env python
#! -*- coding:utf-8 -*-
# Author:   wolfanature
# filename: 852.PeakIndexinaMountainArray.py


# https://leetcode.com/problems/peak-index-in-a-mountain-array/



# Let's call an array A a mountain if the following 
# properties hold:

# A.length >= 3
# There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
# Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

# Example 1:

# Input: [0,1,0]
# Output: 1
# Example 2:

# Input: [0,2,1,0]
# Output: 1
# Note:

# 3 <= A.length <= 10000
# 0 <= A[i] <= 10^6
# A is a mountain, as defined above.

class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        index = 0
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                index = i
                break
        return index

class Solution2(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return A.index(max(A))
        

def testCase1():
	A = [0, 1, 2, 1]
	s = Solution()
	# print(s.peakIndexInMountainArray(A))
	assert 2 == s.peakIndexInMountainArray(A)
	A = [0, 1, 0]
	# print(s.peakIndexInMountainArray(A))
	assert 1 == s.peakIndexInMountainArray(A)
	A = [0, 2, 1, 0]	
	# print(s.peakIndexInMountainArray(A))
	assert 1 == s.peakIndexInMountainArray(A)

import cProfile
A = [i for i in range(50000)] + [50000-j for j in range(50000)]

s = Solution()
s2 = Solution2()

def testCase2():
	cProfile.run("s.peakIndexInMountainArray(A)")
	cProfile.run("s2.peakIndexInMountainArray(A)")


def test():
	# testCase1()
	testCase2()


if __name__ == '__main__':
	test()













