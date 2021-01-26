"""
You are given the values from a preorder and an inorder tree traversal. Write a
function that can take those inputs and outputs a binary tree that adheres
to the given orderings. 
​
*Note: assume that there will not be any duplicates in the tree.*
​
Example:
Inputs:
preorder = [5,7,22,13,9]
inorder = [7,5,13,22,9]
​
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
​
def build_tree(preorder, inorder):
    """
    Input: Two lists of ints, where the preorder list represents 
    the output from running a preorder traversal over a tree, and 
    the inorder list represents the output from running an inorder
    travesal over a tree.
    Output: The tree from which these two lists were created from. 
    """ 
    # What's the relationship between a preorder and an inorder output? 
    # The first element in the preorder list is the root of the tree 
    # The root of a tree in inorder straddles its subtrees 
    # Preorder: root, left, right 
    # Inorder: left, root, right 
​
    # Create the root of the entire tree by grabbing the first 
    # element in the preorder list 
    # We can find the preorder root in the inorder list 
    # From that we can see which elements belong 
    # in the left subtree and which elements belong 
    # in the right subtree 
    
    # base case(s) 
    # we want to get through these arrays 
    # when we iterate through the entire inorder list 
    # we've considered every element and we've built the
    # entire tree 
​
    # how do we move closer to a base case?
    # 1. take the first element in the preorder list 
    # 2. locate that element in the inorder list 
    # 3. figure out the size of the two halves of the inorder list
    #    let l be the length of the left sublist
    #    let r be the length of the right sublist 
    # 4. take the l elements after the first preorder value 
    #    recurse here to build the left subtree 
    # 5. take the r elements after the first preorder value and the 
    #    first l values 
