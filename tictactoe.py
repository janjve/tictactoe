import re

from typing import Optional, List, Tuple


Board = List[List[Optional[int]]]


def show_board(board: Board):
    for row in board:
        print(*row)


def init_board() -> Board:
    return [[None] * 3 for _ in range(3)]


def make_move(board: Board, row: int, col: int, player: int):
    board[row][col] = player


def is_winner(board, player):
    n = len(board)

    for row in board:
        if all(cell == player for cell in row):
            return True

    for col_idx in range(n):
        if all(row[col_idx] == player for row in board):
            return True

    # diagonal descending
    if all(board[idx][idx] == player for idx in range(n)):
        return True

    # diagonal ascending
    if all(board[idx][idx] == player for idx in range(n - 1, -1, -1)):
        return True

    return False


def next_player(current_player: int):
    # player 0 and player 1
    return 1 - current_player


def is_valid_move(board: Board, row: int, col: int) -> bool:
    n = len(board)
    return 0 <= row < n and 0 <= col < n and board[row][col] is None


def try_parse_input(board: Board, input_str: str) -> Optional[Tuple[int, int]]:
    # invalid if not exactly two integers
    if not re.match(r"^\d\d$", input_str):
        return None

    # cast to integers
    row, col = [int(x) for x in input_str]

    if not is_valid_move(board, row, col):
        return None

    return row, col


def main():
    board = init_board()
    cell_count = len(board) * len(board[0])

    i = 0
    prev_player = 0
    current_player = next_player(prev_player)

    while not is_winner(board, prev_player) and i < cell_count:
        show_board(board)
        row, col = -1, -1

        while True:
            input_str = input(f"Make a move player {current_player}: ")
            parsed_input = try_parse_input(board, input_str)
            if parsed_input is not None:
                row, col = parsed_input
                break
            else:
                print(f"invalid input '{input_str}'. Try again.")

        make_move(board, row, col, current_player)

        prev_player, current_player = current_player, next_player(current_player)

        i += 1

    show_board(board)
    for player in [0, 1]:
        if is_winner(board, player):
            print(f"Player {player} won!")


if __name__ == "__main__":
    SystemExit(main())
