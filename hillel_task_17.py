# class Animals
# class Chordate:

class Actinopterygii:
    tail = 'tail'
    left_fins = 'left fins'
    right_fins = 'right fins'

    def swim(self):
        print(f'move {self.tail}')
        print(f'move {self.left_fins}')
        print(f'move {self.right_fins}')


class Atlantic_herring(Actinopterygii):
    def __init__(self, name):
        print(name)
        self.name = name

    def set_color(self, color):
        print(color)
        self.color = 'grey'


class Common_bream(Actinopterygii):
    def set_color(self):
        self.color = 'dark grey'


Fish = Atlantic_herring('Fish')
Fish.swim()
#color daesn't work
