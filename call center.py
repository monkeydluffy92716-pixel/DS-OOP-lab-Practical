from collections import deque

call_queue = deque()

# Add a call to the queue
def addCall(customerID, callTime):
    call_queue.append((customerID, callTime))
    print("Call added successfully.")

# Answer and remove the first call
def answerCall():
    if not isQueueEmpty():
        call = call_queue.popleft()
        print("Answered Call - Customer ID:", call[0],
              "Call Time:", call[1], "minutes")
    else:
        print("No calls waiting.")

# Display all pending calls
def viewQueue():
    if isQueueEmpty():
        print("Call queue is empty.")
    else:
        print("Pending Calls:")
        for call in call_queue:
            print("Customer ID:", call[0],
                  "Call Time:", call[1], "minutes")

# Check whether the queue is empty
def isQueueEmpty():
    return len(call_queue) == 0

# Menu-driven program
while True:
    print("\n1. Add Call")
    print("2. Answer Call")
    print("3. View Queue")
    print("4. Check if Queue is Empty")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        customerID = input("Enter Customer ID: ")
        callTime = float(input("Enter Call Time (minutes): "))
        addCall(customerID, callTime)

    elif choice == '2':
        answerCall()

    elif choice == '3':
        viewQueue()

    elif choice == '4':
        if isQueueEmpty():
            print("Queue is empty.")
        else:
            print("Queue is not empty.")

    elif choice == '5':
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")