# !/usr/bin/env python
#! -*- coding:utf-8 -*-
# Author:   wolfanature
# filename: 1431.KidsWithTheGreatestNumberOfCandies.py

# srcurl: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        Max = max(candies)
        return [x+extraCandies>=Max for x in candies]
        

def testCase():
    S = Solution()
    candies = [4,2,1,1,2]
    extraCandies = 1
    result = S.kidsWithCandies(candies, extraCandies)
    print("result = {S}".format(S=result))
    print("test done")

if __name__ == '__main__':
    testCase()















