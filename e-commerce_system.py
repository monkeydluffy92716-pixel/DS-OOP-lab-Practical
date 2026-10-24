# Customer account IDs
account_ids = [101, 105, 110, 115, 120, 125, 130]

# Linear Search
def linear_search(ids, key):
    for i in range(len(ids)):
        if ids[i] == key:
            return i
    return -1

# Binary Search
def binary_search(ids, key):
    low = 0
    high = len(ids) - 1

    while low <= high:
        mid = (low + high) // 2

        if ids[mid] == key:
            return mid
        elif ids[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Search for a customer account ID
key = int(input("Enter customer account ID: "))

# Linear Search Result
result1 = linear_search(account_ids, key)
if result1 != -1:
    print("Linear Search: Account found at index", result1)
else:
    print("Linear Search: Account not found")

# Binary Search Result
result2 = binary_search(account_ids, key)
if result2 != -1:
    print("Binary Search: Account found at index", result2)
else:
    print("Binary Search: Account not found")