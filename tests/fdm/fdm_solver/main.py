import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../../../src/fdm/solver/")
import fdm_solver as fdm
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../../../src/util/diff_operator_expression")
import diff_op_expression as expr
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../../../src/util/")
import diff_operators.impl.ddx as ddx, diff_operators.impl.ddy as ddy, diff_operators.impl.laplacian2d as laplacian2d
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
        inDomain_s = lambda x, y: abs(x) < 1 and abs(y) < 1
        onBoundary_s = lambda x, y: abs(x-1) < np.spacing(1) or abs(x+1) < np.spacing(1) \
            or abs(y-1) < np.spacing(1) or abs(y+1) < np.spacing(1)

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

if __name__ == '__main__':
    unittest.main()