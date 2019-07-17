#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#
# https://leetcode.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (28.07%)
# Total Accepted:    224.1K
# Total Submissions: 766.7K
# Testcase Example:  '[1,2,0]'
#
# Given an unsorted integer array, find the smallest missing positive integer.
# 
# Example 1:
# 
# 
# Input: [1,2,0]
# Output: 3
# 
# 
# Example 2:
# 
# 
# Input: [3,4,-1,1]
# Output: 2
# 
# 
# Example 3:
# 
# 
# Input: [7,8,9,11,12]
# Output: 1
# 
# 
# Note:
# 
# Your algorithm should run in O(n) time and uses constant extra space.
# 
#
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums: return 1
        for num in nums:
            while 0 <= num - 1 < len(nums) and nums[num-1] != num:
                tmp = num - 1
                num, nums[tmp] = nums[tmp], num
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums) + 1
