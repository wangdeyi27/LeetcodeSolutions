#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (26.10%)
# Total Accepted:    763.8K
# Total Submissions: 2.9M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# 
# 
# 
# Example 2:
# 
# 
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# 
# Example 3:
# 
# 
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
# 
# 
# 
# 
# 
#
class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        max = cur = 0
        j = 0
        dict = {}
        for i in range(0, len(s)):
            cur += 1
            if s[i] not in dict or dict[s[i]] == 0:
                dict[s[i]] = 1
                max = cur if cur > max else max
            else:
                dict[s[i]] += 1
                while dict[s[i]] > 1:
                    dict[s[j]] -= 1
                    cur -= 1
                    j += 1
        return max
