
class Entry:
    def __init__(self, item, priority):
        """Initalzes an entry's item and priority"""

        self.item = item
        self.priority = priority

    def __eq__(self, other):
        """Sees if two entries are equal on basis of priority"""
        if isinstance(other, Entry):
            return(self.priority == other.priority)

    def __lt__(self, other):
        """Sees if entry is less than another on basis of priority"""
        if isinstance(other, Entry):
            return(self.priority < other.priority)

    def __le__(self, other):
        """Sees if entry less than (or equal) to another on basis of priority"""
        if isinstance(other, Entry):
            return(self.priority <= other.priority)

    def __repr__(self):
        """Represents an Entry"""

        return(f'Entry(item={self.item}, priority={self.priority})')
