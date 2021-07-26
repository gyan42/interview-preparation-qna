# Simple Python3 program to find n'th node from end
# TODO https://leetcode.com/problems/remove-nth-node-from-end-of-list/solution/

"""
public ListNode removeNthFromEnd(ListNode head, int n) {
    ListNode dummy = new ListNode(0);
    dummy.next = head;
    ListNode first = dummy;
    ListNode second = dummy;
    // Advances first pointer so that the gap between first and second is n nodes apart
    for (int i = 1; i <= n + 1; i++) {
        first = first.next;
    }
    // Move first to the end, maintaining the gap
    while (first != null) {
        first = first.next;
        second = second.next;
    }
    second.next = second.next.next;
    return dummy.next;
}

"""
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # createNode and and make linked list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Function to get the nth node from
    # the last of a linked list
    def printNthFromLast(self, n):
        temp = self.head  # used temp variable

        length = 0
        while temp is not None:
            temp = temp.next
            length += 1

        # print count
        if n > length:  # if entered location is greater
            # than length of linked list
            print('Location is greater than the' +
                  ' length of LinkedList')
            return
        temp = self.head
        for i in range(0, length - n):
            temp = temp.next
        print(temp.data)


# Driver Code
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(35)
llist.printNthFromLast(3)