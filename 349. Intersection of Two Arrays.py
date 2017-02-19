# Given two arrays, write a function to compute their intersection.

# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

# Note:
# Each element in the result must be unique.
# The result can be in any order.

# class Solution(object):
#     def intersection(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """

import cProfile

def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    rtn = list(set(nums1) & set(nums2))
    return rtn


print intersection([1,2,2,1], [2,2])
print intersection([1,2,3,4], [2,2,3])
cProfile.run("intersection([1,2,2,1], [2,2])")