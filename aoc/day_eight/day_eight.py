from typing import Union
from pprint import pprint
from aoc.utilities.utils import read_input_file_as_array_of_strings
import re


def create_tree(height: int, x: int, y: int) -> str:
    return f"{height} - ({x}, {y})"


def get_trees(lines: list[str]) -> dict[str, dict[str, str]]:
    trees = {}
    for tree_y_pos, line_of_trees in enumerate(lines):
        for tree_x_pos, height_of_tree in enumerate(line_of_trees):
            new_tree = create_tree(height_of_tree, tree_x_pos, tree_y_pos)
            trees[new_tree] = {"R": None, "L": None, "D": None, "U": None}
            if tree_x_pos < len(line_of_trees) - 1:
                right_tree = create_tree(
                    int(line_of_trees[tree_x_pos + 1]), tree_x_pos + 1, tree_y_pos
                )
                trees[new_tree]["R"] = right_tree
            if tree_x_pos > 0:
                left_tree = create_tree(
                    int(line_of_trees[tree_x_pos - 1]), tree_x_pos - 1, tree_y_pos
                )
                trees[new_tree]["L"] = left_tree
            if tree_y_pos < len(lines) - 1:
                down_tree = create_tree(
                    int(lines[tree_y_pos + 1][tree_x_pos]), tree_x_pos, tree_y_pos + 1
                )
                trees[new_tree]["D"] = down_tree
            if tree_y_pos > 0:
                up_tree = create_tree(
                    int(lines[tree_y_pos - 1][tree_x_pos]), tree_x_pos, tree_y_pos - 1
                )
                trees[new_tree]["U"] = up_tree

    # pprint(trees)
    return trees


OPPOSITE_TREE_DIRECTIONS = {"R": "L", "L": "R", "U": "D", "D": "U"}


def get_number_visible_trees(trees: dict[str, dict[str, str]]) -> int:
    number_of_visible_trees = 0
    visible_trees = set()
    for tree, neighbours in trees.items():
        if (
            (neighbours["R"] is None)
            or (neighbours["L"] is None)
            or (neighbours["D"] is None)
            or (neighbours["U"] is None)
        ):
            number_of_visible_trees += 1
            visible_trees.add(tree)
    for tree, neighbours in trees.items():
        visibility, direction = check_tree_visibility(tree, neighbours, visible_trees)
        if (visibility) and (tree not in visible_trees):
            number_of_visible_trees += 1
            visible_trees.add(tree)

    return number_of_visible_trees


def check_tree_visibility(
    tree: str, neighbours: dict[str, str], visible_trees
) -> tuple[bool, Union[str, None]]:
    height, x, y = get_height_and_position_from_tree(tree)
    for direction, neighbour in neighbours.items():
        if neighbour != None:
            neigh_height, neigh_x, neigh_y = get_height_and_position_from_tree(
                neighbour
            )
            if (neigh_height < height) and (neighbour in visible_trees):
                return True, direction
    return False, None


def get_height_and_position_from_tree(tree: str) -> tuple[int, int, int]:
    height_to_parse = re.findall(r"\d+ -", tree)
    position_to_parse = re.findall(r"\d+, \d+", tree)
    if height_to_parse:
        height = int(height_to_parse[0].split(" ")[0])
    if position_to_parse:
        x, y = position_to_parse[0].split(", ")

    return height, int(x), int(y)


def main():
    filename = "./aoc/day_eight/input.txt"
    lines = read_input_file_as_array_of_strings(filename)
    visible_trees = 0
    height = len(lines)
    width = len(lines[0])
    scenic_scores = []
    for i in range(1, len(lines) - 1):
        for j in range(1, len(lines[i]) - 1):
            tree_to_check = int(lines[i][j])
            right_trees = []
            left_trees = []
            down_trees = []
            up_trees = []
            if (j == 2) and (i == 3):
                print("THIS ONE")
            for k in range(j + 1, len(lines[i])):
                right_trees.append(int(lines[i][k]))
            for l in range(j - 1, -1, -1):
                left_trees.append(int(lines[i][l]))
            for m in range(i + 1, len(lines)):
                down_trees.append(int(lines[m][j]))
            for o in range(i - 1, -1, -1):
                up_trees.append(int(lines[o][j]))
            right_score = 0
            for right in right_trees:
                if right <= tree_to_check:
                    right_score += 1
                    if right == tree_to_check:
                        break
                else:
                    right_score += 1
                    break
            left_score = 0
            for left in left_trees:
                if left <= tree_to_check:
                    left_score += 1
                    if left == tree_to_check:
                        break
                else:
                    left_score += 1
                    break
            up_score = 0
            for up in up_trees:
                if up <= tree_to_check:
                    up_score += 1
                    if up == tree_to_check:
                        break
                else:
                    up_score += 1
                    break
            down_score = 0
            for down in down_trees:
                if down <= tree_to_check:
                    down_score += 1
                    if down == tree_to_check:
                        break
                else:
                    down_score += 1
                    break
            scenic_scores.append(right_score * left_score * up_score * down_score)
            if (right_trees) and (max(right_trees) < tree_to_check):
                visible_trees += 1
                continue
            if (left_trees) and (max(left_trees) < tree_to_check):
                visible_trees += 1
                continue
            if (down_trees) and (max(down_trees) < tree_to_check):
                visible_trees += 1
                continue
            if (up_trees) and (max(up_trees) < tree_to_check):
                visible_trees += 1
                continue

    # trees = get_trees(lines)
    sides = ((height + width) * 2) - 4
    # visible_trees = get_number_visible_trees(trees)
    print("TREES", visible_trees + sides)
    print("MAX SCENIC", max(scenic_scores))


if __name__ == "__main__":
    main()
