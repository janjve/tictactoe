from typing import List, Tuple

Move = Tuple[int, int]

class Board:
    def __init__(self, n: int) -> None:
        self.state = [[None] * n for _ in range(n)]
        # self.history: List[Tuple[Move, int]] = []

    def __getitem__(self, i):
        return self.state[i]
    
    def __len__(self):
        return len(self.state)

    def make_move(self, row: int, col: int, player: int):
        self[row][col] = player
        # self.history.append((row, col), player)

    # def revert_move(self):
    #     if self.history:
    #         (row, col), _ = self.history.pop()
    #         self.board[row][col] = None

    def is_winner(self, player):
        n = len(self)

        for row in self:
            if all(cell == player for cell in row):
                return True

        for col_idx in range(n):
            if all(row[col_idx] == player for row in self):
                return True

        # diagonal descending
        if all(self[idx][idx] == player for idx in range(n)):
            return True

        # diagonal ascending
        if all(self[idx][n - 1 - idx] == player for idx in range(n - 1, -1, -1)):
            return True

        return False
    
    def next_player(self, player):
        return 1 - player
    
    def is_valid_move(self, row: int, col: int) -> bool:
        n = len(self)
        return 0 <= row < n and 0 <= col < n and self[row][col] is None

    def is_done(self) -> bool:
        n = len(self)

        for row in range(n):
            for col in range(n):
                if self[row][col] is None:
                    return False

        return True
    
    def get_possible_moves(self) -> List[Move]:
        possible_moves = []
        
        for row in range(len(self)):
            for col in range(len(self[row])):
                if self.is_valid_move(row, col):
                    possible_moves.append((row, col))

        return possible_moves
