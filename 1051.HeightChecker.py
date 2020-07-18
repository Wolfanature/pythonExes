# !/usr/bin/env python
#! -*- coding:utf-8 -*-
# Author:   wolfanature
# filename: 1051.HeightChecker.py

# Students are asked to stand in non-decreasing order of 
# heights for an annual photo.

# Return the minimum number of students not
# standing in the right positions.  
# (This is the number of students that must
# move in order for all students to be 
# standing in non-decreasing order of height.)


# Example 1:

# Input: [1,1,4,2,1,3]
# Output: 3
# Explanation: 
# Students with heights 4, 3 and the last 1 are not 
# standing in the right positions.
 

# Note:

# 1 <= heights.length <= 100
# 1 <= heights[i] <= 100



import cProfile


class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        ordered = sorted(heights)
        cnt = 0
        for index, num in enumerate(heights):
            if num != ordered[index]:
                cnt += 1
        return cnt
        
# other's version
class Solution1(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        return sum([i != j for i, j in zip(heights, sorted(heights))])

def testCase1():
    s = Solution1()
    heights = [1,1,4,2,1,3]
    expect = 3
    print s.heightChecker(heights)
    print("expect=", expect)

def test():
	# cProfile.run("testCase1()")
	# cProfile.run("testCase2()")
	testCase1()
	# testCase2()
	print("test done")


if __name__ == '__main__':
	test()



# 总结
# zip和sorted使用








