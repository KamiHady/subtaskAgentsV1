import os


# A simpel function to open a file from a path/string
def load_file(path: str):
    with open(path, 'r') as file:
        file = file.read()
    return file


# A simple fucntion that saves a string as a markdown (md) file at a desired location
def save_as_md(filename: str, path: str, content: str):
    file_path = os.path.join(path, filename)
    with open(file_path, "w") as file:
        file.write(content)
