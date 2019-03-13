#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (35.17%)
# Total Accepted:    235.4K
# Total Submissions: 665K
# Testcase Example:  '[1,2]'
#
# Given a singly linked list, determine if it is a palindrome.
# 
# Example 1:
# 
# 
# Input: 1->2
# Output: false
# 
# Example 2:
# 
# 
# Input: 1->2->2->1
# Output: true
# 
# Follow up:
# Could you do it in O(n) time and O(1) space?
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev
