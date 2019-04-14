#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (45.64%)
# Total Accepted:    194.2K
# Total Submissions: 414.5K
# Testcase Example:  '4\n2'
#
# Given two integers n and k, return all possible combinations of k numbers out
# of 1 ... n.
# 
# Example:
# 
# 
# Input: n = 4, k = 2
# Output:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
# 
#
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = [[]]
        for _ in range(k):
            res = [[i] + c for c in res for i in range(1, c[0] if c else n+1)]
        return res
