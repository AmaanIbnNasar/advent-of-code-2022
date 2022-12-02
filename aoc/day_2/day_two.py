def read_input_file_as_array_of_strings(filename: str) -> list[str]:
    with open(filename, "r") as file:
        lines = file.readlines()
        return [line.replace("\n", "") for line in lines]


move_by_alpha_coding = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
}
required_outcome_by_alpha_coding = {"X": "loss", "Y": "draw", "Z": "win"}

score_by_move = {"Rock": 1, "Paper": 2, "Scissors": 3}

round_outcome_score_by_outcome = {"loss": 0, "draw": 3, "win": 6}
loss_move_by_move = {"Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock"}
win_move_by_move = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}


def calculate_my_outcome_from_moves(opponent_move: str, my_move: str) -> str:
    if opponent_move == loss_move_by_move[my_move]:
        return "loss"
    elif opponent_move == my_move:
        return "draw"
    else:
        return "win"


def calculate_my_move_from_outcome_and_opponent(
    opponent_move: str, required_outcome: str
):
    if required_outcome == "loss":
        return win_move_by_move[opponent_move]
    elif required_outcome == "win":
        return loss_move_by_move[opponent_move]
    else:
        return opponent_move


def calculate_score_of_strategy(input_strategy):
    split_strategy = input_strategy.split(" ")
    opponent_move = move_by_alpha_coding[split_strategy[0]]
    my_move = move_by_alpha_coding[split_strategy[1]]

    outcome = calculate_my_outcome_from_moves(opponent_move, my_move)

    move_score = score_by_move[my_move]
    outcome_score = round_outcome_score_by_outcome[outcome]

    return move_score + outcome_score


def calculate_score_of_strategy_part_two(input_strategy: str) -> int:
    split_strategy = input_strategy.split(" ")
    opponent_move = move_by_alpha_coding[split_strategy[0]]
    required_outcome = required_outcome_by_alpha_coding[split_strategy[1]]

    my_move = calculate_my_move_from_outcome_and_opponent(
        opponent_move, required_outcome
    )

    move_score = score_by_move[my_move]
    outcome_score = round_outcome_score_by_outcome[required_outcome]

    return move_score + outcome_score


def main():
    file_to_use = "input.txt"
    strategy_guide = read_input_file_as_array_of_strings(file_to_use)
    total_score = 0
    total_score_part_two = 0
    for round in strategy_guide:
        total_score += calculate_score_of_strategy(round)
        total_score_part_two += calculate_score_of_strategy_part_two(round)

    print("TOTAL SCORE", total_score)
    print("TOTAL SCORE PART TWO", total_score_part_two)


if __name__ == "__main__":
    main()
