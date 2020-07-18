# !/usr/bin/env python
#! -*- coding:utf-8 -*-
# Author:   wolfanature
# filename: 1002.FindCommonCharaters.py



import cProfile

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        d = dict()
        targetL = []
        for index, astr in enumerate(A):
            d[index] = {}
            for letter in astr:
                if letter in A[0]:
                    d[index][letter] = d[index].get(letter, 0) + 1
        
        d2 = {}
        for key in d[0]:
            d2[key] = d[0][key]
            for i in zip(d.values()):
                cnt = i[0].get(key, 0)
                if cnt:
                    if key not in d2:
                        pass
                    if cnt < d2.get(key):
                        # d[0][key] = cnt
                        d2[key] = cnt
                else:
                    if key in d2:
                        d2[key] = 0

        for key,value in d2.items():
            targetL += [key]*value
        return targetL

from collections import Counter  
       
class Solution1(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        return list(reduce(lambda x,y: x&y, [Counter(A[i]) for i in range(len(A))]).elements())

def testCase():
    s = Solution()
    A = ["bella","label","roller"]
    expect = ["e","l","l"] 
    # A = ["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]
    # expect = ["a","c","d","d","d"]
    A = ["cool","lock","cook"]
    expect = ["c","o"]
    print "out", s.commonChars(A)
    print("expect=", expect)

def testCase1():
    s = Solution1()
    test = ["bella","label","roller"]
    expect = ["e","l","l"] 
    print "output = ", s.commonChars(test)
    print("expect=", expect)



def test():
	# testCase()
	testCase1()
	print("test done")


if __name__ == '__main__':
	test()



# 总结
# zip和sorted使用








