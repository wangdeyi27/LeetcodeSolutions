#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#
# https://leetcode.com/problems/single-number-ii/description/
#
# algorithms
# Medium (44.96%)
# Total Accepted:    164.6K
# Total Submissions: 359.7K
# Testcase Example:  '[2,2,3,2]'
#
# Given a non-empty array of integers, every element appears three times except
# for one, which appears exactly once. Find that single one.
# 
# Note:
# 
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
# 
# Example 1:
# 
# 
# Input: [2,2,3,2]
# Output: 3
# 
# 
# Example 2:
# 
# 
# Input: [0,1,0,1,0,1,99]
# Output: 99
# 
#
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = b = 0
        for num in nums:
            b = (b ^ num) & ~a
            a = (a ^ num) & ~b
        return b
