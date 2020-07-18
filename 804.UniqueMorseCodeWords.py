# !/usr/bin/env python
#! -*- coding:utf-8 -*-
# Author:   wolfanature
# filename: 804.UniqueMorseCodeWords.py


# International Morse Code defines a standard encoding where 
# each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

# For convenience, the full table for the 26 letters of 
# the English alphabet is given below:

# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# Now, given a list of words, each word can 
# be written as a concatenation of the Morse code of each letter.
 # For example, "cab" can be written as "-.-.-....-",
  # (which is the concatenation "-.-." + "-..." + ".-"). 
  # We'll call such a concatenation, the transformation of a word.

# Return the number of different transformations among all words we have.

# Example:
# Input: words = ["gin", "zen", "gig", "msg"]
# Output: 2
# Explanation: 
# The transformation of each word is:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."

# There are 2 different transformations, "--...-." and "--...--.".
 

# Note:

# The length of words will be at most 100.
# Each words[i] will have length in range [1, 12].
# words[i] will only consist of lowercase letters.
# Trans = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]


class Solution(object):
	Trans = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
	Letters = "abcdefghijklmnopqrstuvwxyz"
	Dict = {}

	def __init__(self):
		for index, letter in enumerate(self.Letters):
			self.Dict[letter] = self.Trans[index]

	def letter2signal(self, letter):
		return self.Dict[letter]

	# my version 
	def uniqueMorseRepresentations(self, words):
		"""
		:type words: List[str]
		:rtype: int
		"""
		b = ["".join([self.letter2signal(letter) for letter in word]) for word in words]
		return len(set(b))


class Solution2(object):
	# other's version, 厉害了
	def uniqueMorseRepresentations(self, words):
		"""
		:type words: List[str]
		:rtype: int
		"""
		MORSE = [".-","-...","-.-.","-..",".","..-.","--.",
		"....","..",".---","-.-",".-..","--","-.","---",
		".--.","--.-",".-.","...","-","..-","...-",
		".--","-..-","-.--","--.."]
		b = ["".join([MORSE[ord(letter) - ord('a')] for letter in word]) for word in words]
		return len(set(b))


def testCase():
	S = Solution()
	TestList= ["gin", "zen", "gig", "msg"]
	result = S.uniqueMorseRepresentations(TestList)
	print("result = {S}".format(S=result))

	S2 = Solution2()
	result2 = S2.uniqueMorseRepresentations(TestList)
	print("result2 = {S}".format(S=result))



	print("test done")

if __name__ == '__main__':
	testCase()


# 总结
# 考察的知识点 1:列表推导式 2.set中无相同元素 3.ord的使用














