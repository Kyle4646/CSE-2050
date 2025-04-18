import process
from process import Process
    
class CircularQueue: #doubly-linked list but ciruclar

    def __init__(self, processes = None):
        '''This initializes processess and length'''
        
        self._len = 0
        self._head = None
        self._d_processes = {}
        if processes is not None:
            for pro in processes:
                self.add_process(pro)
                
    def add_process(self, process):
        '''adds process to list. If one item, makes process loop itself, 
        otherwise it sets the system up'''

        if process.pid in self._d_processes:
            process = self._d_processes[process.pid] #ensures if pid already in queue, makes it same
        else:
            if len(self) == 0:
                self._head = process
                self._head.link = process
                self._head.prev = process
            else:
                current = self._head
                while current.link is not self._head: #waits until end value, then makes that link the process
                    current = current.link
                current.link = process  #last value is process now, makes last value link process
                process.prev = current  #previous process is last current value
                process.link = self._head 
            self._d_processes[(process.pid)] = process
            self._head.prev = process
            self._len += 1

    def kill(self, pid): 
        '''removes process on basis of pid'''

        if pid in self._d_processes: #dictionary hashmap, searching O(1)
            x = self._d_processes[pid] #unordered O(1)
            self.remove_process(x)
            

    def remove_process(self, process):
        '''removes process based on process entered'''

        if len(self) == 1:
            self._head = None
        else:  
            process.prev.link = process.link #skips process
            process.link.prev = process.prev
            if process == self._head:
                self._head = process.link

        self._len -= 1
        del self._d_processes[process.pid]

    
    def __len__(self):
        '''returns length of queue as methods keep track of it'''
        
        return(self._len)
        
          
    def run(self, n_cycles):
        """Runs circular queue for n_cycles, giving each process 1 cycle at a time"""
        n_remaining = n_cycles
        return_strings = []   # Using an intermediate list since appending to a string is O(n)

        while n_remaining:
            self._head.cycles -= 1

            if self._head.cycles == 0:
                return_strings.append(f"{self._head.pid} finished after {n_cycles-n_remaining+1} computational cycles.")
                self.remove_process(self._head)

            else:
                self._head = self._head.link
            
            n_remaining -= 1

        return '\n'.join(return_strings)
    
    def __repr__(self):
        '''Defines representation of CQ checks through every process in the dictionary of processes'''
        
        processlist = []
        for value in self._d_processes.values():
            processlist.append(str(value))
        return(f"CircularQueue({', '.join(processlist)}")

