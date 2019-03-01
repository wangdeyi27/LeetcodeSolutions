#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#
# https://leetcode.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (41.70%)
# Total Accepted:    184.9K
# Total Submissions: 440.3K
# Testcase Example:  '3'
#
# Given a non-negative index k where k ≤ 33, return the kth index row of the
# Pascal's triangle.
# 
# Note that the row index starts from 0.
# 
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
# 
# Example:
# 
# 
# Input: 3
# Output: [1,3,3,1]
# 
# 
# Follow up:
# 
# Could you optimize your algorithm to use only O(k) extra space?
# 
#
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        for i in range(1, rowIndex+2):
            result.append(1)
            for j in range(i-2, 0, -1):
                result[j] += result[j-1]
        return result
