#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#
# https://leetcode.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (44.79%)
# Total Accepted:    229.2K
# Total Submissions: 496.4K
# Testcase Example:  '[1,2,3,null,5]'
#
# Given a binary tree, return all root-to-leaf paths.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# 
# Input:
# 
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
# 
# Output: ["1->2->5", "1->3"]
# 
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        res = []
        self.dfs(root, '', res)
        return res

    def dfs(self, root, path, res):
        if not root.left and not root.right:
            res.append(path + str(root.val))
        if root.left:
            self.dfs(root.left, path+str(root.val)+'->', res)
        if root.right:
            self.dfs(root.right, path+str(root.val)+'->', res)
