from aoc.utilities.utils import read_input_file_as_array_of_strings


def convert_string_range_to_list(range_to_convert: str) -> list[str]:
    range_start, range_end = range_to_convert.split("-")
    return list(range(int(range_start), int(range_end) + 1))


def convert_string_ranges_to_lists(
    ranges_to_convert: str,
) -> list[list[int], list[int]]:
    first_range_str, second_range_str = ranges_to_convert.split(",")

    first_range = convert_string_range_to_list(first_range_str)
    second_range = convert_string_range_to_list(second_range_str)

    return [first_range, second_range]


def find_wholly_overlapping_ranges(ranges: list[str]) -> int:
    ranges_as_list = [convert_string_ranges_to_lists(range) for range in ranges]

    number_of_wholly_overlapping_ranges = 0
    for range_one, range_two in ranges_as_list:
        if set(range_one).issubset(set(range_two)) or set(range_two).issubset(
            set(range_one)
        ):
            number_of_wholly_overlapping_ranges += 1

    return number_of_wholly_overlapping_ranges


def find_any_overlaps(ranges: list[str]) -> int:
    ranges_as_list = [convert_string_ranges_to_lists(range) for range in ranges]

    number_of_overlaps = 0
    for range_one, range_two in ranges_as_list:
        overlap_found = False
        for i, j in zip(range_one, range_two):
            if overlap_found:
                break
            if (i in range_two) or (j in range_one):
                number_of_overlaps += 1
                overlap_found = True
    return number_of_overlaps


def main():
    file_to_use = "./aoc/day_four/input.txt"
    ranges_as_strings = read_input_file_as_array_of_strings(file_to_use)

    print("OVERLAPPING", find_wholly_overlapping_ranges(ranges_as_strings))
    print("ANY OVERLAPS", find_any_overlaps(ranges_as_strings))


if __name__ == "__main__":
    main()
