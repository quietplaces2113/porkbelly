from enum import Enum


class Units(Enum):
    CNT = 0
    OZ = 1
    LB = 2
    TSP = 3
    TBSP = 4
    CUP = 5
    RCP = 6

    def __str__(self):
        return self.name
