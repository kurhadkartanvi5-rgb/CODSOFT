todo_list = []

while True:
    print("\nTO-DO LIST ")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Remove a Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        todo_list.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(todo_list) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(todo_list)):
                print(f"{i + 1}. {todo_list[i]}")

    elif choice == "3":
        if len(todo_list) == 0:
            print("No tasks to remove.")
        else:
            print("\nCurrent Tasks:")
            for i in range(len(todo_list)):
                print(f"{i + 1}. {todo_list[i]}")

            task_number = int(input("Enter task number to remove: "))

            if 1 <= task_number <= len(todo_list):
                removed_task = todo_list.pop(task_number - 1)
                print(f"'{removed_task}' removed successfully!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Thank you for using the To-Do List Application.")
        break

    else:
        print("Please enter a valid choice.")