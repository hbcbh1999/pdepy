from enum import Enum
class Axis(Enum):
    X = 1
    Y = 2
    MIXED = 3

class diff_operator:
    def __init__(self, axis, stencil, stencil_lower_bound, stencil_upper_bound, coefficient = 1):
        # if it's du/dx, then axis = X. if it's du/dy, then axis = Y. If the operator uses both X and Y axis, it's mixed.
        self.axis = axis
        self.stencil = stencil
        # for the classical du/dx^2 's stencil (1) (-2) (1), the lower bound is -1 and the upper bound is 1 
        self.stencil_lower_bound = stencil_lower_bound
        self.stencil_upper_bound = stencil_upper_bound
        # the coefficient before this operator, e.g., 1/delta_x^2
        self.coefficient = coefficient