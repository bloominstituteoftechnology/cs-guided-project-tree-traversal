# Depth-first Traversals
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
​
root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.left.right.right = TreeNode(4.5)
root.right = TreeNode(6)
root.right.right = TreeNode(7)
​
# BST DF Traversals
​
def in_order(n):
    if n is None:
        return
​
    in_order(n.left)
    print(n.value)   # "visit" the node
    in_order(n.right)
​
def pre_order(n):
    if n is None:
        return
​
    print(n.value)   # "visit" the node
    pre_order(n.left)
    pre_order(n.right)
​
def post_order(n):
    if n is None:
        return
​
    post_order(n.left)
    post_order(n.right)
    print(n.value)   # "visit" the node
​
in_order(root)
print()
#pre_order(root)
post_order(root)