import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../diff_operators/")
import impl.ddx as ddx, impl.ddy as ddy
import core.diff_op as diff_op
class diff_operator_expression:
    """
    A class for the storage of all differential operators in a PDE.

    "expression" is a list which contains objects from class "diff_operator"
    """
    def __init__(self, ops = []):
        self.length = 0
        self.expression = []
        for op in ops:
            self.append(op)

    def append(self, op):
        def check_and_append(op):
            if isinstance(op, diff_op.diff_operator):
                self.expression.append(op)
                self.length += 1
            else:
                raise TypeError("Adding non-operator into the expression")
        if type(op) is list:
            for o in op:
                check_and_append(o)
        else:
            check_and_append(op)

    def __len__(self):
        return self.length

    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        if self.n < self.length:
            result = self.expression[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration