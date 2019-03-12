#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#
# https://leetcode.com/problems/power-of-two/description/
#
# algorithms
# Easy (41.56%)
# Total Accepted:    214.9K
# Total Submissions: 515.7K
# Testcase Example:  '1'
#
# Given an integer, write a function to determine if it is a power of two.
# 
# Example 1:
# 
# 
# Input: 1
# Output: true 
# Explanation: 20 = 1
# 
# 
# Example 2:
# 
# 
# Input: 16
# Output: true
# Explanation: 24 = 16
# 
# Example 3:
# 
# 
# Input: 218
# Output: false
# 
#
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
