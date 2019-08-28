#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#
# https://leetcode.com/problems/basic-calculator/description/
#
# algorithms
# Hard (33.59%)
# Total Accepted:    118.9K
# Total Submissions: 352.7K
# Testcase Example:  '"1 + 1"'
#
# Implement a basic calculator to evaluate a simple expression string.
# 
# The expression string may contain open ( and closing parentheses ), the plus
# + or minus sign -, non-negative integers and empty spaces  .
# 
# Example 1:
# 
# 
# Input: "1 + 1"
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: " 2-1 + 2 "
# Output: 3
# 
# Example 3:
# 
# 
# Input: "(1+(4+5+2)-3)+(6+8)"
# Output: 23
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
        res, num, sign, stack = 0, 0, 1, []
        for ss in s:
            if ss.isdigit():
                num = 10*num + int(ss)
            elif ss in ["-", "+"]:
                res += sign*num
                num = 0
                sign = [-1, 1][ss=="+"]
            elif ss == "(":
                stack.append(res)
                stack.append(sign)
                sign, res = 1, 0
            elif ss == ")":
                res += sign*num
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return res + num * sign
