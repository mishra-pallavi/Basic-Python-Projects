# To-Do List Application

# Function to display the to-do list
def show_todo_list():
    with open("todo.txt", "r") as file:
        lines = file.readlines()
        if not lines:
            print("Your to-do list is empty.")
        else:
            for i, line in enumerate(lines, 1):
                print(f"{i}. {line.strip()}")

# Function to add a task to the to-do list
def add_task(task):
    with open("todo.txt", "a") as file:
        file.write(task + "\n")

# Function to mark a task as completed
def mark_completed(task_index):
    with open("todo.txt", "r") as file:
        lines = file.readlines()
    with open("todo.txt", "w") as file:
        for i, line in enumerate(lines, 1):
            if i == task_index:
                file.write("✔ " + line)
            else:
                file.write(line)

# Function to delete a task
def delete_task(task_index):
    with open("todo.txt", "r") as file:
        lines = file.readlines()
    with open("todo.txt", "w") as file:
        for i, line in enumerate(lines, 1):
            if i != task_index:
                file.write(line)

# Main function
if __name__ == "__main__":
    while True:
        print("\nTo-Do List Menu:")
        print("1. Show to-do list")
        print("2. Add a task")
        print("3. Mark task as completed")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_todo_list()
        elif choice == "2":
            task = input("Enter the task: ")
            add_task(task)
            print("Task added to the list.")
        elif choice == "3":
            show_todo_list()
            task_index = int(input("Enter the task number to mark as completed: "))
            mark_completed(task_index)
            print("Task marked as completed.")
        elif choice == "4":
            show_todo_list()
            task_index = int(input("Enter the task number to delete: "))
            delete_task(task_index)
            print("Task deleted.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
