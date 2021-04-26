
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


# Depth First Search
def inorder(root: TreeNode):
    if root:
        inorder(root.left)
        print(root, end=" ")
        inorder(root.right)

if __name__ == "__main__":
    t = TreeNode(25)

    t.insert(15)
    t.insert(50)

    t.insert(10)
    t.insert(22)
    t.insert(35)
    t.insert(70)

    t.insert(4)
    t.insert(12)
    t.insert(18)
    t.insert(24)
    t.insert(31)
    t.insert(44)
    t.insert(66)
    t.insert(90)

    inorder(t)