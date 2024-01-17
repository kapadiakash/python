class Vahicle:
    def __init__(self,color,wheels) -> None:
        self._color=color
        self._wheels=wheels
        
class Car(Vahicle):
    def __init__(self,color,wheels,doors):
        super().__init__(color,wheels)
        self._doors=doors
        
    def car_detail(self):
        print(f'color of Car {self._color},no.of wheel {self._wheels}, no.of door {self._doors}')

car = Car("red",4,4)
car.car_detail()

print("Before changing protected variaable of wheel:",car._wheels)
car._wheels=10
print("Before changing protected variaable of wheel:",car._wheels)

# print('number of carls door',car._doors)
car._doors = 12
print('number of carls door',car._doors)

