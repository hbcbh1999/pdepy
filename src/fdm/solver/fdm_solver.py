import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/../../util/diff_operators')
import core.time_dependent_op as td
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve
class fdm_solver:
    def __init__(self, diff_op_expression, f, domain_condition):
        self.diff_op_expression = diff_op_expression
        self.f = f
        self.domain_condition = domain_condition
        self.domain = domain_condition.domain
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
            x, y = self.index_to_grid[index]
            fv[index] = self.f(*self._get_coord_by_offset(dx, dy, x, y))
            for op in self.diff_op_expression:
                for node in op.stencil:
                    coord, coeff = node
                    x_offset, y_offset = coord
                    cur_x, cur_y = x + x_offset, y + y_offset
                    cur_x_coord, cur_y_coord = self._get_coord_by_offset(dx, dy, cur_x, cur_y)
                    if self.domain_condition.onBoundary(cur_x_coord, cur_y_coord):
                        bv = self.domain_condition.getBoundaryValue(cur_x_coord, cur_y_coord)
                        u[index] -= op.coefficient * coeff * bv
                    elif not self.domain_condition.inDomain(cur_x_coord, cur_y_coord):
                        if not self._has_getNearestPoint(ny): raise NotImplementedError
                        pass
                    else:
                        A[index, self.grid_to_index[cur_x, cur_y]] += op.coefficient * coeff
        return spsolve(csr_matrix(A), fv + u)
        
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

    def _has_getNearestPoint(self, ny):
        if self.domain_condition.getNearestPoint[0] is None:
            return False
        elif self.domain_condition.getNearestPoint[1] is None and ny != 1:
            return False
        return True
    
    def _is_time_dependent(self):
        for op in self.diff_op_expression:
            if isinstance(op, td.time_dependent_operator):
                return True
        return False
    
    def _all_ops_are_time_dependent(self):
        for op in self.diff_op_expression:
            if not isinstance(op, td.time_dependent_operator):
                return False
        return True