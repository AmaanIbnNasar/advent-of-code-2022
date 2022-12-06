from aoc.day_six import day_six


def test_get_location_of_four_characters__one():
    input_string = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    expected_location = 7

    actual = day_six.get_location_of_four_characters(input_string)

    assert actual == expected_location


def test_get_location_of_four_characters__two():
    input_string = "bvwbjplbgvbhsrlpgdmjqwftvncz"
    expected_location = 5

    actual = day_six.get_location_of_four_characters(input_string)

    assert actual == expected_location


def test_get_location_of_four_characters__three():
    input_string = "nppdvjthqldpwncqszvftbrmjlhg"
    expected_location = 6

    actual = day_six.get_location_of_four_characters(input_string)

    assert actual == expected_location


def test_get_location_of_four_characters__four():
    input_string = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
    expected_location = 10

    actual = day_six.get_location_of_four_characters(input_string)

    assert actual == expected_location


def test_get_location_of_four_characters__five():
    input_string = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
    expected_location = 11

    actual = day_six.get_location_of_four_characters(input_string)

    assert actual == expected_location


def test_get_location_of_fourteen_characters__one():
    input_string = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    expected_location = 19

    actual = day_six.get_location_of_fourteen_characters(input_string)

    assert actual == expected_location


def test_get_location_of_fourteen_characters__two():
    input_string = "bvwbjplbgvbhsrlpgdmjqwftvncz"
    expected_location = 23

    actual = day_six.get_location_of_fourteen_characters(input_string)

    assert actual == expected_location


def test_get_location_of_fourteen_characters__three():
    input_string = "nppdvjthqldpwncqszvftbrmjlhg"
    expected_location = 23

    actual = day_six.get_location_of_fourteen_characters(input_string)

    assert actual == expected_location


def test_get_location_of_fourteen_characters__four():
    input_string = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
    expected_location = 29

    actual = day_six.get_location_of_fourteen_characters(input_string)

    assert actual == expected_location


def test_get_location_of_fourteen_characters__five():
    input_string = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
    expected_location = 26

    actual = day_six.get_location_of_fourteen_characters(input_string)

    assert actual == expected_location
