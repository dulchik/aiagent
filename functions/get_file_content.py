import os


def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.join(working_directory, file_path)

    if not os.path.abspath(file_path).startswith(abs_working_dir):
        f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        MAX_CHARS = 10000

        with open(target_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)
        
        if len(file_content_string) == MAX_CHARS:
            file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'
        
        return file_content_string
    except Exception as e:
        return f"Error: {e}"
