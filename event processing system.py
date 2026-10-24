from collections import deque

event_queue = deque()

# Add a new event
def add_event():
    event = input("Enter event name: ")
    event_queue.append(event)
    print("Event added successfully.")

# Process the oldest event
def process_event():
    if event_queue:
        event = event_queue.popleft()
        print("Processed event:", event)
    else:
        print("No events to process.")

# Display pending events
def display_events():
    if event_queue:
        print("Pending events:", list(event_queue))
    else:
        print("No pending events.")

# Cancel an event
def cancel_event():
    event = input("Enter event to cancel: ")
    if event in event_queue:
        event_queue.remove(event)
        print("Event cancelled successfully.")
    else:
        print("Event not found in queue.")

# Menu-driven program
while True:
    print("\n1. Add Event")
    print("2. Process Next Event")
    print("3. Display Pending Events")
    print("4. Cancel Event")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_event()
    elif choice == '2':
        process_event()
    elif choice == '3':
        display_events()
    elif choice == '4':
        cancel_event()
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice.")