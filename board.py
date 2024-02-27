# one board per program

class Board:
    def __init__(self):
        self.cells = [
            ["_", "_", "_"],
            ["_", "_", "_"],
            ["_", "_", "_"],
        ]
        self.is_won = False
        self.rows = 3
        self.columns = 3
    
    def print_board(self):
        for row in range(self.rows):
            row_str = ""
            for column in range(self.columns):
                row_str += self.cells[row][column]
            print(row_str)

    def is_won(self):
        return self.is_won
    
    def put_piece(self, input_char, row, column):
        row = int(row)
        column = int(column)
        
        if row >= 0 and row < self.rows and column >= 0 and column < self.columns \
        and self.cells[row][column] == "_":
            self.cells[row][column] = input_char.upper()
            return True
        elif self.cells[row][column] != "_":
             print("Oops, that spot already occupied")
             return False
        else:
            print("Oops, wrong input position")
            return False
    
    def check_availability(self, row, column):
         if row >= 0 and row < self.rows and column >= 0 and column < self.columns \
        and self.cells[row][column] == "_":
             return True
         else:
             return False
    
    def check_win(self, check_char):
        #print("Current char: " + check_char)
        for row in range(self.rows):
            for column in range(self.columns):
                prev_row = row - 1
                next_row = row + 1
                prev_column = column - 1
                next_column = column + 1
                if(prev_row >= 0 and next_row < self.rows and
                   prev_column >= 0 and next_column < self.columns and
                   self.cells[row][column] == check_char):
                    if self.cells[prev_row][prev_column] == check_char and self.cells[next_row][next_column] == check_char:
                        self.is_won = True
                        print("A", row, column, check_char)
                        return True
                    if self.cells[prev_row][row] == check_char and self.cells[next_row][column] == check_char:
                        self.is_won = True
                        print("B", row, column, check_char)
                        return True
                    if self.cells[prev_row][next_column] == check_char and self.cells[next_row][prev_column] == check_char:
                        self.is_won = True
                        print("C", row, column, check_char)
                        return True
                    if self.cells[row][prev_column] == check_char and self.cells[row][next_column] == check_char:
                        self.is_won = True
                        print("D", row, column, check_char)
                        return True
                    