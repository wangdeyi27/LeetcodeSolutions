#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (50.65%)
# Total Accepted:    308.2K
# Total Submissions: 602.8K
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t , write a function to determine if t is an anagram
# of s.
# 
# Example 1:
# 
# 
# Input: s = "anagram", t = "nagaram"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "rat", t = "car"
# Output: false
# 
# 
# Note:
# You may assume the string contains only lowercase alphabets.
# 
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your
# solution to such case?
# 
#
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict = {}
        for c in s:
            if c in dict:
                dict[c] += 1
            else:
                dict[c] = 1

        for c in t:
            if c in dict:
                dict[c] -= 1
            if c not in dict or dict[c] < 0:
                return False
        return True
