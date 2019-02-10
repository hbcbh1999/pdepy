import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/..')
from core import *
class ddx(diff_op):
    def __init__(self):
        super().__init__(Axis.X, np.array([0, 1/2, -1/2]), 3)