class Stack:
    def __init__(self):
        self.stack = []
​
    def push(self, value):
        self.stack.append(value)
​
    def pop(self):
        return self.stack.pop()
​
    def peek(self):
        return self.stack[-1]
​
    def is_empty(self):
        return self.stack == []
​
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
def dft(root):
​
    # Create a stack
    stack = Stack()
​
    # Push the root node on the stack
    stack.push(root)
​
    # Main loop, while stack isn't empty:
    while not stack.is_empty():
​
        # pop the cur node off the stack
        cur = stack.pop()
​
        # base case
        if cur is None:
            continue
​
        # "visit" that node, print the node value
        print(cur.value)
​
        # push its right and left nodes to the stack
        stack.push(cur.right)
        stack.push(cur.left)
​
dft(root)
​
"""
Stack: <- top   # which nodes we still have to visit
​
Output: 5 3 1 4 4.5 6 7
​
​
Init:
    Create a stack
    Push the root node on the stack
​
Main loop, while stack isn't empty:
    pop the cur node off the stack
    "visit" that node, print the node value
    push its right and left nodes to the stack
​
"""
​
