# !/usr/bin/env python
#! -*- coding:utf-8 -*-
# Author:   wolfanature
# filename: 867.TransposeMatrix.py

# Given a matrix A, return the transpose of A.

# The transpose of a matrix is the matrix flipped over 
# it's main diagonal, switching the row and column indices of the matrix.

 

# Example 1:

# Input: [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
# Example 2:

# Input: [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]

import cProfile


class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(A)
        if rows == 0:
            return []
        cols = len(A[0])
        return [[A[i][j] for i in range(rows)] for j in range(cols)]

        
def testCase1():
    s = Solution()
    A = [[1,2],[4,5],[7,8]]
    A = [[1,2,3],[4,5,6]]
    print s.transpose(A)



def test():
	# cProfile.run("testCase1()")
	# cProfile.run("testCase2()")
	testCase1()
	# testCase2()
	print("test done")


if __name__ == '__main__':
	test()



# 总结
# 列表推导式的使用








