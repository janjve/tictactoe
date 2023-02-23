import math
import random

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

def minimax(board: game.Board, ai_player: int):

    opponent_player = game.next_player(ai_player)
    memo = {}

    def minimax_(board, is_maximizing=False):
        board_tuple = tuple(tuple(x) for x in board)
        if (board_tuple, is_maximizing) in memo:
            return memo[(board_tuple, is_maximizing)]
        if game.is_winner(board, ai_player):
            return 1
        elif game.is_winner(board, opponent_player):
            return -1
        elif game.is_done(board):
            return 0

        scores = []

        for row, col in game.get_possible_moves(board):
            board[row][col] = ai_player if is_maximizing else opponent_player
            scores.append(minimax_(board, not is_maximizing))
            board[row][col] = None

        if is_maximizing:
            score = max(scores)
        else:
            score = min(scores)
        memo[(board_tuple, is_maximizing)] = score
        return score


    best_moves = []
    best_score = -math.inf
    for row, col in game.get_possible_moves(board):
        board[row][col] = ai_player
        score = minimax_(board)
        print("score", score)
        board[row][col] = None
        if score > best_score:
            best_moves = [(row, col)]
            best_score = score
        elif score == best_score:
            best_moves.append((row, col))

    best_move_idx = random.randint(0, len(best_moves) - 1)
    return best_moves[best_move_idx]
