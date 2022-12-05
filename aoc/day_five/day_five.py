import re
from aoc.utilities.utils import read_input_file_as_array_of_strings


def get_top_for_all_stacks(stack_by_name: dict[str, list[str]]) -> str:
    top = ""
    for stack in stack_by_name.values():
        top += stack[-1]
    return top


def run_all_instructions(
    stack_by_name: dict[str, list[str]], instructions: list[str]
) -> None:
    for instruction in instructions:
        moves, stack_from, stack_to = parse_instruction(instruction)

        move_stack_part_two(stack_by_name, moves, stack_from, stack_to)


def move_stack_part_one(
    stack_by_name: dict[str, list[str]], moves: int, stack_from: str, stack_to: str
):
    for _ in range(moves):
        popped = stack_by_name[stack_from].pop()
        stack_by_name[stack_to].append(popped)


def move_stack_part_two(
    stack_by_name: dict[str, list[str]], moves: int, stack_from: str, stack_to: str
):
    crates_to_be_moved = []
    for _ in range(moves):
        crates_to_be_moved.append(stack_by_name[stack_from].pop())
    crates_to_be_moved.reverse()
    stack_by_name[stack_to].extend(crates_to_be_moved)


def parse_instruction(instruction: str):
    moves = re.search(r"move \d+", instruction)
    stack_from = re.search(r"from \d+", instruction)
    stack_to = re.search(r"to \d+", instruction)
    if moves and stack_from and stack_to:
        parsed_moves = int(moves.group().split(" ")[1])
        parsed_from = stack_from.group().split(" ")[1]
        parsed_to = stack_to.group().split(" ")[1]
        return parsed_moves, parsed_from, parsed_to
    raise ValueError("SOMETHING WENT WRONG")


def test_data():
    stack_one = ["Z", "N"]
    stack_two = ["M", "C", "D"]
    stack_three = ["P"]

    stack_by_name = {"1": stack_one, "2": stack_two, "3": stack_three}

    instructions = [
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2",
    ]
    return stack_by_name, instructions


def input_data():
    stack_by_name = {
        "1": ["G", "F", "V", "H", "P", "S"],
        "2": ["G", "J", "F", "B", "V", "D", "Z", "M"],
        "3": ["G", "M", "L", "J", "N"],
        "4": ["N", "G", "Z", "V", "D", "W", "P"],
        "5": ["V", "R", "C", "B"],
        "6": ["V", "R", "S", "M", "P", "W", "L", "Z"],
        "7": ["T", "H", "P"],
        "8": ["Q", "R", "S", "N", "C", "H", "Z", "V"],
        "9": ["F", "L", "G", "P", "V", "Q", "J"],
    }

    instructions = read_input_file_as_array_of_strings("./aoc/day_five/input.txt")[10:]
    return stack_by_name, instructions


def main():
    stack_by_name, instructions = input_data()

    run_all_instructions(stack_by_name, instructions)
    print(get_top_for_all_stacks(stack_by_name))


if __name__ == "__main__":
    main()
