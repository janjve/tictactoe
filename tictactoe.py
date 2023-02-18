import random
import re

from rich.console import Console
from rich.table import Table
from rich import box
from rich.text import Text

from typing import Optional, List, Tuple
import game
import ai


console = Console()

def display_board(board: game.Board):
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


def try_parse_input(board: game.Board, input_str: str) -> Optional[Tuple[int, int]]:
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
    if move is None or not game.is_valid_move(board, *move):
        return None

    return move

def main_pve():
    board = game.init_board()
    cell_count = len(board) * len(board[0])

    i = 0
    prev_player = 0
    current_player = game.next_player(prev_player)
    computer_player = [current_player, prev_player][random.randint(0, 1)]

    while not game.is_winner(board, prev_player) and i < cell_count:
        display_board(board)
        row, col = -1, -1

        if current_player == computer_player:
            row, col = ai.random_ai(board, computer_player)
        else:
            while True:
                input_str = input(f"Player {current_player} make a move: ")
                parsed_input = try_parse_input(board, input_str)
                if parsed_input is not None:
                    row, col = parsed_input
                    break
                else:
                    print(f"invalid input '{input_str}'. Try again.")

        game.make_move(board, row, col, current_player)

        prev_player, current_player = current_player, game.next_player(current_player)

        i += 1
    
    display_board(board)
    if game.is_winner(board, computer_player):
        print("Sorry you lost! :(")
    else:
        print("You won!")


def main_pvp():
    board = game.init_board()
    cell_count = len(board) * len(board[0])

    i = 0
    prev_player = 0
    current_player = game.next_player(prev_player)

    while not game.is_winner(board, prev_player) and i < cell_count:
        display_board(board)
        row, col = -1, -1

        while True:
            input_str = input(f"Player {current_player} make a move: ")
            parsed_input = try_parse_input(board, input_str)
            if parsed_input is not None:
                row, col = parsed_input
                break
            else:
                print(f"invalid input '{input_str}'. Try again.")

        game.make_move(board, row, col, current_player)

        prev_player, current_player = current_player, game.next_player(current_player)

        i += 1
    
    display_board(board)
    for player in [0, 1]:
        if game.is_winner(board, player):
            print(f"Player {player} won!")

def main():
    while True:
        main_pve()
        input()

if __name__ == "__main__":
    SystemExit(main())
