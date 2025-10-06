FILEPATH="todos.txt"
def get_todos(filepath=FILEPATH):
    with open(filepath,'r') as file:
            todos=file.readlines()
    return todos
def write_todos(todos,filepath=FILEPATH):
     with open(filepath,'w') as file:
            file.writelines(todos) 
if __name__ == "__todo__":
      print(get_todos())