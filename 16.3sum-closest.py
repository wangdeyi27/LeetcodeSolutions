#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (33.90%)
# Total Accepted:    298.6K
# Total Submissions: 716.5K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.
# 
# Example:
# 
# 
# Given array nums = [-1, 2, 1, -4], and target = 1.
# 
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
# 
#
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float("inf")
        nums.sort()
        for i, v in enumerate(nums[:-2]):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                tmp = v + nums[l] + nums[r]
                if tmp == target:
                    return target
                else:
                    res = tmp if abs(tmp - target) < abs(res - target) else res
                    if tmp < target:
                        l += 1
                    else:
                        r -= 1
        return int(res)
