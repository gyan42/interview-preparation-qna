"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s),
which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder(node: Node):
    if node:
        print(node.val, end=',')
        preorder(node.left)
        preorder(node.right)

def serialize(root: Node, string=''):
    if root:
        if len(string) > 0:
            string = string + "," + root.val
        else:
            string = root.val
        string = serialize(root.left, string)
        string = serialize(root.right, string)
    return string

def deserialize(string):
    def _deser(str_list):
        if len(str_list) > 0:
            curr_str = str_list[0]
        else:
            return
        parent = Node(val=curr_str)
        parent.left = _deser(str_list[1:])
        parent.right = _deser(str_list[1:])
        return parent
    return _deser(string.split(','))


"""
                root
            left    right
    left.left

"""
node = Node('root', Node('left', Node('left.left')), Node('right'))
preorder(node)
print()
print(serialize(node))
print(deserialize(serialize(node)).left.left.val)
assert deserialize(serialize(node)).left.left.val == 'left.left'