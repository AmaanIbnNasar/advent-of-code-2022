from typing import Union
import re
from aoc.utilities.utils import read_input_file_as_array_of_strings


def parse_all_lines(lines: list[str]):
    directories = {}
    files = {}
    hierarchy_of_directories = []
    current_directory = None
    for line in lines:
        if "$ cd" in line and (".." not in line):
            full_path = ",".join(hierarchy_of_directories)
            directory_name = f"{line[5:]} - {full_path}"
            if directory_name not in directories:
                directories[directory_name] = []
            current_directory = directory_name
            hierarchy_of_directories.append(current_directory)

        if "$ cd .." in line:
            current_directory = hierarchy_of_directories.pop()

        if "dir" in line:
            dir_name = line.split(" ")[1]
            full_path = ",".join(hierarchy_of_directories)
            directories[current_directory].append(f"{dir_name} - {full_path}")

        if re.match(r"\d+", line):
            filename = re.split(r"\d+", line)[1].strip()
            full_path = ",".join(hierarchy_of_directories)
            directories[current_directory].append(f"{filename} - {full_path}")
            files[f"{filename} - {full_path}"] = int(re.findall(r"\d+", line)[0])

    return directories, files


def find_total_size_of_directory(directories, files, directory_name):
    total_size_of_directory = 0
    for item in directories[directory_name]:
        if item in files:
            total_size_of_directory += files[item]
        else:
            total_size_of_directory += find_total_size_of_directory(
                directories, files, item
            )
    return total_size_of_directory


def main():
    filename = "./aoc/day_seven/input.txt"
    lines = read_input_file_as_array_of_strings(filename)
    directories, files = parse_all_lines(lines)

    total_size_by_directory = {}
    for dir_name in directories:
        total_size_by_directory[dir_name] = find_total_size_of_directory(
            directories, files, dir_name
        )
    correct_size_dirs = [
        size for size in total_size_by_directory.values() if size < 100000
    ]
    total_disk_space = 70000000
    space_required = 30000000
    current_space = total_size_by_directory["/ - "]
    unused_space = total_disk_space - current_space
    print(unused_space)
    # print(len(directories))
    # print(files)
    print(space_required - unused_space)
    dirs_to_delete = []
    for dir_size in total_size_by_directory.values():
        if unused_space + dir_size > space_required:
            dirs_to_delete.append(dir_size)
    # print(total_size_by_directory)
    print("CUR", current_space)
    print("DIRs", dirs_to_delete)
    print(min(dirs_to_delete))
    # print(sum(correct_size_dirs))


if __name__ == "__main__":
    main()
