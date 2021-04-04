"""
LIFO
The functions associated with stack are:

    empty() – Returns whether the stack is empty – Time Complexity : O(1)
    size() – Returns the size of the stack – Time Complexity : O(1)
    top() – Returns a reference to the top most element of the stack – Time Complexity : O(1)
    push(g) – Adds the element ‘g’ at the top of the stack – Time Complexity : O(1)
    pop() – Deletes the top most element of the stack – Time Complexity : O(1)
"""

stack = []
stack.append(1)
stack.append(2)
stack.append(3)

print('Initial stack:')
print(stack)

print('\nElements poped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are poped:')
print(stack)

# ----------------------------------------------------------------------------------------------------------------------

from collections import deque
stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)

print('Initial stack:')
print(stack)

print('\nElements poped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are poped:')
print(stack)

#-----------------------------------------------------------------------------------------------------------------------

from queue import LifoQueue
stack = LifoQueue(maxsize=3)
stack.put(1)
stack.put(2)
stack.put(3)

print('Initial stack:')
print(stack)
print('Is stack full?')
print(stack.full())

print('\nElements poped from stack:')
print(stack.get())
print(stack.get())
print(stack.get())

print('\nStack after elements are poped:')
print(stack)

#-----------------------------------------------------------------------------------------------------------------------

class Node(object):
    def __init__(self, prev=None, data=None, next=None):
        self.next = next
        self.data = data
        self.prev = prev

    def __repr__(self):
        return str(self.data)

class Stack(object):
    def __init__(self, maxsize=None):
        self._maxsize = maxsize
        self._head = None
        self._size = 0

    def __repr__(self):
        head = self._head
        while (head):
            print(head, end="->")
            head = head.next
        print("\n")
        return ""

    def full(self):
        return self._maxsize == self._size

    def put(self, data):
        if self._size <= self._maxsize:
            node = Node(data=data)
            print(f"Inserting node {node}")
            if self._head:
                node.next = self._head
                self._head = node
            else:
                self._head = node
            self._size += 1
        else:
            raise RuntimeError("Maxsize reached")

    def pop(self):
        # [None]
        if self._head is None:
            raise RuntimeError("No data to pop")
        else:
            node = self._head
            if self._head.next:  # [1] -> [2]
                self._head = self._head.next
            else: # [1]
                self._head = None
            self._size -= 1
            return node.data

stack = Stack(maxsize=3)
stack.put(1)
stack.put(2)
stack.put(3)

print('Initial stack:')
print(stack)
print('Is stack full?')
print(stack.full())

print('\nElements poped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are poped:')
print(stack)