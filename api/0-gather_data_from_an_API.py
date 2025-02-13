#!/usr/bin/python3

def get_todo_progress():
    emp_id = input("Enter employee ID: ")
    print(f"Fetching data for Employee {emp_id}...")
    
    # Simulated data retrieval
    user_name = "John Doe"
    total_tasks = 10
    done_tasks = ["Task 1", "Task 2", "Task 3", "Task 4"]
    
    print(f"Employee {user_name} is done with tasks({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task}")

if __name__ == "__main__":
    get_todo_progress()
