# !/usr/bin/env python
#! -*- coding:utf-8 -*-
# Author:   wolfanature
# filename: 1295.FindNumbersWithEvenNumberOfDigits.py

# srcurl: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum([len(str(x)) % 2 == 0 for x in nums])
        

def testCase():
    S = Solution()
    nums = [555, 901, 482, 1771]
    result = S.findNumbers(nums)
    out = 1
    assert(result==out)
    print("result = {S}".format(S=result))
    print("test done")

if __name__ == '__main__':
    testCase()















