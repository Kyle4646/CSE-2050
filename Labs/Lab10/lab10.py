
class Entry:

    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def __lt__(self, other):
        if self.priority < other.priority:
            return(True)
        return(False)
    
    def __eq__(self, other):
        if self.priority == other.priority and self.item == other.item:
            return(True)
        return(False)
    
class PQ_UL:
    
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def insert(self, item, priority):
        self.data.append(Entry(item, priority))

    def find_min(self):
        self.data.sort()
        min = self.data[0]
        return min

    def remove_min(self):
        min_index = 0
        for i in range(1, len(self.data)):
            if self.data[i].priority < self.data[min_index].priority:
                min_index = i
        return self.data.pop(min_index)

class PQ_OL:
    
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def insert(self, item, priority):
        new_entry = Entry(item, priority)
        index = 0
        while index < len(self.data) and self.data[index].priority <= priority:
            index += 1
        self.data.insert(index, new_entry)

    def find_min(self):
        if not self.data:
            return None
        return self.data[0]

    def remove_min(self):
        if not self.data:
            return None
        return self.data.pop(0)