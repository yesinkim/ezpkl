"""Make your life simply"""
import inspect
import random
from typing import Union

from ezpkl.refrigerator import ingredients


def save_txt(data, file_name: str = None, separator: str = "\n") -> None:
    """Saves data to a text file.

    Args:
        data: The data to be saved. Can be a string, list, or any other object that can be converted to a string.
        file_name: The name of the text file. If not provided, the function attempts to determine the variable name from the previous frame's local variables.
        separator: The separator to use between items in a list. Defaults to "\n", which means items will be joined with a newline character.

    Returns:
        None

    Raises:
        FileNotFoundError: If the file cannot be found.
        PermissionError: If there is a permission error while saving the file.
    """
    var_name = None
    frame = inspect.currentframe()
    try:
        if not file_name:
            previous_frame = frame.f_back
            for name, value in previous_frame.f_locals.items():
                if value is data:
                    var_name = name
                    break
            if var_name:
                file_name = f"{var_name}.txt"
            else:
                file_name = f"{random.choice(ingredients)}.txt"
                print("I couldn't find the variable name, but here's some ingredient for you instead!")
        elif not file_name.endswith(".txt"):
            file_name = f"{file_name}.txt"

        try:
            with open(file_name, "w") as file:
                if isinstance(data, list):
                    if separator is None:
                        file.write("".join(str(item) for item in data))
                    else:
                        file.write(separator.join(str(item) for item in data))
                else:
                    file.write(str(data))
            print(f"Data saved to '{file_name}'.")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error saving data: {str(e)}")
    finally:
        del frame


def load_txt(filename: str) -> Union[str, None]:
    """Loads data from a text file.

    Args:
        filename: The name of the text file.

    Returns:
        The data loaded from the file, or None if the file is not found.

    Raises:
        FileNotFoundError: If the file cannot be found.
    """
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None
