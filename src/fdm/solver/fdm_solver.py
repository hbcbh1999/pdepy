import numpy as np
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
        self.index_to_grid = None
        self.grid_to_index = {}
    
    def solve(self, nx, ny = 1):
        """
        nx is the grid points number in x axis; ny is the symmetry of nx.
        The following grid has nx = 4, ny = 3
         _ _ _ _ _
        |_|_|_|_|_|
        |_|_|_|_|_|
        |_|_|_|_|_|
        |_|_|_|_|_|
        """
        dx, dy = self.domain.getDelta(nx, ny)
        A = np.zeros([ny, nx])
        fv, u = np.zeros(ny * nx), np.zeros(ny * nx)
        
    def preprocess(self, dx, dy, nx, ny = 1):
        self.index_to_grid = np.zeros(nx*ny)
        for j in range(0, ny):
            y_offset = j + 1
            for i in range(0, nx):
                x_offset = i + 1
                x, y = self.domain.upper_left_coord + np.array([x_offset*dx, y_offset*dy])
                

        
