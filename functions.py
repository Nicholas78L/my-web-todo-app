FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):    # This is a custom function with a PARAMETER of the function (filepath).
    """ Read a text file and return the list of to-do items. """
    with open(filepath, 'r') as file_local:        # open() - это функция, создающая объект типа "файл"
        todos_local = file_local.readlines()
    return todos_local                          # it returns a list 'todos'


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write to-do items list in the text file. """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


# if __name__ == '__main__':
if __name__ == '__main__':
    print('Hello')
    print(get_todos())

