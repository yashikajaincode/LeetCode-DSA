class Solution:
    def validTicTacToe(self, board: list[str]) -> bool:
        def win(player):
            for i in range(3):
                if all(board[i][j] == player for j in range(3)): return True
                if all(board[j][i] == player for j in range(3)): return True
            if all(board[i][i] == player for i in range(3)): return True
            if all(board[i][2 - i] == player for i in range(3)): return True
            return False

        x_count = sum(row.count('X') for row in board)
        o_count = sum(row.count('O') for row in board)

        if o_count > x_count or x_count - o_count > 1:
            return False
        if win('X') and x_count != o_count + 1:
            return False
        if win('O') and x_count != o_count:
            return False
        return True
