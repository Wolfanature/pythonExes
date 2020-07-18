# !/usr/bin/env python
#! -*- coding:utf-8 -*-
# Author:   wolfanature
# filename: 1122.RelativeSortArray.py


# link:https://leetcode.com/problems/relative-sort-array/
# Given two arrays arr1 and arr2, the elements of arr2 are distinct, 
# and all elements in arr2 are also in arr1.

# Sort the elements of arr1 such that the 
# relative ordering of items in arr1 are the 
# same as in arr2.  Elements that 
# don't appear in arr2 should be placed at the 
# end of arr1 in ascending order.

 
# Example 1:

# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]
 

# Constraints:

# arr1.length, arr2.length <= 1000
# 0 <= arr1[i], arr2[i] <= 1000
# Each arr2[i] is distinct.
# Each arr2[i] is in arr1.


import cProfile
# my version
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        targetL = []
        tempL = []
        for i in arr2:
            if i in arr1:
                targetL +=  arr1.count(i) * [i]
        for m in arr1:
        	if m not in arr2:
        		tempL.append(m)

        for tempi in sorted(tempL):
            targetL.append(tempi)
        return targetL


# other's version
class Solution1(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        d = dict()
        rest = []
        pre = []

        for x in arr1:
        	if x in arr2:
        		d[x] = d.get(x, 0) + 1
        	else:
        		rest.append(x)

        for y in arr2:
        	pre += [y for _ in range(d[y])]

        return pre+sorted(rest)

# arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]
def testCase1():
	s = Solution1()
	arr1 = [2,3,1,3,2,4,6,7,9,2,19]
	arr2 = [2,1,4,3,9,6]
	expect = [2,2,2,1,4,3,3,9,6,7,19]
	print s.relativeSortArray(arr1, arr2)
	print expect
	print("===========1")

def testCase2():
	s = Solution()
	arr1 = [2,21,43,38,0,42,33,7,24,13,12,27,12,24,5,23,29,48,30,31]
	arr2 = [2,42,38,0,43,21]
	expect = [2,42,38,0,43,21,5,7,12,12,13,23,24,24,27,29,30,31,33,48]
	print s.relativeSortArray(arr1, arr2)
	print expect

def test():
	cProfile.run("testCase1()")
	# cProfile.run("testCase2()")
	# testCase1()
	# testCase2()
	print("test done")


if __name__ == '__main__':
	test()













