import streamlit as st
import functions

todos = functions.get_todos()

st.title("Enda's ToDo App")
st.subheader("A todo app to track tasks")
st.write("This should help increase productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo item:", placeholder="Add new to do item...")

