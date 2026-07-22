from dataclasses import dataclass


@dataclass
class Ship:
    # -------------------Methods------------------------

    # ------------------Constructor-------------------

    def __init__(self, ship_type: str, ship_length: int):
        self.ship_type = ship_type
        self.ship_length = ship_length


