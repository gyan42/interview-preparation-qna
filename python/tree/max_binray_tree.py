
class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.data)

    def insert(self, data):
        """
        - If value is less then root node, find empty leaf and insert into left
        - If value is greater than root node, find empty leaf and insert into right
        :param data:
        :return:
        """
        if data:
            if data < self.data:
                if self.left is None:
                    print(f"{data} inserted into left side of {self.data}")
                    self.left = TreeNode(data=data)
                else:
                    self.left.insert(data=data)
            else:
                if self.right is None:
                    print(f"{data} inserted into right side of {self.data}")
                    self.right = TreeNode(data=data)
                else:
                    self.right.insert(data=data)


def size(root: TreeNode):
    if root is None:
        return 0
    else:
        return size(root.left) + 1 + size(root.right)


def max_binary_search_tree(root: TreeNode):
    """
    Maximum number in a binary tree.
    Visit right side of the tree.
    """
    maxVal = None
    current = root
    while current:
        maxVal = current.data
        current = current.right
    return maxVal


def max_bt(root: TreeNode):
    if root is None:
        return float('-inf')

    res = root.data
    left_max = max_bt(root.left)
    right_max = max_bt(root.right)

    if left_max > res:
        res = left_max
    if right_max > res:
        res = right_max
    return res

def second_largest_number(root, is_left=False):
    # case 1: no right child
    if root.right is None:
        return second_largest_number(root.left, is_left=True)

    res = None
    curr_max = root.data
    prev_max = -1
    current = root
    while (current):
        current = current.right
        if current:
            prev_max = curr_max
            curr_max = current.data
    if is_left:
        res = curr_max
    else:
        res = prev_max
    return res

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

tree = TreeNode(data=5)
tree.insert(10)

tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(6)
tree.insert(7)
tree.insert(10)

tree.insert(8)
tree.insert(9)
tree.insert(11)
tree.insert(12)


# print(max_bt(tree))

# print(max_binary_search_tree(tree))

print(second_largest_number(tree))

# inorder(tree)