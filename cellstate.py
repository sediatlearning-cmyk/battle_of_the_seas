from enum import Enum


class CellState(Enum):

    EMPTY = " "
    MISS = "o"
    HIT = "X"
    SUNK = "--"
