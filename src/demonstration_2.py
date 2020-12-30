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
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# ​
# def build_tree(preorder, inorder):
#     """
#     Input: Two lists of ints, where the preorder list represents 
#     the output from running a preorder traversal over a tree, and 
#     the inorder list represents the output from running an inorder
#     travesal over a tree.
#     Output: The tree from which these two lists were created from. 
#     """ 
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
    #    recurse here to build the right subtree

class TreeNode:
  def __init__(self, val):
    self.val = val 
	self.left = None 
	self.right = None
​
def build_tree(preorder, inorder):
  # base case: when we've gone through the entire inorder list,
  # then we've constructed the entire tree and are done 
  if not inorder:
    return 
	
  # the root is the first element in our preorder list 
  root = TreeNode(preorder[0])
  # find the index of the root value in our inorder list 
  inorder_index = inorder.index(root.val)
  
  # we move closer to the base case by cutting down the preorder
  # and inorder lists as we build tree nodes 
  # eventually, these lists will be empty because we'll have 
  # constructed the entire tree from them 
  
  # recursion to build the left subtree 
  # for the preorder list, skip the first element and take everything up
  # to but not including the root 
  # for the inorder list, take everything up to but not including the root
  root.left = build_tree(preorder[1:1+inorder_index], inorder[:inorder_index])
  
  # recursion to build the right subtree 
  # for the preorder list, take every element past the root
  # for the inorder list, take everything past the root 
  root.right = build_tree(preorder[1+inorder_index:], inorder[inorder_index+1:])
  
  return root 
  
# Methods to test out that our constructed tree is valid 
def preorder_helper(root, res):
    if root is None:
        return
    res.append(root.val)
    preorder_helper(root.left, res)
    preorder_helper(root.right, res)
​
def preorder_traversal(root):
    result = []
    preorder_helper(root, result)
    return result
​
def inorder_helper(root, res):
    if root is None:
        return
    inorder_helper(root.left, res)
    res.append(root.val)
    inorder_helper(root.right, res)
​
def inorder_traversal(root):
    result = []
    inorder_helper(root, result)
    return result
	
preorder = [5,7,22,13,9]
inorder = [7,5,13,22,9]
​
tree = build_tree(preorder, inorder)
​
print(inorder_traversal(tree) == inorder)
