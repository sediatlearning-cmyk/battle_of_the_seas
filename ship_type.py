from enum import Enum


class ShipType(Enum):

    AIRCRAFT_CARRIER = ("Aircraft Carrier", 5)
    CRUISER = ("Cruiser", 4)
    DESTROYER = ("Destroyer", 3)
    SUBMARINE = ("Submarine", 3)
    TORPEDO_BOAT = ("Torpedo boat", 2)

    def __init__(self, ship_name, ship_length):
        self.ship_name = ship_name
        self.ship_length = ship_length

