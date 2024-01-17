class Car:
    def __init__(self,make,model,year) -> None:
        self.make = make            # Attribute
        self.model = model
        self.year = year
    
    def start(self):            # Method
        print(f"The {self.year} {self.make} {self.model} is starting.")
        
toyota = Car(make="Toyota",model="Camry",year="2022")

toyota.start()          # Public variable