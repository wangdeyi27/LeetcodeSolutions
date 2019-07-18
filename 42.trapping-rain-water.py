#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (41.52%)
# Total Accepted:    312K
# Total Submissions: 712.5K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it is able to trap after raining.
# 
# 
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In
# this case, 6 units of rain water (blue section) are being trapped. Thanks
# Marcos for contributing this image!
# 
# Example:
# 
# 
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# 
#
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3: return 0
        res = 0
        left, right = 0, len(height) - 1
        l_max, r_max = height[left], height[right]
        while left < right:
            l_max, r_max = max(l_max, height[left]), max(r_max, height[right])
            if l_max <= r_max:
                res += l_max - height[left]
                left += 1
            else:
                res += r_max - height[right]
                right -= 1
        return res
