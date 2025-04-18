class DLLNode:
    def __init__(self, item, link=None, prev=None):
        self.item = item
        self.link = link
        self.prev = prev

    def __repr__(self):
        return f"DLLNode({self.item})"

class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._len = 0

    def __len__(self):
        return self._len

    def __repr__(self):
        return f"DoublyLinkedList: head-->{self._head}, tail-->{self._tail}"

    def add_first(self, item):
        """Adds node to front of DLL"""
        node = DLLNode(item, self._head, None) 

        if self._len == 0:  # Empty list case
            self._head = node
            self._tail = node
        else:  # Standard case
            self._head.prev = node
            self._head = node
        
        self._len += 1

    def remove_first(self):
        """Removes and returns first item from DLL"""
        if self._len == 0:
            raise Exception("List is empty")

        item = self._head.item
        self._head = self._head.link  # Move head forward

        if self._head is not None:  
            self._head.prev = None
        else:  
            self._tail = None  # If list becomes empty

        self._len -= 1
        return item
