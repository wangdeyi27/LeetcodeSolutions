#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (29.64%)
# Total Accepted:    253.7K
# Total Submissions: 808.7K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given a string S and a string T, find the minimum window in S which will
# contain all the characters in T in complexity O(n).
# 
# Example:
# 
# 
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# 
# 
# Note:
# 
# 
# If there is no such window in S that covers all characters in T, return the
# empty string "".
# If there is such window, you are guaranteed that there will always be only
# one unique minimum window in S.
# 
# 
#
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = {}
        ct = len(t)
        for c in t:
            if c in d: d[c]+=1
            else: d[c]=1
                
        counter = 0
        left = 0
        min_len = len(s) + 1
        res=""
        
        for idx, c in enumerate(s):
            if c in d:
                d[c]-=1
                if d[c]>=0:
                    counter+=1
                while counter==ct:
                    if s[left] in d:
                        if min_len>(idx-left+1):
                            min_len=idx-left+1
                            res = s[left:idx+1]                        
                        d[s[left]]+=1
                        if d[s[left]]>0:
                            counter-=1
                    left+=1
        return res        
