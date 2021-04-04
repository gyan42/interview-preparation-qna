# Given head, the head of a linked list, determine if the linked list has a cycle in it.

from collections import defaultdict

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ret = False
        visited = defaultdict(lambda: False)
        node = head
        while(node):
            if not visited[node]:
                visited[node] = True
            else:
                ret = True
                break
            node = node.next
        return ret

# head = [3,2,0,-4], pos = 1
ll = ListNode(x=3)
ll.next = ListNode(x=2)
ll.next.next = ListNode(x=0)
ll.next.next.next = ListNode(x=-4)
ll.next.next.next.next = ll.next

print(Solution().hasCycle(ll))
#  head = [3,2,0,-4], pos = -1
ll = ListNode(x=3)
ll.next = ListNode(x=2)
ll.next.next = ListNode(x=0)
ll.next.next.next = ListNode(x=-4)
print(Solution().hasCycle(ll))

print("-----------------------------------------------------------------------------------------------------------------------")

class Solution1(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ret = False
        slow = head
        fast = head
        while(slow and fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                ret = True
                break
        return ret

# head = [3,2,0,-4], pos = 1
ll = ListNode(x=3)
ll.next = ListNode(x=2)
ll.next.next = ListNode(x=0)
ll.next.next.next = ListNode(x=-4)
ll.next.next.next.next = ll.next
print(Solution1().hasCycle(ll))

#  head = [3,2,0,-4], pos = -1
ll = ListNode(x=3)
ll.next = ListNode(x=2)
ll.next.next = ListNode(x=0)
ll.next.next.next = ListNode(x=-4)
print(Solution1().hasCycle(ll))