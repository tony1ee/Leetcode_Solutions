#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result=ListNode()
        current=result
        l1current=l1
        l2current=l2
        node=-1
        while l1current!=None and l2current!=None:
            current.next=ListNode()
            current=current.next
            if l1current.val<l2current.val:
                current.val=l1current.val
                l1current=l1current.next
            else:
                current.val=l2current.val
                l2current=l2current.next
        if l1current!=None or l2current!=None:
            node=l1current if l1current!=None else l2current
            while node!=None:
                current.next=ListNode()
                current=current.next
                current.val=node.val
                node=node.next
        return result.next
# @lc code=end



