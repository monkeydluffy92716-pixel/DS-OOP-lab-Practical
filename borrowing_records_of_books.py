from collections import Counter

borrow_count = [3, 0, 5, 2, 3, 0, 4, 3]


average = sum(borrow_count) / len(borrow_count)
print("Average books borrowed:", average)

highest = max(borrow_count)
lowest = min(borrow_count)
print("Highest borrowing count:", highest)
print("Lowest borrowing count:", lowest)

zero_count = borrow_count.count(0)
print("Members who borrowed no books:", zero_count)

frequency = Counter(borrow_count)
max_frequency = max(frequency.values())
modes = [k for k, v in frequency.items() if v == max_frequency]
print("Most frequent borrowing count(s):", modes)