#
# @lc app=leetcode id=5 lang=python
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (26.36%)
# Total Accepted:    496.6K
# Total Submissions: 1.9M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
#
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        t = "#" + "#".join(s) + "#"
        p = [0] * len(t)
        mx = id = 0

        for i in range(len(t)):
            p[i] = min(p[2 * id - i], mx - i) if i < mx else 1
            while i - p[i] >= 0 and i + p[i] < len(t) and t[i - p[i]] == t[i + p[i]]:
                p[i] += 1
            if i + p[i] > mx:
                mx = i + p[i]
                id = i
        maxValue = max(p)
        maxIndex = p.index(max(p))

        return t[maxIndex - maxValue + 1 : maxIndex + maxValue].replace('#','')
