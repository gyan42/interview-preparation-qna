"""
You are given a dictionary representing a tree, for example: { 'A':['B', 'C'], 'C':['D']}
Write a function that converts the dictionary in a string in the following format: X(A(BC(D)))
"""
class Tree(object):
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right =right
        self.data = data

    def __repr__(self):
        return str(self.data)

def treeToString(root: Tree, string: list):

    if root is None:
        return

    # push the root data as character
    string.append(str(root.data))

    if root.left:
    # for left subtree
        string.append('(')
        treeToString(root.left, string)
        string.append(')')

    # only if right child is present to
    # avoid extra parenthesis
    if root.right:
        string.append('(')
        treeToString(root.right, string)
        string.append(')')


tree = Tree(data='A', left=Tree(data='B'), right=Tree(data='C', left=Tree(data='D')))

string = ['X(']
treeToString(tree, string=string)
string.append(')')
print("".join(string)) # X(A(B)(C(D)))
