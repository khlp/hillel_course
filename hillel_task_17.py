class Domain:
    cell = 'сells'

    def eukaryotes(self):
        print(f'Domain: Eukaryote, {self.cell} organisms whose have a nucleus enclosed within a nuclear envelope')

class Kingdom(Domain):
    movement = 'Ability to move actively'

    def animal(self):
        print(f'Kingdom: Animal \nMain_charecteristic: {self.movement}')

    tail = 'tail'
    left_fins = 'left fins'
    right_fins = 'right fins'

    def swim(self):
        print(f'Movement: move {self.tail}')
        print(f'move {self.left_fins}')
        print(f'move {self.right_fins}')

class Type_(Kingdom):
    notochord = 'a stiff rod of cartilage that extends along the inside of the body'
    dorsal_neural_tube = 'the main communications trunk of the nervous system.'

    def chordates(self):
        print(
            f'Type : Chordate \nAnatomy: \n Notochord - {self.notochord} \n Dorsal neural Tube - {self.dorsal_neural_tube}')

class Class_name(Type_):
    habitat = 'Freshwater and marine environments'

    def ray_finned_fish(self):
        print(f'Class : Actinopterygii \n Habitat: {self.habitat}')


class Atlantic_herring(Class_name):
    color = 'grey'

    def __init__(self, name):
        print(name)
        self.name = name

    def set_color(self):
        print(f'Color : {self.color}')

class Common_bream(Class_name):
    color = 'dark grey'

    def __init__(self, name):
        print(name)
        self.name = name

    def set_color(self):
        print(f'Color : {self.color}')

First_fish = Atlantic_herring('Herring Semen')
First_fish.eukaryotes()
First_fish.animal()
First_fish.swim()
First_fish.chordates()
First_fish.ray_finned_fish()
First_fish.set_color()
print('------------')
Second_fish = Common_bream('Bream Den')
Second_fish.eukaryotes()
Second_fish.animal()
Second_fish.swim()
Second_fish.chordates()
Second_fish.ray_finned_fish()
Second_fish.set_color()