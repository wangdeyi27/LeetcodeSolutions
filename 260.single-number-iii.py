#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#
# https://leetcode.com/problems/single-number-iii/description/
#
# algorithms
# Medium (55.92%)
# Total Accepted:    108.1K
# Total Submissions: 189K
# Testcase Example:  '[1,2,1,3,2,5]'
#
# Given an array of numbers nums, in which exactly two elements appear only
# once and all the other elements appear exactly twice. Find the two elements
# that appear only once.
# 
# Example:
# 
# 
# Input:  [1,2,1,3,2,5]
# Output: [3,5]
# 
# Note:
# 
# 
# The order of the result is not important. So in the above example, [5, 3] is
# also correct.
# Your algorithm should run in linear runtime complexity. Could you implement
# it using only constant space complexity?
# 
#
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dict, res = {}, []
        for num in nums:
            dict[num] = dict.get(num, 0) + 1
        for k, v in dict.items():
            if v == 1: res.append(k)
        return res
