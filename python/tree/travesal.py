from collections import defaultdict

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
                    # print(f"{data} inserted into left side of {self.data}")
                    self.left = TreeNode(data=data)
                else:
                    self.left.insert(data=data)
            else:
                if self.right is None:
                    # print(f"{data} inserted into right side of {self.data}")
                    self.right = TreeNode(data=data)
                else:
                    self.right.insert(data=data)

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

# -----------------------------------------------------------------------------------------------------------------------
"""
The most important points is, BFS starts visiting nodes from root while DFS starts visiting nodes from leaves. 
So if our problem is to search something that is more likely to closer to root, we would prefer BFS. 
And if the target node is close to a leaf, we would prefer DFS. 
"""
# Breadth First Search a.k.a Inorder
# https://www.geeksforgeeks.org/level-order-tree-traversal/
def bfs_recursive(root: TreeNode, visited=defaultdict(lambda: False)):
    if root:
        if root.data not in visited:
            print(root, end=" ")
        if root.left and not visited[root.left.data]:
            print(root.left, end=" ")
            visited[root.left.data] = True
        if root.right and not visited[root.right.data]:
            print(root.right, end=" ")
            visited[root.right.data] = True

        bfs_recursive(root.left, visited=visited)
        bfs_recursive(root.right, visited=visited)

print("bfs_recursive")
bfs_recursive(t)
print()

def bfs_queue(root: TreeNode):
    queue = [] # FIFO
    # current = None
    queue.append(root)
    while len(queue) > 0:
        current_node = queue.pop(0)
        print(current_node, end=" ")
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

print("bfs_queue")
bfs_queue(t)
print()
# -----------------------------------------------------------------------------------------------------------------------

# Depth First Search
def inorder(root: TreeNode):
    if root:
        inorder(root.left)
        print(root, end=" ")
        inorder(root.right)


def inorder_stack(root):
    stack = []
    current = root

    while True:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            print(current.data, end=" ")
            current = current.right
        else:
            break

print("inorder")
inorder(t)
print("\ninorder_stack")
inorder_stack(t)

# -----------------------------------------------------------------------------------------------------------------------

def preorder(root: TreeNode):
    if root:
        print(root, end=" ")
        preorder(root.left)
        preorder(root.right)

def iterative_preorder(root: TreeNode):
    stack = []
    stack.append(root)

    while(len(stack) > 0):
        current = stack.pop()
        print(current.data, end=" ")
        if current.right:
            stack.append(current.right) # Note right first!
        if current.left:
            stack.append(current.left)

def postorder(root: TreeNode):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root, end=" ")

print("\npreorder")
preorder(t)
print("\niterative_preorder")
iterative_preorder(t)

print("\npostorder"); postorder(t)