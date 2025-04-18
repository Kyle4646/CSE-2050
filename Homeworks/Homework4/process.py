
class Process: #acts as our nodes
    """A circular queue to allow us to run processes turn-by-turn"""
    
    def __init__(self, pid, cycles = 100):
        '''Initializes pid number and amount of cycles, default link and prev
        to be none unless stated elsewhere'''
        
        self.pid = pid
        self.cycles = int(cycles)
        self.link = None
        self.prev = None
    
    def __eq__(self, other): #performs equality ==, not =
        '''Magic method takes over = sign to see if two Processes equal to eachother
        on basis of pip'''
        
        return(self.pid == other.pid) #Returns true now two pins equal
    
    def __repr__(self):
        '''returns Process and its attribute'''

        return(f'Process({self.pid},{self.cycles})')