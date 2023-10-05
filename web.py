import streamlit as st
import functions

todos = functions.get_todos()   # That gives us a list of 'todos'


def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    # session_state is an object, which looks like a dictionary, and
    # contains the widget's information (if the widget has a key!!! and
    # if this widget is a part of st.checkbox() !!!).
    # key is - 'new_todo' (from st.text_input()),
    # value  is - what the user will enter in 'st.text_input()'.
    # but st.session_state[] - is a session_state type (specific object type of streamlit)
    # it looks like we call the key ['new_todo'] and
    # get the value (what the user enter), and store it in variable 'todo'
    todos.append(todo)
    functions.write_todos(todos)


st.title('My todo web app')
st.subheader('This is my todo app')
st.text('This app is to increase your productivity.')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index) # delete the complete todo from the list
        functions.write_todos(todos)  # rewrite the todo list
        del st.session_state[todo]  # delete the complete todo (with checkbox)
        # from the st.session_state "dictionary"
        st.rerun()  # rerun streamlit

st.text_input(label='Enter a todo: ', placeholder='Add your new todo...',
              on_change=add_todo, key='new_todo')  # on_change is an argument
            # which equals to callback or, in other words,
            #  customer function ('add_todo()' - in our case).

print('Hello! How are you, man?')