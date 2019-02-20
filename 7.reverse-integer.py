#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.07%)
# Total Accepted:    602.9K
# Total Submissions: 2.4M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# 
# Input: 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: 120
# Output: 21
# 
# 
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of
# this problem, assume that your function returns 0 when the reversed integer
# overflows.
# 
#
class Solution:
    def reverse(self, x: 'int') -> 'int':
        res = 0
        flag = False
        if x < 0:
            flag = True
            x = -x
        while x > 0:
            res = res * 10 + x % 10
            x = x // 10
        if flag:
            res = -res
        if res > 2**31-1 or res < -2**31:
            return 0
        return res
