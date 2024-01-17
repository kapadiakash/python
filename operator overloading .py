class point1:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    
    def __add__(self,other):
        return self.x + other.x , self.y+other.y
    
class point2:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
        
p1 = point1(10,100)
p2 = point2(20,200)

print(p1+p2)
            
    