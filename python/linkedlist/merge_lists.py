"""
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: l1 = [], l2 = []
Output: []

Input: l1 = [], l2 = [0]
Output: [0]

Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both l1 and l2 are sorted in non-decreasing order.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        head = tmp = ListNode(None, None)
        while (l1 and l2):
            if l1.val < l2.val:
                tmp.next = ListNode(l1.val, None)
                l1 = l1.next
            else:
                tmp.next = ListNode(l2.val, None)
                l2 = l2.next
            tmp = tmp.next

        if l1 is not None:
            tmp.next = l1
            while (tmp.next is not None):
                tmp = tmp.next
        if l2 is not None:
            tmp.next = l2

        return head.next
