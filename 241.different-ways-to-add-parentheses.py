#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#
# https://leetcode.com/problems/different-ways-to-add-parentheses/description/
#
# algorithms
# Medium (48.68%)
# Total Accepted:    74.1K
# Total Submissions: 148.1K
# Testcase Example:  '"2-1-1"'
#
# Given a string of numbers and operators, return all possible results from
# computing all the different possible ways to group numbers and operators. The
# valid operators are +, - and *.
# 
# Example 1:
# 
# 
# Input: "2-1-1"
# Output: [0, 2]
# Explanation: 
# ((2-1)-1) = 0 
# (2-(1-1)) = 2
# 
# Example 2:
# 
# 
# Input: "2*3-4*5"
# Output: [-34, -14, -10, -10, 10]
# Explanation: 
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10
# 
#
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit(): return [int(input)]
        res = []
        for i, s in enumerate(input):
            if s in "+-*":
                l = self.diffWaysToCompute(input[:i])
                r = self.diffWaysToCompute(input[i+1:])
                res.extend(self.compute(l, r, s))
        return res

    def compute(self, l, r, op):
        return [eval(str(m)+op+str(n)) for m in l for n in r]
