class Node:
    def __init__(self, city, population):
        self.city = city
        self.population = population
        self.left = None
        self.right = None


class CityBST:
    def __init__(self):
        self.root = None

    def insert(self, root, city, population):
        if root is None:
            return Node(city, population)

        if city.lower() < root.city.lower():
            root.left = self.insert(root.left, city, population)
        elif city.lower() > root.city.lower():
            root.right = self.insert(root.right, city, population)
        else:
            root.population = population

        return root

    def search(self, root, city):
        comparisons = 0

        while root:
            comparisons += 1

            if city.lower() == root.city.lower():
                return root, comparisons
            elif city.lower() < root.city.lower():
                root = root.left
            else:
                root = root.right

        return None, comparisons

    def find_min(self, root):
        while root.left:
            root = root.left
        return root

    def delete(self, root, city):
        if root is None:
            return None

        if city.lower() < root.city.lower():
            root.left = self.delete(root.left, city)
        elif city.lower() > root.city.lower():
            root.right = self.delete(root.right, city)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            successor = self.find_min(root.right)
            root.city = successor.city
            root.population = successor.population
            root.right = self.delete(root.right, successor.city)

        return root

    def display_ascending(self, root):
        if root:
            self.display_ascending(root.left)
            print(root.city, "-", root.population)
            self.display_ascending(root.right)

    def display_descending(self, root):
        if root:
            self.display_descending(root.right)
            print(root.city, "-", root.population)
            self.display_descending(root.left)

    def height(self, root):
        if root is None:
            return 0
        return 1 + max(self.height(root.left),
                       self.height(root.right))


bst = CityBST()

while True:
    print("\n1. Add City")
    print("2. Delete City")
    print("3. Update Population")
    print("4. Search City")
    print("5. Display Ascending Order")
    print("6. Display Descending Order")
    print("7. Maximum Comparisons")
    print("8. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        city = input("Enter city name: ")
        population = int(input("Enter population: "))
        bst.root = bst.insert(bst.root, city, population)
        print("City added successfully.")

    elif choice == '2':
        city = input("Enter city to delete: ")
        found, _ = bst.search(bst.root, city)

        if found:
            bst.root = bst.delete(bst.root, city)
            print("City deleted successfully.")
        else:
            print("City not found.")

    elif choice == '3':
        city = input("Enter city name: ")
        found, _ = bst.search(bst.root, city)

        if found:
            population = int(input("Enter new population: "))
            found.population = population
            print("Population updated successfully.")
        else:
            print("City not found.")

    elif choice == '4':
        city = input("Enter city to search: ")
        found, comparisons = bst.search(bst.root, city)

        if found:
            print("City:", found.city)
            print("Population:", found.population)
        else:
            print("City not found.")

        print("Comparisons:", comparisons)

    elif choice == '5':
        print("\nCities in Ascending Order:")
        bst.display_ascending(bst.root)

    elif choice == '6':
        print("\nCities in Descending Order:")
        bst.display_descending(bst.root)

    elif choice == '7':
        print("Maximum comparisons required:",
              bst.height(bst.root))

    elif choice == '8':
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")