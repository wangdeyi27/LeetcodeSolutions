#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#
# https://leetcode.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (34.11%)
# Total Accepted:    176.8K
# Total Submissions: 507.2K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# Given an array of n positive integers and a positive integer s, find the
# minimal length of a contiguous subarray of which the sum ≥ s. If there isn't
# one, return 0 instead.
# 
# Example: 
# 
# 
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem
# constraint.
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution of
# which the time complexity is O(n log n). 
# 
#
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        sm = sum(nums)
        if sm < s:
            return 0
        l = len(nums)
        for i in range(l):
            nums[i], sm = sm, sm - nums[i]
        res = l
        nums.append(0)
        for i in range(l-1, -1, -1):
            end = min(l, i + res - 1)
            while nums[i] - nums[end] >= s:
                if res > end - i:
                    res = end - i
                begin = (i + end) // 2
                while nums[i] - nums[begin] < s and begin < end - 1:
                    begin = (begin + end) // 2
                if begin == end: break
                end = begin
        return res
