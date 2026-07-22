from dataclasses import dataclass

from board import Board
from ship import Ship


@dataclass
class Player:

    # ----------------------Methods-------------------------

    # ----------------Constructor-----------------------
    def __init__(self, name: str, ships_board: Board, hit_board: Board, ships: list[Ship]):
        self.name = name
        self.ships_board = ships_board
        self.hit_board = hit_board
        self.ships = ships
