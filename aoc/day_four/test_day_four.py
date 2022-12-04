from aoc.day_four import day_four


def test_convert_string_ranges_to_lists():
    input_range = "2-4,6-8"

    expected_lists = [[2, 3, 4], [6, 7, 8]]

    actual = day_four.convert_string_ranges_to_lists(input_range)

    assert actual == expected_lists


def test_convert_string_range_to_list():
    input_range = "2-4"

    expected_list = [2, 3, 4]

    actual = day_four.convert_string_range_to_list(input_range)

    assert actual == expected_list


def test_convert_string_range_to_list__long_range():
    input_range = "4-98"

    expected_list = [i for i in range(4, 99)]

    actual = day_four.convert_string_range_to_list(input_range)

    assert actual == expected_list


def test_find_wholly_overlapping_ranges():
    ranges = ["2-4,6-8", "2-3,4-5", "5-7,7-9", "2-8,3-7", "6-6,4-6", "2-6,4-8"]

    expected_overlapping_ranges = 2

    actual = day_four.find_wholly_overlapping_ranges(ranges)

    assert actual == expected_overlapping_ranges


def test_find_any_overlaps():
    ranges = ["2-4,6-8", "2-3,4-5", "5-7,7-9", "2-8,3-7", "6-6,4-6", "2-6,4-8"]

    expected_overlapping_ranges = 4
    actual = day_four.find_any_overlaps(ranges)
    assert actual == expected_overlapping_ranges
