from aoc.utilities.utils import read_input_file_as_array_of_strings

priority_by_letter = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52,
}


def get_priority_of_line(line: str) -> int:

    lineLength = len(line)
    first_half_of_line = line[: int(lineLength / 2)]
    second_half_of_line = line[int(lineLength / 2) :]

    for letter in first_half_of_line:
        if letter in second_half_of_line:
            return priority_by_letter[letter]


def get_sum_of_priorities(lines: list[str]) -> int:
    priority_sum = 0
    for line in lines:
        priority_sum += get_priority_of_line(line)

    return priority_sum


def get_priority_for_group(lines: list[str]) -> int:
    line_one, line_two, line_three = lines
    for letter in line_one:
        if (letter in line_two) and (letter in line_three):
            return priority_by_letter[letter]


def get_sum_of_group_priorities(lines: list[str]) -> int:
    priority_sum = 0
    end_index = 3
    for i in range(0, len(lines) - 2, 3):
        print("PRIOR", get_priority_for_group(lines[i:end_index]))
        priority_sum += get_priority_for_group(lines[i:end_index])
        end_index += 3
    return priority_sum


def main():
    input_file = "./aoc/day_three/input.txt"
    lines = read_input_file_as_array_of_strings(input_file)
    priority_sum = get_sum_of_priorities(lines)
    priority_group_sum = get_sum_of_group_priorities(lines)
    print("PRIORITY", priority_sum)
    print("PRIORITY GROUP", priority_group_sum)


if __name__ == "__main__":
    main()
