# !/usr/bin/env python
#! -*- coding:utf-8 -*-
# Author:   wolfanature
# filename: 657.JudgeRouteCircle.py


# Initially, there is a Robot at position (0, 0).
# Given a sequence of its moves, judge if this robot makes a circle, 
# which means it moves back to the original place.

# The move sequence is represented by a string. And each move is represent by a character.
# The valid robot moves are R (Right), L (Left), U (Up) and D (down).
 # The output should be true or false representing whether the robot makes a circle.

# Example 1:
# Input: "UD"
# Output: true
# Example 2:
# Input: "LL"
# Output: false




class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        blnHorizon = moves.count("L")*1 + moves.count("R")*(-1)
        blnVertical = moves.count("U")*1 + moves.count("D")*(-1)
        if blnHorizon == 0 and blnVertical == 0:
        	return True
        return False

    def judgeCircleV2(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count("L") == moves.count("R") and moves.count("U") == moves.count("D")



if __name__ == '__main__':
	solution = Solution()
	testList = ["UD", "UDL", "UDLR", "UUULLRRRDDD"]
	for moves in testList:
		print solution.judgeCircle(moves)













