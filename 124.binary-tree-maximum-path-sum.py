#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (29.14%)
# Total Accepted:    208.6K
# Total Submissions: 683.6K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty binary tree, find the maximum path sum.
# 
# For this problem, a path is defined as any sequence of nodes from some
# starting node to any node in the tree along the parent-child connections. The
# path must contain at least one node and does not need to go through the
# root.
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# 
# ⁠      1
# ⁠     / \
# ⁠    2   3
# 
# Output: 6
# 
# 
# Example 2:
# 
# 
# Input: [-10,9,20,null,null,15,7]
# 
# -10
# / \
# 9  20
# /  \
# 15   7
# 
# Output: 42
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        MAX = {}
        def recurse(root, MAX):
            if not root: return 0
            
            left = recurse(root.left, MAX)
            right = recurse(root.right, MAX)
            
            if left < 0: left = 0
            if right < 0: right = 0
            if left+right+root.val > MAX['max']:
                MAX['max'] = left+right+root.val
                
            return root.val + max(left, right)
            
        MAX['max'] = float('-inf')
        recurse(root, MAX)
        return MAX['max']        
