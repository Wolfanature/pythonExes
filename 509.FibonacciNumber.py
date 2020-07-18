# !/usr/bin/env python
#! -*- coding:utf-8 -*-
# Author:   wolfanature
# filename: 509.FibonacciNumber.py


# The Fibonacci numbers, commonly denoted F(n) form a sequence, 
# called the Fibonacci sequence, such that each number 
# is the sum of the two preceding ones, starting from 0 and 1. 
# That is,

# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), for N > 1.
# Given N, calculate F(N).

 
# Example 1:

# Input: 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# Example 2:

# Input: 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
# Example 3:

# Input: 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

# Note:

# 0 ≤ N ≤ 30.

# my version
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        a, b = 0, 1 
        for i in range(N):
            a, b = b, a+b
        return a

# other's version
class Solution2(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 1:
            return N
        res = [0, 1, 1]
        for i in range(2, N):
            res.append(res[-1]+res[-2])
        return res[-1]


def testCase():
    s = Solution2()
    for i in range(5):
        print i, s.fib(i)
    pass

if __name__ == '__main__':
	testCase()


# 总结：
#  1.先排序，取每一组的第一个，加和
#  2. sorted, [::2], sum








