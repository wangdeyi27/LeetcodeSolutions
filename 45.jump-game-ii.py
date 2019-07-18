#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
# https://leetcode.com/problems/jump-game-ii/description/
#
# algorithms
# Hard (27.24%)
# Total Accepted:    178.4K
# Total Submissions: 628.5K
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
# 
# Each element in the array represents your maximum jump length at that
# position.
# 
# Your goal is to reach the last index in the minimum number of jumps.
# 
# Example:
# 
# 
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
# ⁠   Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# Note:
# 
# You can assume that you can always reach the last index.
# 
#
class Solution:
    def jump(self, nums: List[int]) -> int:
        max_reach, next_max_reach, min_jumps, len_nums = 0, 0, 0, len(nums) - 1
        for i, num in enumerate(nums):
            if max_reach >= len_nums: return min_jumps
            next_max_reach = max(next_max_reach, i+num)
            if i == max_reach: min_jumps, max_reach = min_jumps + 1, next_max_reach
