class Car:
    def __init__(self,make,model,year,color,fuel_type,is_nunning=True,speed=0):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.fuel_type = fuel_type
        self.is_running = is_nunning
        self.speed = speed
        
    def start(self):
        if self.is_running:
            print(f"the {self.color} {self.year} {self.make} {self.model} is starting.")
        else:
            print("press start button to start the car.")
            
    def stop(self):
        if self.is_running:
            print(f'the {self.color} {self.year} {self.make} {self.model} is stopping.')
        else:
            print('the car is already stopped')
            
    def accelerate(self,speed_increase):
        if self.is_running:
            self.speed += speed_increase
            print(f'the car is acceletating.current speed: {self.speed} mph.')
        else:
            print('start the car before accelerating.')
            
    def display_info(self):
        print(f'\nCar information:\n'
              f'make:{self.make}\n'
              f'model:{self.model}\n'
               f"Year: {self.year}\n"
              f"Color: {self.color}\n"
              f"Fuel Type: {self.fuel_type}\n"
              f"Is Running: {self.is_running}\n"
              f"Current Speed: {self.speed} mph\n")
        
toyota = Car(make='toyota', model='camry',year=2022,color='blue',fuel_type='gasoline')

toyota.display_info()
toyota.start()
toyota.accelerate(30)
toyota.stop()