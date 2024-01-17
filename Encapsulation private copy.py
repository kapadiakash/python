class Car:
    def __init__(self,make,model,year):
        self.__make = make
        self.__model = model
        self.__year = year
        
    def start(self):
        print(f"The {self.__year} {self.__make} {self.__model} is starting.")
        
    def __info(self):
        print(f"My car is {self.__year} {self.__make} {self.__model} .")
    
    def display_info(self):
        return self.__info()
    
toyota = Car(make="Toyota",model="Camry",year=2022)

toyota.start()

print(toyota._Car__make)

