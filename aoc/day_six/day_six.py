from aoc.utilities.utils import read_input_file_as_array_of_strings


def get_location_of_four_characters(input_string: str) -> int:
    for i in range(len(input_string)):
        four_characters = [
            input_string[i],
            input_string[i + 1],
            input_string[i + 2],
            input_string[i + 3],
        ]

        if len(set(four_characters)) == 4:
            return i + 4


def get_location_of_fourteen_characters(input_string: str) -> int:
    for i in range(len(input_string)):
        distinct_characters = [input_string[j] for j in range(i, i + 14)]

        if len(set(distinct_characters)) == 14:
            return i + 14


def main():
    input_file = "./aoc/day_six/input.txt"
    string_to_process = read_input_file_as_array_of_strings(input_file)[0]

    print("LOCATION", get_location_of_four_characters(string_to_process))
    print("LOCATION", get_location_of_fourteen_characters(string_to_process))


if __name__ == "__main__":
    main()
