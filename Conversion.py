class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_operator(ch):
    return ch in "+-*/"


def construct_tree(prefix):
    stack = []

    # Scan prefix expression from right to left
    for ch in reversed(prefix):
        if not is_operator(ch):
            stack.append(Node(ch))
        else:
            node = Node(ch)
            node.left = stack.pop()
            node.right = stack.pop()
            stack.append(node)

    return stack.pop()


def postorder(root):
    if root is None:
        return

    stack1 = [root]
    stack2 = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    print("Post-order traversal: ", end="")
    while stack2:
        print(stack2.pop().data, end=" ")
    print()


def delete_tree(root):
    if root is None:
        return

    delete_tree(root.left)
    delete_tree(root.right)

    root.left = None
    root.right = None
    root.data = None


prefix = input("Enter prefix expression: ")

root = construct_tree(prefix)

postorder(root)

delete_tree(root)
root = None

print("Entire tree deleted successfully.")