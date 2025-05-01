
from entry import Entry

class Heap:
    def __init__(self):
        """Initalzes the Heap Tree"""

        self._L = list()
        self._idx = dict()

    def __len__(self):
        """Returns length of entries"""

        return(len(self._L))

    def __iter__(self):
        """Yields every item until empty, from least to great"""

        while len(self._L) > 0:
            yield self.remove_min()

    def idx_parent(self, idx):
        '''Finds parent index using formula'''

        parent = (idx - 1) // 2
        return parent if 0 <= parent < len(self._L) else None

    def idx_left(self, idx):
        '''Finds left index using formula'''    

        left = 2 * idx + 1
        return left if left < len(self._L) else None

    def idx_right(self, idx):
        '''Finds right index using formula'''

        right = 2 * idx + 2
        return right if right < len(self._L) else None

    def idx_min_child(self, idx):
        """Find min child"""

        left = self.idx_left(idx)
        right = self.idx_right(idx)
        if left is None and right is not None:
            return right
        if right is None and left is not None:
            return left
        if right is None and left is None:
            return None
        if self._L[left] > self._L[right]:
            return right
        return left
    
    def insert(self, item, priority):
        """Inserts a item into the queue"""

        entry = Entry(item, priority)
        self._L.append(entry)
        index = len(self._L) - 1
        self._idx[item] = index
        self._upheap(index)
    
    def remove_min(self):
        """Removes minimum value"""

        if not self._L:
            return None

        value = self._L[0]
        last_index = len(self._L) - 1

        if len(self._L) == 1:
            self._L.pop()
            self._idx.pop(value.item)
            return value

        self._swap(0, last_index)
        self._L.pop()
        self._idx.pop(value.item)
        self._downheap(0)
        return value
        
    def change_priority(self, item, priority):
        """Changes priority of item"""

        if item not in self._idx:
            return False  

        idx = self._idx[item]
        old_priority = self._L[idx].priority
        self._L[idx].priority = priority

        if priority < old_priority:
            self._upheap(idx)
        else:
            self._downheap(idx)
        return self._idx[item]

    def _swap(self, i, j):
        """Swaps i-hat and j-hat in the tree, private since only for keeping completeness"""

        self._L[i], self._L[j] = self._L[j], self._L[i]
        self._idx[self._L[i].item] = i
        self._idx[self._L[j].item] = j

    def _upheap(self, idx):
        """Upheaps values in the heap"""

        parent = self.idx_parent(idx)
        if parent is not None and self._L[idx] < self._L[parent]:
            self._swap(idx, parent)
            self._upheap(parent)

    def _downheap(self, idx):
        """Downheaps values in the heap"""

        child_of_interest = self.idx_min_child(idx)
        if child_of_interest is not None and self._L[child_of_interest] < self._L[idx]:
            self._swap(idx, child_of_interest)
            self._downheap(child_of_interest)

    @staticmethod
    def heapify(entries):
        """Heapfies the heapmap"""

        heap = Heap()
        heap._L = entries[:]  
        heap._idx = {entry.item: i for i, entry in enumerate(heap._L)}
        for i in reversed(range(len(heap._L) // 2)):
            heap._downheap(i)
        return heap