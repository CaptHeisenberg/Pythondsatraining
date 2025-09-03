class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def maxDepth(root):
    if root is None:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))