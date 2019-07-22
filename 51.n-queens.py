#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#
# https://leetcode.com/problems/n-queens/description/
#
# algorithms
# Hard (37.36%)
# Total Accepted:    148.6K
# Total Submissions: 369.6K
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard
# such that no two queens attack each other.
# 
# 
# 
# Given an integer n, return all distinct solutions to the n-queens puzzle.
# 
# Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.' both indicate a queen and an empty space
# respectively.
# 
# Example:
# 
# 
# Input: 4
# Output: [
# ⁠[".Q..",  // Solution 1
# ⁠ "...Q",
# ⁠ "Q...",
# ⁠ "..Q."],
# 
# ⁠["..Q.",  // Solution 2
# ⁠ "Q...",
# ⁠ "...Q",
# ⁠ ".Q.."]
# ]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as
# shown above.
# 
# 
#
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        def dfs(queens, ddiff, ssum):
            p = len(queens)
            if p == n:
                queens = ['.' * i + 'Q' + '.' * (n - 1 - i) for i in queens]
                res.append(queens)
                return
            for q in range(n):
                if q in queens or p - q in ddiff or p + q in ssum: continue
                dfs(queens + [q], ddiff + [p - q], ssum + [p + q])
        dfs([], [], [])
        return res
