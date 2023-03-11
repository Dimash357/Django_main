# Task 1
s = int(input("Стоимость подписки: "))
p = int(input("Стоимость пиццы: "))
m = int(input("Зарплата: "))
if s + p <= m:
    print("Да")
else:
    print("Нет")


# Task 2
class ChessBoard:
    def __init__(self):
        self.board = [['.' for j in range(8)] for i in range(8)]

    def print_board(self):
        for row in self.board:
            print(' '.join(row))

    def is_valid_cell(self, square):
        row, col = square
        if row < 0 or row >= 8:
            raise ValueError("Invalid row")
        if col < 0 or col >= 8:
            raise ValueError("Invalid column")
        return True

    def can_queen_move(self, square1, square2):
        self.is_valid_cell(square1)
        self.is_valid_cell(square2)
        row1, col1 = square1
        row2, col2 = square2
        if row1 == row2 or col1 == col2 or abs(row1 - row2) == abs(col1 - col2):
            return True
        return False

    def can_knight_move(self, square1, square2):
        self.is_valid_cell(square1)
        self.is_valid_cell(square2)
        row1, col1 = square1
        row2, col2 = square2
        diff_row = abs(row1 - row2)
        diff_col = abs(col1 - col2)
        if (diff_row == 2 and diff_col == 1) or (diff_row == 1 and diff_col == 2):
            return True
        return False


board = ChessBoard()
print("Initial board:")
board.print_board()

square1 = (0, 0)
square2 = (7, 7)
try:
    print(f"Can queen move from {square1} to {square2}? {board.can_queen_move(square1, square2)}")
except ValueError as e:
    print(e)
except Exception as e:
    print(f"An error occurred: {e}")

square1 = (3, 5)
square2 = (8, 7)
try:
    print(f"Can queen move from {square1} to {square2}? {board.can_queen_move(square1, square2)}")
except ValueError as e:
    print(e)
except Exception as e:
    print(f"An error occurred: {e}")

square1 = (0, 0)
square2 = (1, 2)
try:
    print(f"Can knight move from {square1} to {square2}? {board.can_knight_move(square1, square2)}")
except ValueError as e:
    print(e)
except Exception as e:
    print(f"An error occurred: {e}")

square1 = (0, 0)
square2 = (-1, 2)
try:
    print(f"Can knight move from {square1} to {square2}? {board.can_knight_move(square1, square2)}")
except ValueError as e:
    print(e)
except Exception as e:
    print(f"An error occurred: {e}")
