class NodeEdge:
    def __init__(self, v1=None, v2=None):
        self.marked = False
        self.v1 = v1
        self.v2 = v2
        self.link_v1 = None
        self.link_v2 = None

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"({self.v1}:{self.v2})"
