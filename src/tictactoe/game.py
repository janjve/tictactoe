from typing import List, Tuple

Move = Tuple[int, int]

class Board:
    def __init__(self, n: int, k: int = None) -> None:
        if k is None:
            k = n

        self.state = [[None] * n for _ in range(n)]
        self.k = k
        self.history: List[Move] = []

    def __getitem__(self, i):
        return self.state[i]
    
    def __len__(self):
        return len(self.state)

    def make_move(self, row: int, col: int, player: int):
        self[row][col] = player
        self.history.append((row, col))

    def revert_move(self):
        if self.history:
            row, col = self.history.pop()
            self.board[row][col] = None

    def winner(self):
        # no moves was done yet
        if not self.history:
            return None
        
        # only check previous move
        move_row, move_col = self.history[-1]
        player = self[move_row][move_col]

        # check for horizontal win
        directions = [(0,1), (1,0)]

        # check each direction
        for d_row, d_col in directions:
            count = 0
            row, col = move_row, move_col

            # span out in direction while we find occurence of player
            while count < self.k and self.inside_board(row, col) and self[row][col] == player:
                count += 1
                row += d_row
                col += d_col
            
            # span out in oppposite direction while we find occurence of player
            d_row = -d_row
            d_col = -d_col
            row, col = move_row + d_row, move_col + d_col  # reset without recounting move cell
            
            while count < self.k and self.inside_board(row, col) and self[row][col] == player:
                count += 1
                row += d_row
                col += d_col
            
            # player has won by having k elements in current direction
            if count == self.k:
                return player
            
        return None

    def winner_old(self):
        # no moves was done yet
        if not self.history:
            return None
        
        # only check previous move
        row, col = self.history[-1]
        player = self[row][col]

        n = len(self)
        k = self.k

        # Check for horizontal wins
        left_horizontal = 0
        right_horizontal = 0
        
        for i in range(n):
            for j in range(n - k + 1):
                if all(self[i][j + x] == self[i][j] for x in range(1, k)):
                    return self[i][j]

        # Check for vertical wins
        for i in range(n - k + 1):
            for j in range(n):
                if all(self[i + x][j] == self[i][j] for x in range(1, k)):
                    return self[i][j]

        # Check for top-left to bottom-right diagonal wins
        for i in range(n - k + 1):
            for j in range(n - k + 1):
                if all(self[i + x][j + x] == self[i][j] for x in range(1, k)):
                    return self[i][j]

        # Check for top-right to bottom-left diagonal wins
        for i in range(n - k + 1):
            for j in range(k - 1, n):
                if all(self[i + x][j - x] == self[i][j] for x in range(1, k)):
                    return self[i][j]

        # No winner
        return None

    def next_player(self, player):
        return 1 - player
    
    def inside_board(self, row: int, col: int) -> bool:
        n = len(self)
        return 0 <= row < n and 0 <= col < n

    def is_valid_move(self, row: int, col: int) -> bool:
        return self.inside_board(row, col) and self[row][col] is None

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
