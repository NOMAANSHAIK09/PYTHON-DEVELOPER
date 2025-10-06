import streamlit as st
import functions as fun

todos = fun.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos = fun.get_todos()
    todos.append(todo)
    fun.write_todos(todos)
    st.session_state["new_todo"] = ""



st.title("My To-Do App")
st.subheader("This a todo app.")
st.write("The To-Do app helps users organize their daily tasks by allowing them to create, edit, and manage task lists. "
         "It acts as a digital planner where users can keep track of what needs to be done, set priorities, and mark "
         "tasks as completed — improving productivity and reducing the chance of forgetting important activities.")

# Render all todos
for index, todo in enumerate(todos):
    if st.checkbox(todo.strip(), key=todo):
        todos.pop(index)
        fun.write_todos(todos)
        if todo in st.session_state:
            del st.session_state[todo]
            st.rerun()

        
st.text_input(label="", placeholder="Add new todo",
              on_change=add_todo, key='new_todo')
