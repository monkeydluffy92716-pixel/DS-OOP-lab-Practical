SIZE = 10
hash_table = [None] * SIZE
DELETED = "DELETED"

# Hash function using division method
def hash_function(key):
    return key % SIZE

# Insert a key
def insert(key):
    index = hash_function(key)

    for i in range(SIZE):
        pos = (index + i) % SIZE

        if hash_table[pos] is None or hash_table[pos] == DELETED:
            hash_table[pos] = key
            print("Key inserted successfully.")
            return

        if hash_table[pos] == key:
            print("Key already exists.")
            return

    print("Hash table is full.")

# Search for a key
def search(key):
    index = hash_function(key)

    for i in range(SIZE):
        pos = (index + i) % SIZE

        if hash_table[pos] is None:
            break

        if hash_table[pos] == key:
            print("Key found at index", pos)
            return

    print("Key not found.")

# Delete a key
def delete(key):
    index = hash_function(key)

    for i in range(SIZE):
        pos = (index + i) % SIZE

        if hash_table[pos] is None:
            break

        if hash_table[pos] == key:
            hash_table[pos] = DELETED
            print("Key deleted successfully.")
            return

    print("Key not found.")

# Display the table
def display():
    print("\nIndex\tKey")
    for i in range(SIZE):
        print(i, "\t", hash_table[i])

# Menu-driven program
while True:
    print("\n1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        key = int(input("Enter key: "))
        insert(key)

    elif choice == "2":
        key = int(input("Enter key to search: "))
        search(key)

    elif choice == "3":
        key = int(input("Enter key to delete: "))
        delete(key)

    elif choice == "4":
        display()

    elif choice == "5":
        break

    else:
        print("Invalid choice.")