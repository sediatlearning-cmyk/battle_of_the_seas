from ship_type import ShipType
from orientation import Orientation


class Ship:

    # -------------------Methods------------------------

    # ------------------Constructor-------------------

    def __init__(self, ship_type: ShipType,
                 ship_starting_position: tuple,
                 orientation: Orientation):
        self.ship_type = ship_type
        self.ship_starting_position = ship_starting_position
        self.orientation = orientation
        self.ship_damage_positions = []
