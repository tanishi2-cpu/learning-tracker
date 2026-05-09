tasks = []

print("=== Learning Tracker ===")

while True:
    print(f"\nTotal Completed Tasks: {len(tasks)}")
    print("Completed Tasks:")
    print("2. View progress")
    print("3. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        task = input("Enter completed task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        print("\nCompleted Tasks:")
        
        if len(tasks) == 0:
            print("No tasks completed yet.")

        else:
            for task in tasks:
                print("-", task)

    elif choice == "3":
        print("Goodbye!")
        break
