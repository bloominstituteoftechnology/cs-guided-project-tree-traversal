'''
Implement a depth-first traversal iteratively
'''
def iter_dft(root):
    # Performs a pre-order traversal iteratively 
    # visits the nodes of the tree in depth-first order 
    # and returns a list of the visited values 
    # we need some way to visit the nodes in the same 
    # order but without recursion 
    # since we noticed that traversing using recursion 
    # visits the nodes of the tree in LIFO ordering
    # let's use a stack to achieve the same effect 
    # the stack will keep track of the order of elements
    # as we traverse through the tree 
    stack = [] 
    result = [] 
    
    # what do we initially add to our stack? 
    # add our initial root node to our stack 
    stack.append(root)
​
    # how do we loop through our tree? 
    # add and remove nodes from our stack in LIFO 
    while len(stack) > 0:
        # pop off the top stack element 
        # this is the current node we're visiting 
        current = stack.pop() 
​
        # add the current node's children to the stack (if it has children) 
        if current.right is not None:
            stack.append(current.right)
​
        if current.left is not None:
            stack.append(current.left)
​
        result.append(current.value)
​
    return result 
    
from collections import deque 
​
def bft(root):
    # visits the nodes of the tree in breadth-first order 
    # adds all the nodes to a result list and returns it 
    queue = deque() # holds on to nodes 
    result = [] # holds on to values of nodes 
​
    queue.append(root)
​
    while len(queue) > 0: 
        # dequeue the node that was added earliest to the queue 
        # current = queue.pop(0) # O(n)
        current = queue.popleft() # O(1) 
        # Ring buffer 
​
        result.append(current.value)
​
        if current.left is not None:
            queue.append(current.left)
​
        if current.right is not None:
            queue.append(current.right)
​
    return result