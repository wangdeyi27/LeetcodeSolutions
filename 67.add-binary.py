#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (37.67%)
# Total Accepted:    274.6K
# Total Submissions: 725.4K
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings, return their sum (also a binary string).
# 
# The input strings are both non-empty and contains only characters 1 or 0.
# 
# Example 1:
# 
# 
# Input: a = "11", b = "1"
# Output: "100"
# 
# Example 2:
# 
# 
# Input: a = "1010", b = "1011"
# Output: "10101"
# 
#
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1, num2, sum = 0, 0, 0
        for num in a:
            num1 = num1 * 2 + int(num)
        for num in b:
            num2 = num2 * 2 + int(num)

        sum = num1 + num2
        if sum==0:
            return '0'
        res = ''
        while sum > 0:
            res = str(sum % 2) + res
            sum //= 2
        return res
