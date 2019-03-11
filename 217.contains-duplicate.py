#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#
# https://leetcode.com/problems/contains-duplicate/description/
#
# algorithms
# Easy (50.54%)
# Total Accepted:    305.9K
# Total Submissions: 600.9K
# Testcase Example:  '[1,2,3,1]'
#
# Given an array of integers, find if the array contains any duplicates.
# 
# Your function should return true if any value appears at least twice in the
# array, and it should return false if every element is distinct.
# 
# Example 1:
# 
# 
# Input: [1,2,3,1]
# Output: true
# 
# Example 2:
# 
# 
# Input: [1,2,3,4]
# Output: false
# 
# Example 3:
# 
# 
# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true
# 
#
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        memo = set()
        for num in nums:
            if num in memo:
                return True
            memo.add(num)
        return False
