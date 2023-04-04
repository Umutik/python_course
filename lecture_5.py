class Dog:
    biology_class = 'Animal'

    def __init__(self, name, weight, color):
        self._name = name
        self.weight = weight
        self.color = color

    def run(self):
        return 'I can run!'

    def get_name(self):
        return f'Hello! My name is {self._name}'

    def set_name(self, new_name):
        self._name = new_name





# dog1 = Dog('Tom', 8, 'black')
# print(dog1.name)
# print(dog1.get_name())
# print(dog1.weight)
# print(dog1.color)
# print(dog1.biology_class)


dog2 = Dog('Rex', 7, 'Grey')
print(dog2.biology_class)
print(dog2.get_name())
# print(dog2.__dict__)
# dog2.name = 'Snoopy'
# print(dog2.get_name())
# print(dog2.name)
print(dog2.set_name('Snoopy'))
print(dog2.get_name())


class Pitbull(Dog):

    def __init__(self, name, weight, color, passport):
        super().__init__(name, weight, color)
        self.passport = passport

    def give_a_paw(self):
        return 'I can give a paw!'

    def run(self):
        return 'I can run faster'

dog3 = Pitbull('Lassie', 8, 'white', 'type1')
# print(dog3.get_name())
# print(dog3.biology_class)
print(dog3.passport)
# print(dog2.run())
# print(dog3.run())

#Polymorphism



