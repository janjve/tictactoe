import re

from rich.console import Console
from rich.table import Table
from rich import box
from rich.text import Text

from typing import Optional, List, Tuple


Board = List[List[Optional[int]]]
console = Console()

def show_board(board: Board):
    console.clear()
    table = Table(show_header=False, show_lines=True)

    # table.add_row("1", justify="right", style="cyan", no_wrap=True)
    placeholders = "789456123"
    i = 0
    for row in board:
        table_row_content = []
        for cell in row:
            if cell is None:
                text = Text(f"{placeholders[i]}")
                text.stylize("grey3", 0, 1)
            elif cell == 0:
                text = Text("X")
                text.stylize("bold green", 0, 1)
            elif cell == 1:
                text = Text("O")
                text.stylize("bold magenta", 0, 1)

            table_row_content.append(text)
            i += 1
        table.add_row(*table_row_content)


    console.print(table)




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


def try_parse_input(board: Board, input_str: str) -> Optional[Tuple[int, int]]:
    key_map = {
        '7': (0,0),
        '8': (0,1),
        '9': (0,2),
        '4': (1,0),
        '5': (1,1),
        '6': (1,2),
        '1': (2,0),
        '2': (2,1),
        '3': (2,2),
    }

    move = key_map.get(input_str)

    # invalid if not single digit
    if move is None or not is_valid_move(board, *move):
        return None

    return move


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
            input_str = input(f"Player {current_player} make a move: ")
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
