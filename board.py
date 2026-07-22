from dataclasses import dataclass


@dataclass
class Board:

    # ----------------Methods--------------------
    def display_board(self):

        grid = [[" " for _ in range(self.row)] for _ in range(self.column)]

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








