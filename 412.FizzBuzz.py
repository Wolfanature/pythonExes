# !/usr/bin/env python
#! -*- coding:utf-8 -*-
# Author:   wolfanature
# filename: 412_FizzBuzz.py



# Write a program that outputs the string representation of numbers from 1 to n.
# But for multiples of three it should output “Fizz” instead of the number 
# and for the multiples of five output “Buzz”. 
# For numbers which are multiples of both three and five output “FizzBuzz”.

# Example:
# 	n = 15,
# 	Return:
# 	[
# 	    "1",
# 	    "2",
# 	    "Fizz",
# 	    "4",
# 	    "Buzz",
# 	    "Fizz",
# 	    "7",
# 	    "8",
# 	    "Fizz",
# 	    "Buzz",
# 	    "11",
# 	    "Fizz",
# 	    "13",
# 	    "14",
# 	    "FizzBuzz"
# 	]


class Solution(object):

	# my version
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return map(self.trans, [i for i in range(1, n + 1)])

    def trans(self, x):
		if x %3 == 0 and x % 5 == 0:
			return "FizzBuzzaam"
		elif x % 3 == 0:
			return "Fizz"
		elif x % 5 == 0:
			return "Buzzaam"
		return str(x)

	# popular versions 比较牛逼的版本
	# 这个理解起来还是有点困难, 暂时没看懂
	# def fizzBuzz(self, n):
	#     return['FizzBuzz'[i%-3&-4:i%-5&8^12]or`i`for i in range(1,n+1)]

	# def fizzBuzz(self, n):
	#     return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]


if __name__ == '__main__':
	solution = Solution()
	print solution.fizzBuzz(15)













