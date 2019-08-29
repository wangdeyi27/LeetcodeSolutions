#
# @lc app=leetcode id=233 lang=python3
#
# [233] Number of Digit One
#
# https://leetcode.com/problems/number-of-digit-one/description/
#
# algorithms
# Hard (30.53%)
# Total Accepted:    42.8K
# Total Submissions: 139.9K
# Testcase Example:  '13'
#
# Given an integer n, count the total number of digit 1 appearing in all
# non-negative integers less than or equal to n.
# 
# Example:
# 
# 
# Input: 13
# Output: 6 
# Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
# 
# 
#
class Solution:
    def countDigitOne(self, n: int) -> int:
        ones, m = 0, 1
        while m <= n:
            ones += (n // m + 8) // 10 * m + (n // m % 10 == 1) * (n % m + 1)
            m *= 10
        return ones
