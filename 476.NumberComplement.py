# !/usr/bin/env python
#! -*- coding:utf-8 -*-
# Author:   wolfanature
# filename: 476.NumberComplement.py


# Given a positive integer, output its complement number. 
# The complement strategy is to flip the bits of its binary representation.

# Note:
# The given integer is guaranteed to fit within the range of a 32-bit signed integer.
# You could assume no leading zero bit in the integer’s binary representation.


# Example 1:
# Input: 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits), 
#             and its complement is 010. So you need to output 2.

# Example 2:
# Input: 1
# Output: 0
# Explanation: The binary representation of 1 is 1 (no leading zero bits), 
#             and its complement is 0. So you need to output 0.


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return ~(-num+1)&num
        



if __name__ == '__main__':
	solution = Solution()
	testList = [5, 1]
	for moves in testList:
		print solution.findComplement(moves)













