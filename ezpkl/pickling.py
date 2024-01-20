"""Easy peasy lemon squeezy!🍋🤝🍸"""
import inspect
import pickle
import random

from ezpkl.refrigerator import ingredients

# TODO: add filename, folder opt
def save_pkl(var, file_name: str = None) -> None:
    """Saves a variable as a pickle file.

    Args:
        var: The variable to be saved as a pickle file.
        file_name: The name of the pickle file. If not provided, the function attempts to determine the variable name from the previous frame's local variables.

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
                if value is var:
                    var_name = name
                    break
            if var_name:
                file_name = f"{var_name}.pkl"
            else:
                
                file_name = f"{random.choice(ingredients)}.pkl"
                print(
                    "I couldn't find the variable name, but here's some ingredient for you instead!"
                )
        elif not file_name.endswith(".pkl"):
            file_name = f"{file_name}.pkl"

        try:
            with open(file_name, "wb") as file:
                pickle.dump(var, file)
            print(f"Variable '{file_name}' saved.")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error saving variable: {str(e)}")
    finally:
        del frame


def load_pkl(filename: str):
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None
