from enum import Enum
class Axis(Enum):
    X = 1
    Y = 2
    MIXED = 3

class diff_op:
    def __init__(self, axis, stencil, stencil_len, coefficient = 1):
        self.axis = axis
        self.stencil = stencil
        self.stencil_len = stencil_len
        self.coefficient = coefficient