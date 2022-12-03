from aoc.day_three import day_three


def test_get_priority_of_line():
    input_line = "aa"

    expected_priority = 1

    actual = day_three.get_priority_of_line(input_line)

    assert actual == expected_priority


def test_get_group_priority():
    group = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
    ]
    expected_priority = 18

    actual = day_three.get_priority_for_group(group)

    assert actual == expected_priority


def test_get_sum_of_group_priorities():
    lines = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]
    expected_priority = 70

    actual = day_three.get_sum_of_group_priorities(lines)

    assert actual == expected_priority


def test_get_sum_of_priorities():
    lines = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]

    expected_sum = 157

    actual = day_three.get_sum_of_priorities(lines)

    assert actual == expected_sum
