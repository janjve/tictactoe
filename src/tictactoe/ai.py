import itertools
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

    opponent_player = board.next_player(ai_player)
    memo = {}

    def minimax_(board, is_maximizing, alpha: int, beta: int):
        board_tuple = tuple(tuple(x) for x in board)
        if (board_tuple, is_maximizing) in memo:
            return memo[(board_tuple, is_maximizing)]
        
        if board.is_winner(ai_player):
            return (1, (None,None))
        elif board.is_winner(opponent_player):
            return (-1, (None,None))
        elif board.is_done():
            return (0, (None,None))
        
        moves = list(board.get_possible_moves())
        random.shuffle(moves)
        best_move = None
        if is_maximizing:
            best_score = -math.inf
            for row, col in moves:
                board[row][col] = ai_player
                score, _ = minimax_(board, not is_maximizing, alpha, beta)
                board[row][col] = None
                if score > best_score:
                    best_move = (row, col)
                    best_score = score
                alpha = max(alpha, score)

                if beta <= alpha:
                    break
        else:
            best_score = math.inf
            for row, col in moves:
                board[row][col] = opponent_player
                score, _ = minimax_(board, not is_maximizing, alpha, beta)
                board[row][col] = None

                if score < best_score:
                    best_move = (row, col)
                    best_score = score
                beta = min(beta, score)

                if beta <= alpha:
                    break

        memo[(board_tuple, is_maximizing)] = best_score, best_move
        
        return memo[(board_tuple, is_maximizing)] 

    best_score, best_move = minimax_(board, True, -math.inf, math.inf)
    print(best_score)
    return best_move
