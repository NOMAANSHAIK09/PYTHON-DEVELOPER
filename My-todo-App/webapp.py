import streamlit as st
import functions as fun 

todos = fun.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos = fun.get_todos()
    todos.append(todo)
    fun.write_todos(todos)
    st.session_state["new_todo"] = ""

st.title("My Todo-App")
st.subheader("This a todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        fun.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="",placeholder="add new todo",
              on_change=add_todo,key='new_todo')
#https://github.com/NOMAANSHAIK09/My-todo-App.git
