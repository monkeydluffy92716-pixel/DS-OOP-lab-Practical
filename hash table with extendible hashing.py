class Bucket:
    def __init__(self, depth):
        self.depth = depth
        self.data = {}


class ExtendibleHash:
    def __init__(self, bucket_size=2):
        self.global_depth = 1
        self.bucket_size = bucket_size

        b0 = Bucket(1)
        b1 = Bucket(1)

        self.directory = [b0, b1]

    def get_index(self, key):
        return key & ((1 << self.global_depth) - 1)

    # Insert key-value pair
    def insert(self, key, value):
        while True:
            index = self.get_index(key)
            bucket = self.directory[index]

            if key in bucket.data:
                bucket.data[key] = value
                print("Key updated successfully.")
                return

            if len(bucket.data) < self.bucket_size:
                bucket.data[key] = value
                print("Key inserted successfully.")
                return

            self.split_bucket(index)

    # Split a full bucket
    def split_bucket(self, index):
        bucket = self.directory[index]

        if bucket.depth == self.global_depth:
            self.directory = self.directory + self.directory
            self.global_depth += 1

        old_depth = bucket.depth
        bucket.depth += 1
        new_bucket = Bucket(bucket.depth)

        split_bit = 1 << old_depth

        for i in range(len(self.directory)):
            if self.directory[i] is bucket and (i & split_bit):
                self.directory[i] = new_bucket

        old_data = bucket.data.copy()
        bucket.data.clear()

        for key, value in old_data.items():
            self.insert(key, value)

    # Search for a key
    def search(self, key):
        index = self.get_index(key)
        bucket = self.directory[index]

        if key in bucket.data:
            print("Value:", bucket.data[key])
            return bucket.data[key]

        print("Key not found.")
        return None

    # Delete a key
    def delete(self, key):
        index = self.get_index(key)
        bucket = self.directory[index]

        if key in bucket.data:
            del bucket.data[key]
            print("Key deleted successfully.")
        else:
            print("Key not found.")


# Menu-driven program
ht = ExtendibleHash(bucket_size=2)

while True:
    print("\n1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        key = int(input("Enter key: "))
        value = input("Enter value: ")
        ht.insert(key, value)

    elif choice == "2":
        key = int(input("Enter key to search: "))
        ht.search(key)

    elif choice == "3":
        key = int(input("Enter key to delete: "))
        ht.delete(key)

    elif choice == "4":
        break

    else:
        print("Invalid choice.")