class Mammals:
    leg1 = 'leg 1'
    leg2 = 'leg 2'
    leg3 = 'leg 3'
    leg4 = 'leg 3'

    def move_leg(self):
        print(f'move {self.leg1}')
        print(f'move {self.leg3}')
        print(f'move {self.leg2}')
        print(f'move {self.leg4}')


class Dog(Mammals):
    def voice(self):
        print(f'Гав! My name is {self.name}')

    def __init__(self, name, mom=None, father=None):
        print(name)
        self.name = name

        if mom is None or father is None:
            self.color = 'rainbow'
        else:
            self.set_color(mom.color, father.color)

    def set_color(self, mom_color, father_color):
        self.color = mom_color + father_color


class Cat(Mammals):
    def voice(self):
        print('Meow!')

    def save_something(self, parameter_name, parameter_value):
        self.brain[parameter_name] = parameter_value

    def greet_master(self):
        self.voice()
        print(self.brain['master'])

    def __init__(self, cat_name, mother=None, father=None):
        if mother is None and father is None:
            self.color = 'white'
        else:
            self.color = mother.color + ' ' + father.color
        self.brain = {}
        self.brain['name'] = cat_name


mother_1 = Cat('murka')
father_1 = Cat('barsik')

print(mother_1.color)
print(father_1.color)

Mika = Cat('Mika', mother_1, father_1)
print(Mika.color)
Mika.move_leg()

Sharik = Dog('Sharik')
Sharik.voice()
Sharik.move_leg()
print(Sharik.color)