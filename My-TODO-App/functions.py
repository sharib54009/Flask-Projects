import os

# Get the directory where functions.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILEPATH = os.path.join(BASE_DIR, "Todos.txt")


def get_todos(filename=FILEPATH):
    """Read todos from file."""
    try:
        with open(filename, "r") as file:
            todos = file.readlines()
    except FileNotFoundError:
        # Create file if it doesn't exist
        with open(filename, "w") as file:
            pass
        todos = []

    return todos


def write_todos(todos_arg, filename=FILEPATH):
    """Write the to-do items list to the text file."""
    with open(filename, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())