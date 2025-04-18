
class Node:

    def __init__(self, item, link = None):
        '''Initialzes functions'''
        
        self.item = item
        self.link = link

    def __repr__(self):
        '''defines representation of instance'''

        return(f'Node({self.item})')
    

class LinkedList:

    def __init__(self, items = None):
        '''initializes functions'''
        
        self._length = 0
        self._head = None
        self._tail = None
        if items is not None:
            for item in items:
                self.add_last(item)
        
    

    def __len__(self):
        '''finds length of list'''
        
        return(self._length)
    
    def get_head(self):
        '''returns head'''
        
        if self._head is not None:
            return(self._head.item)
    
    def get_tail(self):
        '''returns tails'''
        if self._tail is not None:
            return(self._tail.item)
    
    def add_first(self, item):
        '''adds item to beginning of list'''

        self._head = Node(item, self._head) #makes link the head so head is now after it
        if self._tail is None: self._tail = self._head
        self._length += 1
   
    def add_last(self, item):
       '''adds items to end of list'''

       if self._head is None:
           self.add_first(item)
       else:
           self._tail.link = Node(item)
           self._tail = self._tail.link #makes new link for tail, thing after tail then makes that new end
           self._length += 1

    def remove_last(self):
        '''This removes last item'''
        
        if self._length == 0:
            raise RuntimeError('You cant do that')
        if self._head is self._tail: 
            return(self.remove_first())
        else:
            currentnode = self._head
            while currentnode.link is not self._tail:
                currentnode = currentnode.link #finds last item by waiting until there is no link (last item)
            store_item = self._tail.item
            self._tail = currentnode
            self._tail.link = None
            self._length -= 1
            return(store_item)
        
    def remove_first(self):
        '''Removes first item'''  
        
        if self._length == 0:
            raise RuntimeError('You cant do that')
        store_item = self._head.item
        self._head = self._head.link
        if self._head is None: 
            self._tail = None
        self._length -= 1
        return(store_item)
                        
