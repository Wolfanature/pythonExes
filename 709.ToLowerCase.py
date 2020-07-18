# !/usr/bin/env python
#! -*- coding:utf-8 -*-
# Author:   wolfanature
# filename: 709.ToLowerCase.py


# Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.


# Example 1:

# Input: "Hello"
# Output: "hello"
# Example 2:

# Input: "here"
# Output: "here"
# Example 3:

# Input: "LOVELY"
# Output: "lovely"


class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()

def testCase():
	S = Solution()
	testList = [("Hello", "hello"), ("here", "here"), ("LOVELY", "lovely")]
	for item in testList: 
		assert S.toLowerCase(item[0]) == item[1]
	print("test done")

if __name__ == '__main__':
	testCase()














