import os


def move_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3 or command_parts[0] != "mv":
        return
    file_in = command_parts[1]
    file_path = command_parts[2]
    if file_path.endswith("/"):
        base_name = os.path.basename(file_in)
        file_path = os.path.join(file_path, base_name)
    if os.path.abspath(file_in) == os.path.abspath(file_path):
        return
    directory = os.path.dirname(file_path)
    if directory != "":
        os.makedirs(directory, exist_ok=True)
    with open(file_in, "r") as file, open(file_path, "w") as file_out:
        file_out.write(file.read())
    os.remove(file_in)
