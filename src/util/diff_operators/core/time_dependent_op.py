from . import diff_op
class time_dependent_operator(diff_op.diff_operator):
    def __init__(self, stencil, coefficient = 1):
        super().__init__(stencil, coefficient, True)