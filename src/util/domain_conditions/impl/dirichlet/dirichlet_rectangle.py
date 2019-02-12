import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/../..')
from core.boundary_condition import bc # domain_conditions' core
# from core.domain import domain as dm

class dirichlet_rectangular_bc(bc.boundary_condition):
    def __init__(self, inDomain, onBoundary, getBoundaryValue, domain):
        super().__init__(inDomain, onBoundary, getBoundaryValue)
        self.domain = domain # this is the class domain