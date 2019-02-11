import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../../src/util/diff_operators/impl")
import ddx, ddy
import unittest

class Test(unittest.TestCase):
    def test_ddx(self):
        a = ddx.ddx()
        t, c = a.stencil[0]
        assert t == (-1, 0)
        assert c == -1/2

    def test_ddy(self):
        a = ddy.ddy()
        t, c = a.stencil[0]
        assert t == (0, -1)
        assert c == -1/2

if __name__ == '__main__':
    unittest.main()