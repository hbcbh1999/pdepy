from . import diff_op
class time_dependent_operator(diff_op.diff_operator):
    def __init__(self, stencil, known_terms, coefficient = 1):
        # a list of tuple whose first element is relative position of node in the stencil, 
        # second element is the coefficient in the fdm equation
        self.stencil = stencil
        # a list of known terms on the right hand side of equation
        self.known_terms = known_terms
        # the coefficient before this operator, e.g., 1/delta_x^2
        self.coefficient = coefficient