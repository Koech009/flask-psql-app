# define the node class
from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# define the tree
root = Node("CEO")
root.left = Node("CTO")
root.right = Node("CFO")
root.left.left = Node("Dev Manager")
root.left.right = Node("QA Manager")
root.right.left = Node("Finance Manager")
root.right.right = Node("Accounting Manager")


# binary search tree= left < root < right
bst_root = Node(10)
bst_root.left = Node(5)
bst_root.right = Node(15)
bst_root.left.left = Node(3)
bst_root.left.right = Node(7)
bst_root.right.left = Node(12)
bst_root.right.right = Node(18)
bst_root.right.right.right = Node(20)

# implement the traversal methods


def pre_order(node):
    if node:
        print(node.value)
        pre_order(node.left)
        pre_order(node.right)


def in_order(node):
    if node:
        in_order(node.left)
        print(node.value)
        in_order(node.right)


def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.value)


# Level order traversal using a queue(top-down,left to right)


def level_order(node):
    if not node:
        return
    queue = deque([node])
    while queue:
        current = queue.popleft()
        print(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)


# test the traversals
if __name__ == "__main__":
    print("Pre-order Traversal:")
    pre_order(root)
    print("\nIn-order Traversal:")
    in_order(root)
    print("\nPost-order Traversal:")
    post_order(root)
    print("\nLevel-order Traversal:")
    level_order(root)

    print("\n---Binary Search Tree Traversals---")
    print("In-order Traversal (BST):")
    in_order(bst_root)
    print("\nPre-order Traversal (BST):")
    pre_order(bst_root)
    print("\nPost-order Traversal (BST):")
    post_order(bst_root)
    print("\nLevel-order Traversal (BST):")
    level_order(bst_root)
