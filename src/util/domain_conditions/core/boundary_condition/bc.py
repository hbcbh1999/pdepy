class boundary_condition:
    def __init__(self, inDomain, getBoundaryValue):
        # inDomain is a function which takes a point, returns whether the point is in domain.
        self.inDomain = inDomain
        # getBoundaryValue is a function which takes a point, and returns the boundary value on that point.
        self.getBoundaryValue = getBoundaryValue