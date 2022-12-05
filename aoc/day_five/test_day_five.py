from aoc.day_five import day_five


def test_get_top_for_all_stacks():
    stack_one = ["Z", "N"]
    stack_two = ["M", "C", "D"]
    stack_three = ["P"]
    stack_by_name = {
        "1": stack_one,
        "2": stack_two,
        "3": stack_three,
    }

    expected_top = "NDP"

    actual = day_five.get_top_for_all_stacks(stack_by_name)

    assert actual == expected_top


def test_run_through_instructions():
    stack_one = ["Z", "N"]
    stack_two = ["M", "C", "D"]
    stack_three = ["P"]
    stack_by_name = {
        "1": stack_one,
        "2": stack_two,
        "3": stack_three,
    }

    instructions = [
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2",
    ]

    day_five.run_all_instructions(stack_by_name, instructions)

    assert stack_one == ["C"]
    assert stack_two == ["M"]
    assert stack_three == ["P", "D", "N", "Z"]


def test_parse_instruction():
    input_instruction = "move 11 from 22 to 33"

    expected_moves = 11
    expected_from = "22"
    expected_to = "33"

    actual_moves, actual_from, actual_to = day_five.parse_instruction(input_instruction)
    print(actual_moves, actual_from, actual_to)
    assert actual_moves == expected_moves
    assert actual_from == expected_from
    assert actual_to == expected_to


def test_move_stack_part_one():
    stack_one = ["Z", "N"]
    stack_two = ["M", "C", "D"]
    stack_three = ["P"]
    stack_by_name = {
        "1": stack_one,
        "2": stack_two,
        "3": stack_three,
    }

    moves = 1
    stack_from = "2"
    stack_to = "1"

    day_five.move_stack_part_one(stack_by_name, moves, stack_from, stack_to)

    assert stack_one == ["Z", "N", "D"]
    assert stack_two == ["M", "C"]
    assert stack_three == ["P"]


def test_move_stack_part_two():
    stack_one = ["Z", "N", "D"]
    stack_two = ["M", "C"]
    stack_three = ["P"]
    stack_by_name = {
        "1": stack_one,
        "2": stack_two,
        "3": stack_three,
    }

    moves = 3
    stack_from = "1"
    stack_to = "3"

    day_five.move_stack_part_two(stack_by_name, moves, stack_from, stack_to)

    assert stack_one == []
    assert stack_two == ["M", "C"]
    assert stack_three == [
        "P",
        "Z",
        "N",
        "D",
    ]
