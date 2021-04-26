
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