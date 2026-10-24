class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def tokenize(formula):
    tokens = []
    for ch in formula:
        if ch.isspace():
            continue
        if ch.isalnum() or ch in "&|!>()":
            tokens.append(ch)
        else:
            raise ValueError("Invalid character: " + ch)
    return tokens


def build_tree(tokens):
    # Operator precedence: NOT > AND > OR > implication
    precedence = {'!': 4, '&': 3, '|': 2, '>': 1}
    output = []
    operators = []

    for token in tokens:
        if token.isalnum():
            output.append(Node(token))

        elif token == '(':
            operators.append(token)

        elif token == ')':
            while operators and operators[-1] != '(':
                apply_operator(output, operators.pop())
            if not operators:
                raise ValueError("Mismatched parentheses")
            operators.pop()

        else:
            while (operators and operators[-1] != '(' and
                   precedence[operators[-1]] >= precedence[token]):
                apply_operator(output, operators.pop())
            operators.append(token)

    while operators:
        if operators[-1] == '(':
            raise ValueError("Mismatched parentheses")
        apply_operator(output, operators.pop())

    if len(output) != 1:
        raise ValueError("Invalid formula")

    return output[0]


def apply_operator(output, op):
    node = Node(op)

    if op == '!':
        if not output:
            raise ValueError("Missing operand")
        node.right = output.pop()
    else:
        if len(output) < 2:
            raise ValueError("Missing operand")
        node.right = output.pop()
        node.left = output.pop()

    output.append(node)


def display_inorder(root):
    if root:
        if root.left:
            print("(", end="")
        display_inorder(root.left)
        print(root.value, end="")
        display_inorder(root.right)
        if root.left:
            print(")", end="")


formula = input("Enter propositional formula: ")

try:
    tokens = tokenize(formula)
    root = build_tree(tokens)
    print("Binary tree created successfully.")
    print("Inorder representation: ", end="")
    display_inorder(root)
    print()
except ValueError as e:
    print("Invalid formula:", e)