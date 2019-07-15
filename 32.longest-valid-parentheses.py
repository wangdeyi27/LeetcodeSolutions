#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
# https://leetcode.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (24.79%)
# Total Accepted:    199.2K
# Total Submissions: 772.3K
# Testcase Example:  '"(()"'
#
# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.
# 
# Example 1:
# 
# 
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# 
# 
# Example 2:
# 
# 
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"
# 
# 
#
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right, res = 0, 0, 0
        for word in s:
            if word == '(': left += 1
            else: right += 1
            if left == right:
                res = max(res, right * 2)
            if left < right:
                left, right = 0, 0

        left, right = 0, 0
        for word in s[::-1]:
            if word == '(': left += 1
            else: right += 1
            if left == right:
                res = max(res, left * 2)
            if left > right:
                left, right = 0, 0
        return res
