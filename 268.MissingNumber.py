# !/usr/bin/env python
#! -*- coding:utf-8 -*-
# Author:   wolfanature
# filename: 268.MissingNumber.py



# Given an array containing n distinct numbers 
# taken from 0, 1, 2, ..., n, find the one that is missing from the array.

# Example 1:

# Input: [3,0,1]
# Output: 2
# Example 2:

# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
# Note:
# Your algorithm should run in linear runtime complexity.
#  Could you implement it using only constant extra space complexity?



# my version
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) + 1
        return n*(n-1)/2 - sum(nums)




def testCase():
    s = Solution()
    print s.missingNumber([3,0,1])
    print s.missingNumber([9,6,4,2,3,5,7,0,1])
    pass

if __name__ == '__main__':
	testCase()


# 总结：
#  1.先排序，取每一组的第一个，加和
#  2. sorted, [::2], sum








