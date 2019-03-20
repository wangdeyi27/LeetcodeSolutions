#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (23.17%)
# Total Accepted:    500.4K
# Total Submissions: 2.1M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
# 
# Note:
# 
# The solution set must not contain duplicate triplets.
# 
# Example:
# 
# 
# Given array nums = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []
        
        res = set()
        nums.sort()
            
        for i, v in enumerate(nums[:-2]):
            if i > 0 and v == nums[i-1]:
                continue
            
            l = i+1
            r = n-1
            target = -v
            
            while l < r:
                if nums[l] + nums[r] == target:
                    res.add((v, nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
        
        return list(map(list, res))
