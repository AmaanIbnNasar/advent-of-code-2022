from aoc.day_eight import day_eight as e


def test_get_trees():
    lines = ["12", "34"]
    expected_trees = {
        "1 - (0, 0)": {"R": "2 - (1, 0)", "L": None, "D": "3 - (0, 1)", "U": None},
        "2 - (1, 0)": {"R": None, "L": "1 - (0, 0)", "D": "4 - (1, 1)", "U": None},
        "3 - (0, 1)": {"R": "4 - (1, 1)", "L": None, "D": None, "U": "1 - (0, 0)"},
        "4 - (1, 1)": {"R": None, "L": "3 - (0, 1)", "D": None, "U": "2 - (1, 0)"},
    }

    actual_trees = e.get_trees(lines)

    assert actual_trees == expected_trees


def test_get_height_and_position_from_tree():
    tree = "929 - (23, 50)"

    expected_height = 929
    expected_x = 23
    expected_y = 50

    actual_height, actual_x, actual_y = e.get_height_and_position_from_tree(tree)

    assert actual_height == expected_height
    assert actual_x == expected_x
    assert actual_y == expected_y


def test_get_number_visible_trees__outer_trees():
    trees = {
        "1 - (0, 0)": {"R": "2 - (1, 0)", "L": None, "D": "3 - (0, 1)", "U": None},
        "2 - (1, 0)": {"R": None, "L": "1 - (0, 0)", "D": "4 - (1, 1)", "U": None},
        "3 - (0, 1)": {"R": "4 - (1, 1)", "L": None, "D": None, "U": "1 - (0, 0)"},
        "4 - (1, 1)": {"R": None, "L": "3 - (0, 1)", "D": None, "U": "2 - (1, 0)"},
    }

    expected_visible_trees = 4

    actual = e.get_number_visible_trees(trees)

    assert actual == expected_visible_trees


def test_check_tree_visibility__visible():
    neighbours = {
        "R": "1 - (0, 0)",
        "L": "99 - (0, 0)",
        "D": "99 - (0, 0)",
        "U": "99 - (0, 0)",
    }
    tree = "5 - (0, 0)"

    expected_direction = "R"
    expected_visibility = True

    actual_visibility, actual_direction = e.check_tree_visibility(
        tree, neighbours, set(["1 - (0, 0)"])
    )

    assert actual_visibility == expected_visibility
    assert actual_direction == expected_direction


def test_check_tree_visibility__not_visible():
    neighbours = {
        "R": "99 - (0, 0)",
        "L": "99 - (0, 0)",
        "D": "99 - (0, 0)",
        "U": "99 - (0, 0)",
    }
    tree = "5 - (0, 0)"

    expected_visibility = False
    expected_direction = None
    actual_visibility, actual_direction = e.check_tree_visibility(
        tree, neighbours, set()
    )

    assert actual_visibility == expected_visibility
    assert actual_direction == expected_direction


def test_get_number_visible_trees__more_trees():
    trees = {
        "0 - (1, 0)": {
            "D": "5 - (1, 1)",
            "L": "3 - (0, 0)",
            "R": "3 - (2, 0)",
            "U": None,
        },
        "0 - (4, 4)": {"D": None, "L": "9 - (3, 4)", "R": None, "U": "9 - (4, 3)"},
        "1 - (3, 1)": {
            "D": "3 - (3, 2)",
            "L": "5 - (2, 1)",
            "R": "2 - (4, 1)",
            "U": "7 - (3, 0)",
        },
        "2 - (0, 1)": {
            "D": "6 - (0, 2)",
            "L": None,
            "R": "5 - (1, 1)",
            "U": "3 - (0, 0)",
        },
        "2 - (4, 1)": {
            "D": "2 - (4, 2)",
            "L": "1 - (3, 1)",
            "R": None,
            "U": "3 - (4, 0)",
        },
        "2 - (4, 2)": {
            "D": "9 - (4, 3)",
            "L": "3 - (3, 2)",
            "R": None,
            "U": "2 - (4, 1)",
        },
        "3 - (0, 0)": {"D": "2 - (0, 1)", "L": None, "R": "0 - (1, 0)", "U": None},
        "3 - (0, 3)": {
            "D": "3 - (0, 4)",
            "L": None,
            "R": "3 - (1, 3)",
            "U": "6 - (0, 2)",
        },
        "3 - (0, 4)": {"D": None, "L": None, "R": "5 - (1, 4)", "U": "3 - (0, 3)"},
        "3 - (1, 3)": {
            "D": "5 - (1, 4)",
            "L": "3 - (0, 3)",
            "R": "5 - (2, 3)",
            "U": "5 - (1, 2)",
        },
        "3 - (2, 0)": {
            "D": "5 - (2, 1)",
            "L": "0 - (1, 0)",
            "R": "7 - (3, 0)",
            "U": None,
        },
        "3 - (2, 2)": {
            "D": "5 - (2, 3)",
            "L": "5 - (1, 2)",
            "R": "3 - (3, 2)",
            "U": "5 - (2, 1)",
        },
        "3 - (2, 4)": {
            "D": None,
            "L": "5 - (1, 4)",
            "R": "9 - (3, 4)",
            "U": "5 - (2, 3)",
        },
        "3 - (3, 2)": {
            "D": "4 - (3, 3)",
            "L": "3 - (2, 2)",
            "R": "2 - (4, 2)",
            "U": "1 - (3, 1)",
        },
        "3 - (4, 0)": {"D": "2 - (4, 1)", "L": "7 - (3, 0)", "R": None, "U": None},
        "4 - (3, 3)": {
            "D": "9 - (3, 4)",
            "L": "5 - (2, 3)",
            "R": "9 - (4, 3)",
            "U": "3 - (3, 2)",
        },
        "5 - (1, 1)": {
            "D": "5 - (1, 2)",
            "L": "2 - (0, 1)",
            "R": "5 - (2, 1)",
            "U": "0 - (1, 0)",
        },
        "5 - (1, 2)": {
            "D": "3 - (1, 3)",
            "L": "6 - (0, 2)",
            "R": "3 - (2, 2)",
            "U": "5 - (1, 1)",
        },
        "5 - (1, 4)": {
            "D": None,
            "L": "3 - (0, 4)",
            "R": "3 - (2, 4)",
            "U": "3 - (1, 3)",
        },
        "5 - (2, 1)": {
            "D": "3 - (2, 2)",
            "L": "5 - (1, 1)",
            "R": "1 - (3, 1)",
            "U": "3 - (2, 0)",
        },
        "5 - (2, 3)": {
            "D": "3 - (2, 4)",
            "L": "3 - (1, 3)",
            "R": "4 - (3, 3)",
            "U": "3 - (2, 2)",
        },
        "6 - (0, 2)": {
            "D": "3 - (0, 3)",
            "L": None,
            "R": "5 - (1, 2)",
            "U": "2 - (0, 1)",
        },
        "7 - (3, 0)": {
            "D": "1 - (3, 1)",
            "L": "3 - (2, 0)",
            "R": "3 - (4, 0)",
            "U": None,
        },
        "9 - (3, 4)": {
            "D": None,
            "L": "3 - (2, 4)",
            "R": "0 - (4, 4)",
            "U": "4 - (3, 3)",
        },
        "9 - (4, 3)": {
            "D": "0 - (4, 4)",
            "L": "4 - (3, 3)",
            "R": None,
            "U": "2 - (4, 2)",
        },
    }

    expected_visible_trees = 21

    actual = e.get_number_visible_trees(trees)

    assert actual == expected_visible_trees
