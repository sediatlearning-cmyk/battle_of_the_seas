from dataclasses import dataclass

from board import Board
from ship import Ship


@dataclass
class Player:

    # ----------------------Methods-------------------------
    def ask_name_of_player(self):
        name = input("What is your name? ")
        return name

    def place_the_ships(self):
        pass

    # ----------------Constructor-----------------------
    def __init__(self, name: str, ships_board: Board, hit_board: Board, ships: list[Ship]):
        self.name = name
        self.ships_board = ships_board
        self.hit_board = hit_board
        self.ships = ships
