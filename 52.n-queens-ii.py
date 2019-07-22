#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#
# https://leetcode.com/problems/n-queens-ii/description/
#
# algorithms
# Hard (50.41%)
# Total Accepted:    103.6K
# Total Submissions: 196.4K
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard
# such that no two queens attack each other.
# 
# 
# 
# Given an integer n, return the number of distinct solutions to the n-queens
# puzzle.
# 
# Example:
# 
# 
# Input: 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown
# below.
# [
# [".Q..",  // Solution 1
# "...Q",
# "Q...",
# "..Q."],
# 
# ["..Q.",  // Solution 2
# "Q...",
# "...Q",
# ".Q.."]
# ]
# 
# 
#
class Solution:
    res = 0
    def totalNQueens(self, n: int) -> int:
        def dfs(queens, ddiff, ssum):
            p = len(queens)
            if p == n:
                self.res += 1
                return
            for q in range(n):
                if q in queens or (p - q) in ddiff or (p + q) in ssum: continue
                dfs(queens + [q], ddiff + [p - q], ssum + [p + q])
        dfs([], [], [])
        return self.res
