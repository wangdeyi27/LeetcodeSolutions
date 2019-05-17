#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (28.41%)
# Total Accepted:    207.4K
# Total Submissions: 711.7K
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.
# 
# Example 1:
# 
# 
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# 
# 
# Example 2:
# 
# 
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
# 
#
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cMax, cMin, res = nums[0], nums[0], nums[0]
        for num in nums[1:]:
            tmp = cMax
            cMax = max(num, num*cMax, num*cMin)
            cMin = min(num, num*tmp, num*cMin)
            res = max(res, cMax)
        return res
