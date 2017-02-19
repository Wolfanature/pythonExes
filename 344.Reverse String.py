


# Write a function that takes a string as input and returns the string reversed.

# Example:
# Given s = "hello", return "olleh".


# class Solution(object):
#     def reverseString(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """

# fanc
def reverseString(s):
    """
    :type s: str
    :rtype: str
    """
    s = s[::-1]
    return s

# Test
a = "hello"
print reverseString("hello")
print reverseString("wolf")
print reverseString("wolf an")


a = "hello"
b = "ollhef"
 