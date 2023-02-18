from typing import Optional, List


Board = List[List[Optional[int]]]

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
    if all(board[idx][n - 1 - idx] == player for idx in range(n - 1, -1, -1)):
        return True

    return False


def next_player(current_player: int):
    # player 0 and player 1
    return 1 - current_player


def is_valid_move(board: Board, row: int, col: int) -> bool:
    n = len(board)
    return 0 <= row < n and 0 <= col < n and board[row][col] is None

