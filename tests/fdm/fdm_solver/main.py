import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../../../src/fdm/solver/")
import fdm_solver as fdm
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../../../src/util/diff_operator_expression")
import diff_op_expression as expr
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../../../src/util/")
import diff_operators.impl.ddx as ddx, diff_operators.impl.ddy as ddy, diff_operators.impl.laplacian2d as laplacian2d,\
    diff_operators.impl.ddt as ddt, diff_operators.impl.time_dependent_d2dx as td_d2dx
import diff_operators.core.diff_op as diff_op
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../../../src/util/domain_conditions/core/domain")
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../../../src/util/domain_conditions/impl/dirichlet")
import dirichlet_rectangle as dr
import domain as dm
import unittest
import numpy as np

class Test(unittest.TestCase):
    def setUp(self):
        domain = dm.domain(np.array([-1, -1]), np.array([1, 1]))
        d = ddx.ddx(0.1)
        self.expression = expr.diff_operator_expression([d])
        inDomain = lambda x, y: abs(x) < 1 and abs(y) < 1
        onBoundary = lambda x, y: abs(x-1) < np.spacing(1) or abs(x+1) < np.spacing(1) \
            or abs(y-1) < np.spacing(1) or abs(y+1) < np.spacing(1)
        getBoundaryValue = lambda x, y: 1
        self.diri = dr.dirichlet_rectangular_bc(inDomain, onBoundary, getBoundaryValue, domain)
        self.diri2 = dr.dirichlet_rectangular_bc(inDomain, onBoundary, getBoundaryValue, domain, (lambda x, y: 1, lambda x, y: 2))
        self.solver = fdm.fdm_solver(self.expression, lambda x, y: 1, self.diri)
        self.solver2 = fdm.fdm_solver(self.expression, lambda x, y: 1, self.diri2)

        domain_s = dm.domain(np.array([0, 0]), np.array([1, 1]))
        inDomain_s = lambda x, y: 0 < x < 1 and 0 < y < 1
        onBoundary_s = lambda x, y: abs(x-1) < np.spacing(1) or abs(x) < np.spacing(1) \
            or abs(y-1) < np.spacing(1) or abs(y) < np.spacing(1)
        getBoundaryValue_s = lambda x, y: 1/(1+x) + 1/(1+y)
        f_s = lambda x, y: 2/(1+x)**3 + 2/(1+y)**3
        self.dirichlet = dr.dirichlet_rectangular_bc(inDomain_s, onBoundary_s, getBoundaryValue_s, domain_s)
        self.real_solver = fdm.fdm_solver([], f_s, self.dirichlet)

    def test_solve(self):
        real_function = lambda x, y: 1/(1+x) + 1/(1+y)
        error = []
        for n in [9, 19, 39, 79]:
            dx, dy = 1/(n+1), 1/(n+1)
            self.real_solver.diff_op_expression = expr.diff_operator_expression([laplacian2d.laplacian2d(dx, dy)])
            u = self.real_solver.solve(n, n)
            real_u = np.zeros(n**2)
            for j in range(0, n):
                y = (j+1)/(n+1)
                for i in range(0, n):
                    x = (i+1)/(n+1)
                    real_u[j*n+i] = real_function(x, y)
            error.append(max(abs(real_u-u)))
            # print(f"when n = {n}, the error is {max(abs(real_u-u))}")
        assert error[0] < .000554
        assert error[1] < .000141
        assert error[2] < .000036
        assert error[3] < .000009

        
    def test_preprocess(self):
        self.solver.preprocess(19, 9)
        assert self.solver.vector_len == 171
    
    def test_get_coord_by_offset(self):
        x, y = self.solver._get_coord_by_offset(0.1, 0.2, 0, 0)
        assert x == -0.9
        assert y == -0.8
    
    def test_has_getNearestPoint(self):
        assert self.solver._has_getNearestPoint(2) == False
        assert self.solver2._has_getNearestPoint(2) == True

    def test_is_time_dependent(self):
        a = ddt.ddt(0.1)
        b = td_d2dx.td_d2dx(0.1)
        expression = expr.diff_operator_expression([a, b])
        self.solver.diff_op_expression = expression
        assert self.solver._is_time_dependent() is True
        assert self.solver._all_ops_are_time_dependent() is True
        
    def test_all_ops_are_time_dependent(self):
        a = ddt.ddt(0.1)
        b = ddx.ddx(0.1)
        expression = expr.diff_operator_expression([a, b])
        self.solver.diff_op_expression = expression
        assert self.solver._all_ops_are_time_dependent() is False

if __name__ == '__main__':
    unittest.main()