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
    return root
def inorder(root):
    if root:
     inorder(root.left)
     print(root.data)
     inorder(root.right)
root = None
data = {50,30,70,20,40,60,80}
for d in data:
    root = insert(root,d)
inorder(root)