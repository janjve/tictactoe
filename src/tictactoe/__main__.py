import random
from rich.console import Console
from rich.table import Table
from rich import box
from rich.text import Text

from typing import Optional, List, Tuple
from tictactoe import game, ai


console = Console()

def display_board(board: game.Board):
    console.clear()
    table = Table(show_header=False, show_lines=True)
    if len(board) == 3:
        placeholders = "789456123"
    elif len(board) == 4:
        placeholders = "1234qwerasdfzxcv"
    
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
    if len(board) == 3:
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
    elif len(board) == 4:
        key_map = {
            '1': (0,0),
            '2': (0,1),
            '3': (0,2),
            '4': (0,3),
            'q': (1,0),
            'w': (1,1),
            'e': (1,2),
            'r': (1,3),
            'a': (2,0),
            's': (2,1),
            'd': (2,2),
            'f': (2,3),
            'z': (3,0),
            'x': (3,1),
            'c': (3,2),
            'v': (3,3),
        }

    move = key_map.get(input_str)

    # invalid if not single digit
    if move is None or not board.is_valid_move(*move):
        return None

    return move


def main_pve(n):
    ai_player = ai.minimax
    board = game.Board(n)
    cell_count = len(board) * len(board[0])

    i = 0
    prev_player = 0
    current_player = board.next_player(prev_player)
    players = [prev_player, current_player]
    random.shuffle(players)
    ai_player_id, human_player_id = players

    while board.winner() is None and i < cell_count:
        display_board(board)
        row, col = -1, -1

        if current_player == ai_player_id:
            row, col = ai_player(board, ai_player_id)
        else:
            while True:
                input_str = input(f"Player {current_player} make a move: ")
                parsed_input = try_parse_input(board, input_str)
                if parsed_input is not None:
                    row, col = parsed_input
                    break
                else:
                    print(f"invalid input '{input_str}'. Try again.")

        board.make_move(row, col, current_player)

        prev_player, current_player = current_player, board.next_player(current_player)

        i += 1
    
    display_board(board)
    winner = board.winner()
    if winner == ai_player_id:
        print("Sorry you lost! :(")
    elif winner == human_player_id:
        print("You won!")
    else:
        print("Draw :|")


def main_pvp(n):
    board = game.Board(n)
    cell_count = len(board) * len(board[0])

    i = 0
    prev_player = 0
    current_player = board.next_player(prev_player)

    while board.winner() is None and i < cell_count:
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

        board.make_move(row, col, current_player)

        prev_player, current_player = current_player, board.next_player(current_player)

        i += 1
    
    display_board(board)
    winner = board.winner()
    if winner is not None:
        print(f"Player {winner} won!")
    else:
        print("It was a draw")



def main():
    while True:
        mode = ''
        while mode not in ['e3', 'e4', 'p3', 'p4']:
            mode = input("What PvX game-mode on board NxN would you like? [E3/e4/p3/p4] ")
            mode = mode.strip().lower()
            if not mode:
                mode = 'e3'
                
        pvx = mode[0]
        n = int(mode[1])

        if pvx == 'p':
            main_pvp(n)
        else:
            main_pve(n)

if __name__ == "__main__":
    SystemExit(main())
