"""
You are given the values from a postorder and an inorder tree traversal. Write
a function that can take those inputs and output a binary tree.

*Note: assume that there will not be any duplicates in the tree.*

Example:
Inputs:
postorder = [7,13,9,22,5]
inorder = [7,5,13,22,9]

Output:
    5
   / \
  7  22
    /  \
   13   9
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(inorder, postorder):
    # Your code here

