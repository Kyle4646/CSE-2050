
class LocalRecord:
    def __init__(self, pos, max=None, min=None, precision = 0):
        '''Initialzes variables of record'''
        
        self.pos = self._round(pos, precision)
        self.max = max
        self.min = min
        self.precision = precision

    def _round(self, pos, precision = 0):
        '''Rounds values on basis of precision'''

        return((round(pos[0], precision)), round(pos[1], precision))

    def add_report(self, temp):
        '''If we have a new temperature report in area, changes max or min if needed'''
        
        if self.max is None and self.min is None:
            self.max = temp
            self.min = temp
            return
        
        if temp >= self.min and temp <= self.max: return #if in established range, do nothing 
        if self.min == self.max and temp > self.max:
            self.max = temp
        if temp < self.min:
            self.min = temp
        if temp > self.max:
            self.max = temp
        
    def __eq__(self, other):
        '''If position similar enough, say they are equal'''
        
        if (self.pos[0] == other.pos[0]) and (self.pos[1] == other.pos[1]):
            return(True)
        return(False)

    def __hash__(self): 
        '''Returns hash value for tuple'''

        return(hash(self.pos))

    def __repr__(self):
        '''Returns representation of Record'''

        return f"Record(pos={self.pos}, max={self.max}, min={self.min}"

class RecordsMap:
    def __init__(self):
        '''Initialzer for record map'''

        self._min_buckets = 8
        self._n_buckets = 8
        self._len = 0
        self._L = [[] for i in range(self._n_buckets)]

    def _find_bucket(self, pos):
        '''Finds what bucket index pos belongs in'''

        bucket = hash(pos) % self._n_buckets
        return(bucket)

    def __len__(self): 
        '''Returns length of record map'''

        return(self._len)

    def add_report(self, pos, temp):
        '''Adds report to mapping. If already in mapping, sets that record's new temp.
        Otherwise makes a new record'''

        temprecord = LocalRecord(pos)
        bucket = self._find_bucket(temprecord.pos) #uses rounded position, otherwise will be in completley different bucket than potential matching pos
        for record in self._L[bucket]:
            if record == temprecord:
                record.add_report(temp)
                #searches in bucket to see if record in map already and sets value, same value is same bucket
                return
            
        newrecord = LocalRecord(pos)
        newrecord.add_report(temp)
        self._L[bucket].append(newrecord)
        self._len += 1

        load_factor = len(self) / self._n_buckets
        if load_factor >= 2:
            self._rehash(2 * self._n_buckets)

    def __getitem__(self, pos): 
        '''Returns temp from position'''
        
        temprecord = LocalRecord(pos)
        bucket = self._find_bucket(temprecord.pos)
        for record in self._L[bucket]:
            if record == temprecord:
                return(record.min, record.max)
            
        raise KeyError('Position not in our data base, want to add it?')
  
    def __contains__(self, pos): 
        '''Sees if pos is in the RecordsMap'''
        
        temprecord = LocalRecord(pos)
        bucket = self._find_bucket(temprecord.pos)
        for record in self._L[bucket]:
            if record == temprecord:
                return True
        return False

    def _rehash(self, m_new):
        '''Rehashes and assigns new buckets'''
        
        new_buckets = [[] for i in range(m_new)]

        for bucket in self._L:
            for item in bucket:
                new_bucket_idx = hash(item) % m_new
                new_buckets[new_bucket_idx].append(item) #O(n) searches through every item

        self._L = new_buckets
        self._n_buckets = m_new