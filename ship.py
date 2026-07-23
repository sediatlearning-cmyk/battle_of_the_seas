import orientation
import ship_type
from ship_type import ShipType
from orientation import Orientation


class Ship:

    # -------------------Methods------------------------
    def calculate_ship_positions(self):
        ship_positions = []
        ship_length = self.ship_type.ship_length
        start_line = ship_positions[0]
        start_column = ship_positions[1]
        for number in range(ship_length):
            if self.orientation == Orientation.HORIZONTAL:
                # TODO: A terminer
                ship_positions.append(start_line, start_column + number)

    # ------------------Constructor-------------------

    def __init__(self, ship_type: ShipType,
                 ship_starting_position: tuple,
                 orientation: Orientation):
        self.ship_type = ship_type
        self.ship_starting_position = ship_starting_position
        self.orientation = orientation
        self.ship_damage_positions = []

