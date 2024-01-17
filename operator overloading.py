# class point1:
#     def __init__(self,x) -> None:
#         self.x = x
    
#     def __add__(self,other):
#         return self.x + other.x
    
# class point2 :
#     def __init__(self,x) -> None:
#         self.x = x
        
# p1 = point1(10)
# p2 = point2(20)

# print(p1+p2)

# print(point1.__add__(p1,p2))


class point1:
    def __init__(self,x) -> None:
        self.x = x
    
    def __add__(self,other):
        return self.x + other.x
    
class point2:
    def __init__(self,x) -> None:
        self.x = x

p1 = point1(40)
p2 = point2(60)

print(p1+p2)

    