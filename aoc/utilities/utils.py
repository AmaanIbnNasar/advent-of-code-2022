def read_input_file_as_array_of_strings(filename: str) -> list[str]:
    with open(filename, "r") as file:
        lines = file.readlines()
        return [line.replace("\n", "") for line in lines]
