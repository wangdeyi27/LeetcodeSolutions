#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/
#
# algorithms
# Hard (38.87%)
# Total Accepted:    138.9K
# Total Submissions: 350.3K
# Testcase Example:  '[1,3,5]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# 
# Find the minimum element.
# 
# The array may contain duplicates.
# 
# Example 1:
# 
# 
# Input: [1,3,5]
# Output: 1
# 
# Example 2:
# 
# 
# Input: [2,2,2,0,1]
# Output: 0
# 
# Note:
# 
# 
# This is a follow up problem to Find Minimum in Rotated Sorted Array.
# Would allow duplicates affect the run-time complexity? How and why?
# 
# 
#
class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, mid, end = 0, 0, len(nums) - 1
        while(start < end and nums[start] == nums[end]):
            start += 1
            
        if nums[end] > nums[start]: return nums[start]
        
        while(start + 1 < end):
            mid = (start + end) // 2
            if (nums[mid] >= nums[start]):
                start = mid
            else: 
                end = mid

        return min(nums[start], nums[end])       
