import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"]
    print(todo)

todos = functions.get_todos()

st.title("Enda's ToDo App")
st.subheader("A todo app to track tasks")
st.write("This should help increase productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo item:", placeholder="Add new to do item...", on_change=add_todo, key="new_todo")

# st.session_state # used to output session state to UI

