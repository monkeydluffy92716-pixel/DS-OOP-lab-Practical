# Hash table of size 10 using chaining

SIZE = 10
hash_table = [[] for _ in range(SIZE)]

# Hash function using division method
def hash_function(key):
    return key % SIZE

# Insert key-value pair
def insert(key, value):
    index = hash_function(key)

    for i, (k, v) in enumerate(hash_table[index]):
        if k == key:
            hash_table[index][i] = (key, value)
            print("Key updated successfully.")
            return

    hash_table[index].append((key, value))
    print("Key inserted successfully.")

# Search for a key
def search(key):
    index = hash_function(key)

    for k, v in hash_table[index]:
        if k == key:
            print("Value:", v)
            return

    print("Key not found.")

# Delete a key
def delete(key):
    index = hash_function(key)

    for i, (k, v) in enumerate(hash_table[index]):
        if k == key:
            hash_table[index].pop(i)
            print("Key deleted successfully.")
            return

    print("Key not found.")

# Display the hash table
def display():
    for i in range(SIZE):
        print(i, ":", hash_table[i])

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
        value = input("Enter value: ")
        insert(key, value)

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