import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../../src/util/diff_operators/impl")
import ddx, ddy
import unittest

class Test(unittest.TestCase):
    def test_ddx(self):
        a = ddx.ddx()
        assert a.stencil_upper_bound == 1
        assert a.stencil_lower_bound == -1

    def test_ddy(self):
        a = ddy.ddy()
        assert a.stencil_upper_bound == 1
        assert a.stencil_lower_bound == -1

if __name__ == '__main__':
    unittest.main()