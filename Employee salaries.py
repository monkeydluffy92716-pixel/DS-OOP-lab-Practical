# Employee salaries
salaries = [45000.50, 60000.00, 35000.75, 80000.00,
            55000.25, 90000.00, 70000.50, 40000.00]

# Selection Sort
def selection_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Bubble Sort
def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# Sort using both algorithms
selection_result = selection_sort(salaries)
bubble_result = bubble_sort(salaries)

print("Selection Sort:", selection_result)
print("Bubble Sort:", bubble_result)

# Display top five highest salaries
print("Top 5 highest salaries:")
for salary in selection_result[-5:][::-1]:
    print(salary)