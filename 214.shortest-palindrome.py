#
# @lc app=leetcode id=214 lang=python3
#
# [214] Shortest Palindrome
#
# https://leetcode.com/problems/shortest-palindrome/description/
#
# algorithms
# Hard (28.02%)
# Total Accepted:    79.4K
# Total Submissions: 282.8K
# Testcase Example:  '"aacecaaa"'
#
# Given a string s, you are allowed to convert it to a palindrome by adding
# characters in front of it. Find and return the shortest palindrome you can
# find by performing this transformation.
# 
# Example 1:
# 
# 
# Input: "aacecaaa"
# Output: "aaacecaaa"
# 
# 
# Example 2:
# 
# 
# Input: "abcd"
# Output: "dcbabcd"
#
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1: return s
        j = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == s[j]:
                j += 1
        
        if j == len(s):
            return s
        
        left = self.shortestPalindrome(s[:j])
        return s[j:][::-1] + left + s[j:]
