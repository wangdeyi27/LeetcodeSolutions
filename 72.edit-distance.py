#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#
# https://leetcode.com/problems/edit-distance/description/
#
# algorithms
# Hard (36.17%)
# Total Accepted:    184.3K
# Total Submissions: 478.2K
# Testcase Example:  '"horse"\n"ros"'
#
# Given two words word1 and word2, find the minimum number of operations
# required to convert word1 to word2.
# 
# You have the following 3 operations permitted on a word:
# 
# 
# Insert a character
# Delete a character
# Replace a character
# 
# 
# Example 1:
# 
# 
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# 
# 
# Example 2:
# 
# 
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
# 
# 
#
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1)+1, len(word2)+1
        dp = [i for i in range(l2)]
        for i in range(1, l1):
            pre, dp[0] = i-1, i
            for j in range(1, l2):
                tmp = dp[j]
                dp[j] = min(dp[j]+1, dp[j-1]+1, pre+(word1[i-1]!=word2[j-1]))
                pre = tmp
        return dp[-1]
