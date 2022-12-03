from day_one.day1 import (
    read_input_file_as_array,
    get_max_elf_calories,
    get_elf_calories_summed,
)


def test_read_input_file_as_array():
    expected_array = [
        1000,
        2000,
        3000,
        -99,
        4000,
        -99,
        5000,
        6000,
        -99,
        7000,
        8000,
        9000,
        -99,
        10000,
    ]

    actual_array = read_input_file_as_array("./day_1/test.txt")

    assert actual_array == expected_array


def test_get_elf_calories_summed():
    input_array = [1, 2, 3, -99, 4, 5, 6]

    expected_array = [6, 15]

    actual_array = get_elf_calories_summed(input_array)

    assert actual_array == expected_array


def test_get_max_elf_calories__returns_the_sum_for_one_elf():
    input_array = [1, 2, 3]

    expected_calory = 6

    actual_array = get_max_elf_calories(input_array)

    assert actual_array == expected_calory


def test_get_max_elf_calories__returns_the_sum_for_multiple_elves():
    input_array = [1, 2, 3, -99, 4, 5, 6]

    expected_calory = 15

    actual_array = get_max_elf_calories(input_array)

    assert actual_array == expected_calory
