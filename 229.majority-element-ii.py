#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#
# https://leetcode.com/problems/majority-element-ii/description/
#
# algorithms
# Medium (31.13%)
# Total Accepted:    101.8K
# Total Submissions: 316.5K
# Testcase Example:  '[3,2,3]'
#
# Given an integer array of size n, find all elements that appear more than ⌊
# n/3 ⌋ times.
# 
# Note: The algorithm should run in linear time and in O(1) space.
# 
# Example 1:
# 
# 
# Input: [3,2,3]
# Output: [3]
# 
# Example 2:
# 
# 
# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]
# 
#
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums: return []
        cnt1, cnt2, c1, c2 = 0, 0, 0, 1
        for n in nums:
            if n == c1: cnt1 += 1
            elif n == c2: cnt2 += 1
            elif cnt1 == 0: c1, cnt1 = n, 1
            elif cnt2 == 0: c2, cnt2 = n, 1
            else: cnt1, cnt2 = cnt1-1, cnt2-1
        return [n for n in (c1,c2) if nums.count(n) > len(nums) // 3]
