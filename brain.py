
class Board:

    def __init__(self):
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        self.turn = 1
        self.winner = 0
        self.count_moves = 0

    def is_valid_move(self, pos: tuple):
        return self.board[pos[0]][pos[1]] == 0

    def inset(self, pos: tuple):
        self.board[pos[0]][pos[1]] = self.turn
        self.turn = self.turn * -1
        self.count_moves += 1

    def game_status(self):
        # Checks for win in the rows / columns
        for i in range(3):
            row_sum = 0
            col_sum = 0
            for j in range(3):
                row_sum += self.board[i][j]
                col_sum += self.board[j][i]
            if abs(row_sum) == 3:
                self.winner = row_sum / 3
            if abs(col_sum) == 3:
                self.winner = col_sum / 3

        # Checks for win in the diagonals
        lft_to_rt_sum = 0
        rt_to_lft_sum = 0
        for i in range(3):
            lft_to_rt_sum += self.board[i][i]
            rt_to_lft_sum += self.board[i][2-i]
        if abs(lft_to_rt_sum) == 3:
            self.winner = lft_to_rt_sum / 3
        if abs(rt_to_lft_sum) == 3:
            self.winner = rt_to_lft_sum / 3

        return self.winner

    def is_tie(self):
        return self.count_moves == 9

    def print_board(self):
        xo = [' ', 'X', 'O']
        print("- - - - -")
        for row in self.board:
            print(f"|{xo[row[0]]}  "
                  f"{xo[row[1]]}  "
                  f"{xo[row[2]]}|  \n")


# ------------------------- Check Code --------------------------------------------------

# b = Board()
# import random
# status = 0
# while not b.is_tie() and status == 0:
#     pos = (random.randint(0, 2), random.randint(0, 2))
#     if b.is_valid_move(pos):
#       b.inset(pos)
#       status = b.game_status()
#       b.print_board()
# print(f"The winner is {b.winner}")


