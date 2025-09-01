class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
def insert(root,data):
    if root is None:
        root = Node(data)
        return root
    elif data < root.data:
        root.left = insert(root.left,data)
    else:
        root.right = insert(root.right,data)