class Board:

    row: int = 10
    column: int = 10
    grid: list = [[" " for _ in range(row)] for _ in range(column)]

    # ----------------Methods--------------------

    def display_board(self, grid):
        letters = [" A ", " B ", " C ", " D ", " E ", " F ", " G ", " H ", " I ", " J "]
        print(letters)
        for row in grid:
            
            print("+---" * 10 + "+")
            for cell in row:
                print(f"| {cell} |", end="")
            print("|")

        print("+---" * 10 + "+")

    # ---------------Constructor-----------------

    def __init__(self, row: int, column: int):
        self.row: int = row
        self.column: int = column
