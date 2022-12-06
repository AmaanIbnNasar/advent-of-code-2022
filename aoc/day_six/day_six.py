from aoc.utilities.utils import read_input_file_as_array_of_strings


def get_location_of_distinct_characters(
    input_string: str, num_distinct_characters: int
) -> int:
    for i in range(len(input_string)):
        distinct_characters = [
            input_string[j] for j in range(i, i + num_distinct_characters)
        ]

        if len(set(distinct_characters)) == num_distinct_characters:
            return i + num_distinct_characters


def main():
    input_file = "./aoc/day_six/input.txt"
    string_to_process = read_input_file_as_array_of_strings(input_file)[0]

    print("LOCATION", get_location_of_distinct_characters(string_to_process, 4))
    print("LOCATION", get_location_of_distinct_characters(string_to_process, 14))


if __name__ == "__main__":
    main()
