#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (32.85%)
# Total Accepted:    277.8K
# Total Submissions: 838.2K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in ascending order, find the starting
# and ending position of a given target value.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# If the target is not found in the array, return [-1, -1].
# 
# Example 1:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# 
# Example 2:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# 
#
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        low, high, res = 0, len(nums) - 1, [-1, -1]
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                low_left, high_left = low, mid
                low_right, high_right = mid, high
                while low_left <= high_left:
                    mid_left = (low_left + high_left) // 2
                    if nums[mid_left] > target - 0.5:
                        high_left = mid_left - 1
                    else:
                        low_left = mid_left + 1
                res[0] = low_left
                while low_right <= high_right:
                    mid_right = (low_right + high_right) // 2
                    if nums[mid_right] < target + 0.5:
                        low_right = mid_right + 1
                    else:
                        high_right = mid_right - 1
                res[1] = high_right
                break
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return res
