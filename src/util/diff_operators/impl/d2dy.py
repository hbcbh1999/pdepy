import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/..')
from core import diff_op # diff_operators' core
import numpy as np
class d2dy(diff_op.diff_operator):
    def __init__(self, dy, coefficient = 1):
        super().__init__([((0, -1), 1/dy**2), ((0, 0), -2/dy**2), ((0, 1), 1/dy**2)], coefficient)

    def getIrregularStencil(self, dy, tau, direction):
        # direction = 1 represents positive y axis; -1 represents negative y axis
        c1, c2, c3 = 2/(tau+1), -2/tau, 2/(tau*(tau+1))
        if direction == diff_op.Direction.POSITIVE:
            return [((0, -1), c1/dy^2), ((0, 0), c2/dy^2), ((0, 1), c3/dy^2)]
        elif direction == diff_op.Direction.NEGATIVE:
            return [((0, -1), c3/dy^2), ((0, 0), c2/dy^2), ((0, 1), c1/dy^2)]