
class LazyQueue:

    def __init__(self):
        '''Initialzes head and list'''
        self._head = 0
        self._L = []
    
    def enqueue(self, item):
        '''Adds item to end of queue'''
        
        self._L.append(item)

    def dequeue(self):
        '''Lazily removes items on average in O(1) by changing head'''

        item = self.peek()
        self._head += 1
        if self._head > len(self._L)//2:
            self._L = self._L[self._head:]
            self._head = 0
        return item

    def peek(self):
        '''Peeks to head'''

        return self._L[self._head]

    def __len__(self):
        '''Returns len of list'''

        return len(self._L) - self._head

    def isEmpty(self):
        '''Returns if queue empty'''

        return len(self) == 0