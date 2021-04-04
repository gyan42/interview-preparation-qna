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

def find_depth_of_tree(tree, n, index):
    """
    find height of full binary tree using preorder
                    n
                 /     \
                l       n
                      /   \
                    n       l
                 /     \
                l       l



    :param str:
    :return:
    """
    if tree[index] == 'l' or index >= n:
        return 0

    index += 1
    left = find_depth_of_tree(tree, n, index)

    index += 1
    right = find_depth_of_tree(tree, n, index)

    res = max(left, right) + 1
    return res

count = [0]
def find_nth_node(tree: TreeNode, n):
    "Find n-th node of inorder traversal"
    if tree is None:
        return

    if count[0] < n:
        find_nth_node(tree.left, n)
        count[0] = count[0] + 1
        if count[0] == n:
            print(f"{count} position --> {tree}")
        find_nth_node(tree.right, n)


#-----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    # t = TreeNode(25)
    #
    # t.insert(15)
    # t.insert(50)
    #
    # t.insert(10)
    # t.insert(22)
    # t.insert(35)
    # t.insert(70)
    #
    # t.insert(4)
    # t.insert(12)
    # t.insert(18)
    # t.insert(24)
    # t.insert(31)
    # t.insert(44)
    # t.insert(66)
    # t.insert(90)
    #
    # print("\nsize")
    # print(size(t))
    #
    # print("\nmax")
    # print(max_binary_search_tree(t))
    #
    # print("\nmax_bt")
    # print(max_bt(t))
    #
    # print("\nbfs")
    # print(bfs_recursive(t))
    #
    # print("\nbfs_queue")
    # bfs_queue(t)

    print("find_depth_of_tree: ", find_depth_of_tree(tree='nlnnlll', n=len('nlnnlll'), index=0))
    print("find_depth_of_tree: ", find_depth_of_tree(tree='nlnll', n=len('nlnll'), index=0))


    #------------------------------------
    tree = TreeNode(10,
                    TreeNode(20,
                             TreeNode(40), TreeNode(50)),
                    TreeNode(30))
    # Inorder Traversal is : 40 20 50 10 30
    print("find_node:")  # 10
    find_nth_node(tree, 4)