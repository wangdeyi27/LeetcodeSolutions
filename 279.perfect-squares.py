#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares/description/
#
# algorithms
# Medium (40.43%)
# Total Accepted:    187.3K
# Total Submissions: 444K
# Testcase Example:  '12'
#
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
# 
# Example 1:
# 
# 
# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.
# 
# Example 2:
# 
# 
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
#
class Solution:
    numSquaresDP = [0]
    def numSquares(self, n):
        if len(self.numSquaresDP) <= n:
            perfectSqr = [v**2 for v in range(1, int(math.sqrt(n)) + 1)]
            for i in range(len(self.numSquaresDP), n + 1):
                self.numSquaresDP.append( min(1 + self.numSquaresDP[i - sqr] for sqr in perfectSqr if sqr <= i))
        return self.numSquaresDP[n]
