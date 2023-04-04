class Car:

    def __init__(self, name, color, year):
        self._name = name
        self.color = color
        self.year = year

    def speed(self):
        return 'It is a fast car'

    def get_name(self):
        return f'Hi! My favorite car is {self._name}'

    def set_name(self, new_name):
        self._name = new_name


car1 = Car('BMW', 'black', 2022)
print(car1.name)
print(car1.get_name())
print(car1.year)
print(car1.color)

# car2 = Car('Mercedes-Benz', 'white', 2020)
# print(car2.get_name())
# print(car2.__dict__)
# car2.name = 'Land Rover'
# print(car2.get_name())
# print(car2.name)
# print(car2.set_name('Subaru'))
# print(car2.name)
#
#
class Cadillac(Car):

    def __init__(self, name, color, year, power, speed):
        super().__init__(name, color, year)
        self.power = power
        self.speed = speed

    def fastest_one(self):
        return 'I am the fastest one!'

    def speed(self):
        return 'I am a fastest car!'


car3 = Cadillac('Escalade', 'black', 2023, 48000, 480)
print(car3.get_name())
print(car3.__dict__)
