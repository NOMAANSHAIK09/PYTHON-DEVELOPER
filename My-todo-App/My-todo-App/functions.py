FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    try:
        with open(filepath, 'r') as file:
            todos = file.readlines()
    except FileNotFoundError:
        # If file doesn't exist, create it empty
        with open(filepath, 'w') as file:
            pass
        todos = []
    return todos

def write_todos(todos, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos)

if __name__ == "__main__":
    print(get_todos())
