class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Insert a node
    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)

        return root

    # Search for a node
    def search(self, root, key):
        if root is None or root.data == key:
            return root

        if key < root.data:
            return self.search(root.left, key)

        return self.search(root.right, key)

    # Find minimum node
    def find_min(self, root):
        while root.left:
            root = root.left
        return root

    # Delete a node
    def delete(self, root, key):
        if root is None:
            return None

        if key < root.data:
            root.left = self.delete(root.left, key)
        elif key > root.data:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            successor = self.find_min(root.right)
            root.data = successor.data
            root.right = self.delete(root.right, successor.data)

        return root

    # Display using inorder traversal
    def display(self, root):
        if root:
            self.display(root.left)
            print(root.data, end=" ")
            self.display(root.right)


# Main program
tree = BST()

while True:
    print("\n\n1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        value = int(input("Enter value: "))
        tree.root = tree.insert(tree.root, value)
        print("Node inserted.")

    elif choice == '2':
        value = int(input("Enter value to delete: "))
        tree.root = tree.delete(tree.root, value)
        print("Deletion operation completed.")

    elif choice == '3':
        value = int(input("Enter value to search: "))
        if tree.search(tree.root, value):
            print("Value found.")
        else:
            print("Value not found.")

    elif choice == '4':
        print("BST elements (Inorder): ", end="")
        tree.display(tree.root)

    elif choice == '5':
        break

    else:
        print("Invalid choice.")