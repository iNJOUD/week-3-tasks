class Car:
    # create class attributes
    def __init__(self, plateNo, color, model, speed, typeCar, category):
        self.plateNo = plateNo
        self.color = color
        self.model = model
        self.speed = speed
        self.typeCar = typeCar
        self.category = category

    # create 5 methods to control the car
    def drive(self):
        return f'Car With plate number {self.plateNo} is moving ahead!'

    def stop(self):
        return f'Car With plate number {self.plateNo} Stopped!'

    def turn(self, keyword):
        return f'Car With plate number {self.plateNo} turned to {keyword}'


# create 5 class objects
car1 = Car('5948', 'Black', 'FORD', '10000', 'SEDAN', 'Mini')
car2 = Car('3452', 'Silver', 'KIA', '10000', 'CUV', 'intermediate')
car3 = Car('1132', 'White', 'TOYOTA', '10000', 'SUV', 'economy')
car4 = Car('6643', 'gray', 'ISUZU', '10000', 'VAN', 'compact')
car5 = Car('9876', 'Dark blue', 'GMC', '10000', 'COUPE', 'mini')

# simulate the cars on road
print(car1.drive())
print(car2.drive())
print(car3.turn('left'))
print(car4.turn('right'))
print(car1.turn('left'))
print(car5.drive())
print(car2.turn('right'))
print(car1.stop())
print(car2.stop())