class Node(object):
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

    def __repr__(self):
        return str(self.data)

def printll(head: Node):
    while(head):
        if head.next:
            print(head.data, end="->")
        else:
            print(head.data)
        head = head.next
    print("\n")

def is_palindrome(head: Node):
    stack = []
    temp = head
    while(temp):
        stack.append(temp.data)
        temp = temp.next
    ret = False
    temp = head
    print(stack)
    while(temp):
        if temp.data == stack.pop():
            ret = True
        else:
            ret = False
            break
        temp = temp.next
    return ret

# [9] [1] [4] [1] [9]
head = Node(data=9,
            next=Node(data=1,
                      next=Node(data=4,
                                next=Node(data=1,
                                          next=Node(data=9)))))
printll(head)
print(is_palindrome(head))