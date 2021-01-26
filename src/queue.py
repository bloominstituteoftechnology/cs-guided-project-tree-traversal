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
class Queue:
    def __init__(self):
        self.queue = []
​
    def enqueue(self, v):
        self.queue.append(v)  # O(1)
​
    def dequeue(self):
        return self.queue.pop(0)  # O(n) TODO make this not horrible
​
    def is_empty(self):
        return self.queue == []
​
def bft(root):
    queue = Queue()
​
    queue.enqueue(root)
​
    while not queue.is_empty():
​
        cur = queue.dequeue()
​
        if cur is None:
            continue
​
        print(cur.value)  # Visit the node
​
        queue.enqueue(cur.left)
        queue.enqueue(cur.right)
​
bft(root)
