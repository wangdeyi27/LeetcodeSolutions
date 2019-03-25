#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (52.78%)
# Total Accepted:    310.5K
# Total Submissions: 579.4K
# Testcase Example:  '3'
#
# 
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# 
# For example, given n = 3, a solution set is:
# 
# 
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
# 
#
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        s = [("(", 1, 0)]
        while s:
            tmp, l, r = s.pop()
            if r > l or l > n or r > n:
                continue
            if l == n and r == n:
                res.append(tmp)
            s.append((tmp+"(", l+1, r))
            s.append((tmp+")", l, r+1))
        return res
