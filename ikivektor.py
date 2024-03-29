class Vektor:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def boyu(self):
        boy=(self.x **2+self.x,self.y **2) **0.5
        return boy
    def _repr(self):
        return("%di+%dj"%(self.x,self.y))
    def __add__(self, other):
        return Vektor(self.x+other.x,self.y+other.y)

    def __gt__(self, other):
        if self.boyu()>other.boyu():return True