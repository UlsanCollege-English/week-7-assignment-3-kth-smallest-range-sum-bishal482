# kth_range.py

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    """Insert a value into the BST. Duplicates are ignored."""
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    # if val == root.val, do nothing (ignore duplicates)
    return root

def kth_smallest(root, k):
    """Return the k-th smallest value in BST (1-based index)."""
    stack = []
    node = root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        k -= 1
        if k == 0:
            return node.val
        node = node.right
    raise IndexError("k is larger than number of nodes in BST")

def range_sum_bst(root, low, high):
    """Return the sum of all node values in BST within [low, high]."""
    if not root:
        return 0
    total = 0
    if low <= root.val <= high:
        total += root.val
    if root.val > low:
        total += range_sum_bst(root.left, low, high)
    if root.val < high:
        total += range_sum_bst(root.right, low, high)
    return total
