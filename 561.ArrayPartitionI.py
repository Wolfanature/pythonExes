# !/usr/bin/env python
#! -*- coding:utf-8 -*-
# Author:   wolfanature
# filename: 561.ArrayPartitionI.py


# Given an array of 2n integers, your task is to group 
# these integers into n pairs of integer, 
# say (a1, b1), (a2, b2), ..., (an, bn) 
# which makes sum of min(ai, bi) 
# for all i from 1 to n as large as possible.

# Example 1:
# Input: [1,4,3,2]

# Output: 4
# Explanation: n is 2, and the maximum sum of 
# pairs is 4 = min(1, 2) + min(3, 4).
# Note:
# n is a positive integer, which is in the range of [1, 10000].
# All the integers in the array will be in the range of [-10000, 10000].


# my version
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        nums2 = sorted(nums)
        for index, num in enumerate(nums2):
            if index % 2 == 0:
                total += num
        return total

# other's version
class Solution2(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])


def testCase():
    s = Solution2()
    rst = s.arrayPairSum([1,2,4,3,6,5])
    print type(rst), rst
    # cProfile.run("Solution().selfDividingNumbers(1, 222)")
    # cProfile.run("Solution2().selfDividingNumbers(1, 222)")
    pass

if __name__ == '__main__':
	testCase()


# 总结：
#  1.先排序，取每一组的第一个，加和
#  2. sorted, [::2], sum








