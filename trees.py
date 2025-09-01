from collections import deque


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
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)
def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)
root = None
data = {50,30,70,20,40,60,80}
for d in data:
    root = insert(root,d)
data = [50, 30, 70, 20, 40, 60, 80]
root = None
for d in data:
    root = insert(root, d)

print("Inorder: ", end="")
inorder(root)
print("\nPreorder: ", end="")
preorder(root)
print("\nPostorder: ", end="")
postorder(root)

def levelorder(root):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.data, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
print("\nLevelorder: ", end="")
levelorder(root)

def maxDepth(root):
    if root is None:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
print("Max Depth of tree:", maxDepth(root))
