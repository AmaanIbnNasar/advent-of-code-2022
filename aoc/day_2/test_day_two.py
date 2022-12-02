from aoc.day_2.day_two import (
    calculate_score_of_strategy,
    calculate_my_outcome_from_moves,
    calculate_my_move_from_outcome_and_opponent,
    calculate_score_of_strategy_part_two,
)


def test_calculate_my_outcome_from_moves():
    opponent_move = "Rock"
    my_move = "Paper"

    expected_outcome = "win"

    actual_outcome = calculate_my_outcome_from_moves(opponent_move, my_move)

    assert actual_outcome == expected_outcome


def test_calculate_my_move_from_outcome_and_opponent():
    opponent_move = "Rock"
    required_outcome = "loss"

    expected_move = "Scissors"

    actual_move = calculate_my_move_from_outcome_and_opponent(
        opponent_move, required_outcome
    )

    assert actual_move == expected_move


def test_calculate_score_of_strategy_part_two():
    input_strategy = "A Y"

    expected_score = 4

    actual_score = calculate_score_of_strategy_part_two(input_strategy)

    assert actual_score == expected_score


def test_calulate_score_of_strategy():
    input_strategy = "A Y"

    expected_score = 8

    actual_score = calculate_score_of_strategy(input_strategy)

    assert actual_score == expected_score
