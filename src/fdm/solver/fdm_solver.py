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
        self.vector_len = 0
    
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
        self.preprocess(nx, ny)
        dx, dy = self.domain.getDelta(nx, ny)
        A = np.zeros([self.vector_len, self.vector_len])
        fv, u = np.zeros(self.vector_len), np.zeros(self.vector_len)
        for index in range(self.vector_len):
            for op in self.diff_op_expression:
                for node in op.stencil:
                    coord, coeff = node
                    x_offset, y_offset = coord
                    pass

        
    def preprocess(self, nx, ny = 1):
        dx, dy = self.domain.getDelta(nx, ny)
        self.index_to_grid = np.zeros(nx*ny, dtype=(int, 2))
        self.vector_len = 0
        for j in range(0, ny): # grid index on y axis
            for i in range(0, nx): # grid index on x axis
                x, y = self._get_coord_by_offset(dx, dy, i, j) # the real (x,y) coordinate
                if self.domain_condition.inDomain(x, y):
                    self.index_to_grid[self.vector_len] = (i, j)
                    self.grid_to_index[(i, j)] = self.vector_len
                    self.vector_len += 1

    def _get_coord_by_offset(self, dx, dy, x_grid_index, y_grid_index):
        x_offset, y_offset = x_grid_index + 1, y_grid_index + 1
        return self.domain.lower_left_coord + np.array([x_offset*dx, y_offset*dy])


        