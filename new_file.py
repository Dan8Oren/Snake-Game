def explode(self, board):
    radius = 3
    b_row = 2  # self.location[0]
    b_col = 3  # self.location[1]
    for to_row in range(radius+1):
        for to_col in range(radius+1):
            if to_row == 0 and to_col == 0:  # if center continue
                continue
            if 0 <= b_row + to_row < len(board) and 0 <= b_col + to_col < len(board[0]):
                board[b_row + to_row][b_col + to_col] = "R"
            else:
                pass
            if 0 <= b_row - to_row < len(board) and 0 <= b_col - to_col < len(board[0]):
                board[b_row - to_row][b_col - to_col] = "R"
            else:
                board[b_row][b_col] = "R"
    
            if to_row == 0 or to_col == 0:  # if on center column continue
                continue
    
            if 0 <= b_row + to_row < len(board) and 0 <= b_col - to_col < len(board[0]):
                board[b_row + to_row][b_col - to_col] = "R"
            else:
                pass
            if 0 <= b_row - to_row < len(board) and 0 <= b_col + to_col < len(board[0]):
                board[b_row - to_row][b_col + to_col] = "R"
            else:
                pass
    
    return board


if __name__ == '__main__':
    board = [[0 for _ in range(6)] for _ in range(6)]
    self = 8
    board = explode(self, board)
    for row in board:
        print(row)