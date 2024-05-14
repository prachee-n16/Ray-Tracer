def save_file_contents(filename: str, data: str) -> None:
    with open(filename, 'w') as file:
        file.write(data)