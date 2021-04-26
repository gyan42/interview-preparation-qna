from collections import defaultdict

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.data)


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

print("find_depth_of_tree: ", find_depth_of_tree(tree='nlnnlll', n=len('nlnnlll'), index=0))
print("find_depth_of_tree: ", find_depth_of_tree(tree='nlnll', n=len('nlnll'), index=0))

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


tree = TreeNode(10,
                TreeNode(20,
                         TreeNode(40), TreeNode(50)),
                TreeNode(30))
# Inorder Traversal is : 40 20 50 10 30
print("find_node:")  # 10
find_nth_node(tree, 4)