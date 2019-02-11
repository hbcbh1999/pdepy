import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../../../src/util/domain_conditions/impl/dirichlet")
import dirichlet_rectangle as dr
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../../../src/util/domain_conditions/core/domain")
import domain as dm
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.inDomain = lambda x, y: abs(x) < 1 and abs(y) < 1
        self.getBoundaryValue = lambda x, y: 1
        self.domain = dm.domain((-1, -1), (1, 1))

    def test_init(self):
        a = dr.dirichlet_rectangular_bc(self.inDomain, self.getBoundaryValue, self.domain)
        assert a.domain.lower_left_coord == (-1, -1)

if __name__ == '__main__':
    unittest.main()