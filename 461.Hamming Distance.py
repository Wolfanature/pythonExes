
# The Hamming distance between two integers is the number
# of positions at which the corresponding bits are different.
# Given two integers x and y, calculate the Hamming distance.

# Note:
# 0 <= x, y < 231.

# example:

# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        |   |
# The above arrows point to positions where the
# corresponding bits are different.

# class Solution(object):
#     def hammingDistance(self, x, y):
#         """
#         :type x: int
#         :type y: int
#         :rtype: int
#         """
    

def hammingDistance(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    temp = x ^ y
    distance = 0
    while temp:
    	distance += 1
    	temp = temp & (temp - 1)

    return distance


# Self-Test-Case
result = hammingDistance(1,4)
print 'result is',result