

class Foo:

    def __init__(self, name, profession):
        self.name = name
        self.profession = profession

    '''This initializer takes the name and profession, assumed to be a string'''
    
    def speak(self):
        return(f'{self.name} says hello!')
    
    '''Allows name to say hello defined in initializer'''
    
    def __repr__(self):
        return(f'Foo({self.name}, {self.profession})')
    
    '''Returns represenation of object we set as a class'''