from aoc.day_seven import day_seven
from aoc.day_seven.day_seven import Directory, File


def test_parse_all_lines():
    lines = [
        "$ cd /",
        "$ ls",
        "dir a",
        "100 b.txt",
        "200 c.txt",
        "dir d",
        "$ cd a",
        "$ ls",
        "dir e",
        "300 f",
        "400 g",
        "500 h",
        "$ cd e",
        "$ ls",
        "600 i",
        "$ cd ..",
        "$ cd ..",
        "$ cd d",
        "$ ls",
        "700 j",
        "800 d.log",
        "900 d.ext",
        "1000 k",
    ]
    expected_directories = {"/": ["a", "b", "c", "d"], "a": [], "d": []}
    expected_files = {"b": 100, "c": 200}

    actual_directories = day_seven.parse_all_lines(lines)
    assert actual_directories == expected_directories


def test_parse_line__cd_directory():
    expected_directory = Directory("/", None, [])

    input_line = "$ cd /"

    actual_current, add_mode = day_seven.parse_line(input_line, None)

    assert add_mode == False
    assert actual_current == expected_directory


def test_parse_line__ls():
    expected_add_mode = True
    input_line = "$ ls"

    _, actual_add_mode = day_seven.parse_line(input_line, None)

    assert actual_add_mode == expected_add_mode


def test_parse_line__add_mode_true():
    input_line = "100 a.txt"
    current_directory = Directory("dir", None, [])

    expected_file = File("a.txt", 100)

    _, add_mode = day_seven.parse_line(input_line, current_directory, True)

    assert add_mode == True
    assert expected_file == current_directory.contents[0]
