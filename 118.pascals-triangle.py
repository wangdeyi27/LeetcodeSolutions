#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (44.19%)
# Total Accepted:    227.8K
# Total Submissions: 511.8K
# Testcase Example:  '5'
#
# Given a non-negative integer numRows, generate the first numRows of Pascal's
# triangle.
# 
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
# 
# Example:
# 
# 
# Input: 5
# Output:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
# 
# 
#
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        if numRows > 0:
            res.append([1])
            for i in range(1, numRows):
                tmp = []
                for j in range(i + 1):
                    num1 = res[i-1][j-1] if j-1>=0 else 0
                    num2 = res[i-1][j] if j<len(res[i-1]) else 0
                    tmp.append(num1 + num2)
                res.append(tmp)
        return res
