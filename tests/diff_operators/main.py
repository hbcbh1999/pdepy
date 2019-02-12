import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../../src/util/diff_operators/")
import impl.ddx as ddx, impl.ddy as ddy
import core.diff_op as diff_op
import unittest

class Test(unittest.TestCase):
    def test_ddx(self):
        a = ddx.ddx(0.1)
        t, c = a.stencil[0]
        assert t == (-1, 0)
        assert c == -5

    def test_ddy(self):
        a = ddy.ddy(0.1)
        t, c = a.stencil[1]
        assert t == (0, 1)
        assert c == 5

    def test_inheritance(self):
        assert issubclass(ddx.ddx, diff_op.diff_operator)

if __name__ == '__main__':
    unittest.main()