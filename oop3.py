class point:
    """create a new point at coordinates x,y"""
    def __init__(self,x=0,y=0):
        """create a new point at x,y"""
        self.x=x
        self.y=y
    def distance(self):
        return((self.x**2)+(self.y**2))**0.5
p=point(3,4)
print(p.distance())