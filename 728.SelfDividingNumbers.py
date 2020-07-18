# !/usr/bin/env python
#! -*- coding:utf-8 -*-
# Author:   wolfanature
# filename: 728.SelfDivingNumbers.py


# A self-dividing number is a number that is divisible by 
# every digit it contains.

# For example, 128 is a self-dividing number 
# because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

# Also, a self-dividing number is not 
# allowed to contain the digit zero.

# Given a lower and upper number bound, 
# output a list of every possible self dividing number, 
# including the bounds if possible.

# Example 1:
# Input: 
# left = 1, right = 22
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

# Note:
# The boundaries of each input argument are 1 <= left <= right <= 10000.

import cProfile

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        # a = xrange(left, right+1)
        # return filter(lambda x: "0" not in str(x) and self.selfFilter(x), a) 
        return filter(lambda x: self.selfFilter(x), xrange(left, right + 1)) 
        # return [x if self.selfFilter(x) for x in xrange(left, right+1)]

    def selfFilter(self, x):
        xStr = str(x)
        if "0" in xStr:
            return False
        i = 0
        for index, eachNum in enumerate(xStr):
            if x % int(eachNum) == 0:
                i += 1
            if i != index + 1:
                return False
        return True

# others' version
class Solution2(object):
    def selfDividingNumbers(self, left, right):
            """
            :type left: int
            :type right: int
            :rtype: List[int]
            """
            L = []
            for i in range(left, right+1):
                xStr = str(i)
                tag = True
                if "0" in xStr:
                    tag = False
                    continue
                for letter in list(xStr):
                    if i % int(letter) != 0:
                        tag = False
                        continue
                if tag:
                    L.append(i)
            return L
    #还是涉及了部分类型转换

# others' version
class Solution3(object):
    def selfDividingNumbers(self, left, right):
            """
            :type left: int
            :type right: int
            :rtype: List[int]
            """
            rtn = []
            for i in range(left, right + 1):
                num = i
                cnt = 0
                while num and num % 10 != 0:
                    if i % (num % 10) == 0:
                        cnt += 1
                    num = num/10
                if cnt == len(str(i)):
                    rtn.append(i)
            return rtn

def testCase():
    s = Solution3()
    b = s.selfDividingNumbers(1, 22)
    print type(b), b

    # cProfile.run("Solution().selfDividingNumbers(1, 222)")
    # cProfile.run("Solution2().selfDividingNumbers(1, 222)")
    pass

if __name__ == '__main__':
	testCase()


# 总结：
#  1.Solution中使用了filter, 又额外写了一个函数 
#  2.Solution2方法看更直接一些， 还是使用了大量的转换
#  3. 如果能避免str, list使用的转换最好，因为测试数据如果大了的话，这一部分也是要花时间的









