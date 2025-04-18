###############################################################################
# init, and repr  are implemented for you. You should implement the other     #
# methods recursively.                                                        #
###############################################################################
class Node:
    """Reucrsively implementes Linked List functionality"""
    def __init__(self, data, link=None):
        """Instantiates a new Node with given data"""
        self.data = data
        self.link = link

    def __repr__(self):
        """Returns string representation of node"""
        return f"Node({self.data})"
    
    def __len__(self):
        """Recursively calculates length of sublist starting at this node"""

        if self.link is None: #base case
            return(1)
        return(1 + len(self.link)) #Keeps calling len until it reaches tail

    def get_tail(self):
        """Recursively finds the data stored in the tail of this sublist"""
    
        if self.link is None:
            return(self.data) #goes until it finds tail
        return(self.link.get_tail())

    def add_last(self, data):
        """Recursively adds to end of this sublist"""

        if self.link is None:
            self.link = Node(data)
        else:
            return(self.link.add_last(data))

    def total(self):
        """Recusrively adds all items"""
        summe = 0

        if self.link is None:
            return(self.data)
        return(self.data + self.link.total()) #similar to length but uses data to contunously add.

    def remove_last(self):
        """Recursively removes last item in sublist
            Returns a tuple of (new_head, data). The new_head is the
            new head of this sublist after removing the tail.

            OUTPUT
            ------
            new_head, tail_data
                * new_head: Node or None
                    The new link for whatever node called this function
                
                * tail_data: Any
                    The data that was found in the tail node
        """
    
        if self.link is None: #only ever triggers if one object
            return(None, self.data)
        if self.link.link is None:
            data = self.link.data
            self.link = None
            return(self, data)
        new_head, tail_data = self.link.remove_last()
        self.link = new_head #Continously makes self's link the head, thus storing it
        return(self, tail_data)

    def reverse(self, prev = None):
        """Recursively reverse list"""

        if self.link is None:
            self.link = prev
            return(self)
        else:
            curr = self.link #stores link
            self.link = prev
            return(curr.reverse(self))


