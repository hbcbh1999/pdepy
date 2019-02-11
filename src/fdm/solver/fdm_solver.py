class fdm_solver:
    def __init__(self, diff_op_expression, f, domain_condition, get_nearest_point = (None, None)):
        self.diff_op_expression = diff_op_expression
        self.f = f
        self.domain_condition = domain_condition
        self.domain = domain_condition.domain
        # get_nearest_point is a 2 element function tuple, 
        # where the first one takes (x, y) and gives the closest point on x axis,
        # and the second one gives the closest point on y axis.
        # used by irregular domain
        self.get_nearest_point = get_nearest_point
    
    def solve(self, nx, ny = 0):
        delta_x, delta_y = self.domain.getDelta(nx, ny)