import streamlit as st
import functions as fc

todos = fc.get_todos()

def add_todo():
    new_todo = st.session_state['input_box'] + "\n"
    todos.append(new_todo)
    fc.write_todos(todos)

st.title('My ToDo App')

for value, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=value)
    if checkbox:
        todos.pop(value)
        fc.write_todos(todos)
        del st.session_state[value]
        st.experimental_rerun()
st.text_input(label='', placeholder='Add new to do...'
              ,on_change=add_todo, key='input_box')

#st.session_state