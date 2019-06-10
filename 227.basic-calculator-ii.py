#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#
# https://leetcode.com/problems/basic-calculator-ii/description/
#
# algorithms
# Medium (32.47%)
# Total Accepted:    110.6K
# Total Submissions: 329.9K
# Testcase Example:  '"3+2*2"'
#
# Implement a basic calculator to evaluate a simple expression string.
# 
# The expression string contains only non-negative integers, +, -, *, /
# operators and empty spaces  . The integer division should truncate toward
# zero.
# 
# Example 1:
# 
# 
# Input: "3+2*2"
# Output: 7
# 
# 
# Example 2:
# 
# 
# Input: " 3/2 "
# Output: 1
# 
# Example 3:
# 
# 
# Input: " 3+5 / 2 "
# Output: 5
# 
# 
# Note:
# 
# 
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.
# 
# 
#
class Solution:
    def calculate(self, s: str) -> int:
        s += '+0'
        stack, num, pre = [], 0, '+'
        for i in range(len(s)):
            if s[i].isdigit(): num = num * 10 + int(s[i])
            elif not s[i].isspace():
                if pre == '+': stack.append(num)
                elif pre == '-': stack.append(-num)
                elif pre == '*': stack.append(stack.pop() * num)
                else:            stack.append(int(stack.pop() / num))
                pre, num = s[i], 0
        return sum(stack)
