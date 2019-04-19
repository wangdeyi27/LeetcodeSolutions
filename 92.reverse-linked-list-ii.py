#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (33.84%)
# Total Accepted:    187.6K
# Total Submissions: 542.8K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# Reverse a linked list from position m to n. Do it in one-pass.
# 
# Note: 1 ≤ m ≤ n ≤ length of list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        res = ListNode(0)
        res.next = head
        node = res

        for i in range(m-1):
            node = node.next

        cur = node.next
        pre = None
        for i in range(n-m+1):
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next

        node.next.next = cur
        node.next = pre
        return res.next
