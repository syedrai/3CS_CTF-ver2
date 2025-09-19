# Binary tree for in-order traversal
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Simple tree: concatenate values in-order to get flag
root = Node("3CS{CTF-")
root.left = Node("Vers.2_")
root.right = Node("treewalk}")

def inorder(node):
    return inorder(node.left) + node.val + inorder(node.right) if node else ""
flag = inorder(root)
print("Flag:", flag)
