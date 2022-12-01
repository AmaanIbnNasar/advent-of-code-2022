def read_input_file_as_array(file_to_read: str) -> list[int]:
    with open(file_to_read, "r") as file:
        lines = file.readlines()
        return [
            int(line.replace("\n", "")) if line.replace("\n", "") != "" else -99
            for line in lines
        ]


def get_elf_calories_summed(array_of_calories: list[int]) -> list[int]:
    elves = []
    new_elf = []
    for i, n in enumerate(array_of_calories):
        if n == -99:
            elves.append(new_elf)
            new_elf = []
            continue
        new_elf.append(n)
        if i == len(array_of_calories) - 1:
            elves.append(new_elf)
    summed_elves = [sum(elf) for elf in elves]
    return summed_elves


def get_max_elf_calories(array_of_calories: list[int]) -> list[int]:
    summed_elves = get_elf_calories_summed(array_of_calories)
    return max(summed_elves)


def get_top_three_max_elf_calories(summed_elves: list[int]) -> list[int]:
    summed_elves.sort(reverse=True)
    return summed_elves[:3]


def main():
    input_file = "input.txt"
    array_of_calories = read_input_file_as_array(input_file)
    summed_elves = get_elf_calories_summed(array_of_calories)
    max_elf_calories = get_max_elf_calories(array_of_calories)
    print(sum(get_top_three_max_elf_calories(summed_elves)))


if __name__ == "__main__":
    main()
