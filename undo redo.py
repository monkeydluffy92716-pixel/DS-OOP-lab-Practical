# Undo/Redo system using two stacks

document = ""
undo_stack = []
redo_stack = []

def make_change(new_text):
    global document
    undo_stack.append(document)
    document += new_text
    redo_stack.clear()
    print("Change made successfully.")

def undo_action():
    global document
    if undo_stack:
        redo_stack.append(document)
        document = undo_stack.pop()
        print("Undo successful.")
    else:
        print("Nothing to undo.")

def redo_action():
    global document
    if redo_stack:
        undo_stack.append(document)
        document = redo_stack.pop()
        print("Redo successful.")
    else:
        print("Nothing to redo.")

def display_document():
    print("Current Document:", document)

# Menu-driven program
while True:
    print("\n1. Make Change")
    print("2. Undo Action")
    print("3. Redo Action")
    print("4. Display Document")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        text = input("Enter text to add: ")
        make_change(text)
    elif choice == '2':
        undo_action()
    elif choice == '3':
        redo_action()
    elif choice == '4':
        display_document()
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice.")