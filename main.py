import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

    print(todo)


st.title("Enda's ToDo App")
st.subheader("A todo app to track tasks")
st.write("This should help increase productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    # print
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo item:", placeholder="Add new to do item...", on_change=add_todo, key="new_todo")

# st.session_state  # used to output session state to UI
