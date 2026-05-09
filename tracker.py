print("=== Learning Tracker ===")

while True:
    print(f"\nTotal Completed Tasks: {len(tasks)}")
    print("Completed Tasks:")
    print("2. View progress")
    print("3. Exit")

    choice = input("Select an option: ")

    if choice == "3":
        print("Goodbye!")
        break
