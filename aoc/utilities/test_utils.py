from .utils import read_input_file_as_array_of_strings


def test_read_input_file_as_array_of_strings():
    expected_array = ["1", "2", "3"]

    actual_array = read_input_file_as_array_of_strings("./aoc/utilities/test.txt")

    assert actual_array == expected_array
