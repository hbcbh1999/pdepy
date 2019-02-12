class diff_operator(object):
    def __init__(self, stencil, coefficient = 1):
        # a list of tuple whose first element is relative position of node in the stencil, 
        # second element is the coefficient in the fdm equation
        self.stencil = stencil
        # the coefficient before this operator, e.g., 1/delta_x^2
        self.coefficient = coefficient