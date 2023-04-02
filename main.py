import datetime

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, priority, due_date):
        """Add a task to the to-do list."""
        self.tasks.append({
            'task': task,
            'priority': priority,
            'due_date': due_date
        })

    def remove_task(self, task):
        """Remove a task from the to-do list."""
        for t in self.tasks:
            if t['task'] == task:
                self.tasks.remove(t)
                break

    def show_tasks(self):
        """Display all tasks in the to-do list."""
        if not self.tasks:
            print('No tasks yet!')
        else:
            print('Tasks:')
            for i, task in enumerate(self.tasks):
                # Display task details including priority level and due date
                print(f'{i + 1}. {task["task"]} ({task["priority"]}) - Due {task["due_date"].strftime("%Y-%m-%d")}')

    def sort_tasks(self, key):
        """Sort the tasks in the to-do list by the specified key (priority or due date)."""
        if key == 'priority':
            # Sort tasks by priority level (high, medium, low)
            self.tasks = sorted(self.tasks, key=lambda x: x['priority'], reverse=True)
        elif key == 'due_date':
            # Sort tasks by due date
            self.tasks = sorted(self.tasks, key=lambda x: x['due_date'])
        else:
            print('Invalid sorting key. Choose either "priority" or "due_date".')

def main():
    todo_list = TodoList()

    while True:
        # Display menu options
        print('1. Add task')
        print('2. Remove task')
        print('3. Show tasks')
        print('4. Sort tasks')
        print('5. Quit')
        choice = input('Enter your choice: ')

        if choice == '1':
            # Prompt user for task details and add task to the list
            task = input('Enter task: ')
            priority = input('Enter priority (high, medium, low): ')
            while priority not in ['high', 'medium', 'low']:
                priority = input('Invalid priority. Enter priority (high, medium, low): ')
            due_date = input('Enter due date (YYYY-MM-DD): ')
            try:
                due_date = datetime.datetime.strptime(due_date, '%Y-%m-%d')
            except ValueError:
                print('Invalid date format. Try again.')
                continue
            todo_list.add_task(task, priority, due_date)
            print(f'Task "{task}" added.')
        elif choice == '2':
            # Prompt user for task to remove and remove it from the list
            task = input('Enter task: ')
            if task in [t['task'] for t in todo_list.tasks]:
                todo_list.remove_task(task)
                print(f'Task "{task}" removed.')
            else:
                print(f'Task "{task}" not found.')
        elif choice == '3':
            # Display all tasks in the list
            todo_list.show_tasks()
        elif choice == '4':
            # Prompt user for sorting criteria and sort the tasks
            key = input('Sort by priority or due date? ')
            todo_list.sort_tasks(key)
            todo_list.show_tasks()
        elif choice == '5':
            # Exit the program
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Try again.')

if __name__ == '__main__':
    main()

## Keval Rakholiya
## Thank you 
