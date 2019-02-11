import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/..')
from core import diff_op, Axis # diff_operators' core
import numpy as np
class ddx(diff_op.diff_operator):
    def __init__(self):
        super().__init__(Axis.X, np.array([0, 1/2, -1/2]), -1, 1)