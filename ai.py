import random
from copy import deepcopy
from typing import List, Optional, Tuple

import game


def randomize(board: game.Board, *_):
    n = len(board) - 1
    move = None
    while move is None:
        move_row = random.randint(0, n)
        move_col = random.randint(0, n)
        if game.is_valid_move(board, move_row, move_col):
            move = move_row, move_col

    return move


def greedy(board: game.Board, ai_player: int):
    board = deepcopy(board)
    n = len(board)

    memo = {}

    def win_loss(board, current_player) -> Tuple[int, int]:
        board_tuple = tuple(tuple(x) for x in board)
        if (board_tuple, current_player) in memo:
            return memo[(board_tuple, current_player)]

        if game.is_winner(board, ai_player):
            return (1, 0)
        elif game.is_winner(board, game.next_player(ai_player)):
            return (0, 1)
        
        wins = 0
        losses = 0
        for row in range(n):
            for col in range(n):
                if game.is_valid_move(board, row, col):
                    game.make_move(board, row, col, current_player)
                    win_d, loss_d = win_loss(board, game.next_player(ai_player))
                    wins += win_d
                    losses += loss_d
                    board[row][col] = None

        memo[(board_tuple, current_player)] = (wins, losses)

        return memo[(board_tuple, current_player)]


    best_ratio = 0.0
    move = (0,0)
    for row in range(n):
        for col in range(n):
            if game.is_valid_move(board, row, col):
                game.make_move(board, row, col, ai_player)
                wins, losses = win_loss(board, game.next_player(ai_player))
                ratio = (wins + 0.01) / (losses + 0.01)
                if ratio > best_ratio:
                    best_ratio = ratio
                    move = (row, col)
                    
                board[row][col] = None

    print(f"Picking move {move} with ratio {best_ratio}")

    return move