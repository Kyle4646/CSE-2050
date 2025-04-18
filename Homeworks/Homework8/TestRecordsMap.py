# Import what you need
# Include unittests here. Focus on readability, including comments and docstrings.
import unittest
from RecordsMap import LocalRecord
from RecordsMap import RecordsMap
import time
import random

class TestLocalRecord(unittest.TestCase):
    def test_init_only_pos(self):
        """Tests to see if initialzer works properly"""

        record1 = LocalRecord((120, 560))
        self.assertEqual(str(repr(record1)), 'Record(pos=(120, 560), max=None, min=None')
        self.assertEqual(record1.precision, 0)

    def test_init_all(self):
        '''Tests if other variables work properly if manually entered'''
        
        record1 = LocalRecord((120.44, 560.22), 10, 11, 2)
        self.assertEqual(str(repr(record1)), 'Record(pos=(120.44, 560.22), max=10, min=11')
        self.assertEqual(record1.precision, 2)

    def test_hash(self):
        """Sees if hashes work properly"""

        record1 = LocalRecord((120.44, 560.62))
        record2 = LocalRecord((120.1, 561.2))
        record3 = LocalRecord((120.2, 600))

        self.assertEqual(hash(record1), hash(record2))
        self.assertEqual(hash(record1), -2435597166931524554)
        self.assertNotEqual(hash(record1), hash(record3))
    
    def test_eq_0_precision(self):
        """Tests to see if similar reports are considered equal"""

        record1 = LocalRecord((120.44, 560.62))
        record2 = LocalRecord((120.1, 561.2))
        record3 = LocalRecord((120.2, 600))
        
        self.assertEqual(record1, record2)
        self.assertNotEqual(record1, record3) 

    def test_eq_set_precision(self):
        '''Tests to see if same records work under more strict precision'''

        record1 = LocalRecord((120.4455, 560.6299), precision = 2)
        record2 = LocalRecord((120.4499, 560.6311), precision = 2)
        record3 = LocalRecord((120.2111, 600.4444), precision = 2)
        
        self.assertEqual(record1, record2)
        self.assertNotEqual(record1, record3)

    def test_add_report(self):
        """Tests to see if adding report changes max/min properly"""

        record1 = LocalRecord((120, 560), 100, 1)
        record1.add_report(8)
        self.assertEqual(record1.max, 100)
        self.assertEqual(record1.min, 1) #if in range, see if nothing changes

        record1.add_report(101)
        self.assertEqual(record1.max, 101)
        self.assertEqual(record1.min, 1)

        record1.add_report(-2)
        self.assertEqual(record1.min, -2)
        self.assertEqual(record1.max, 101)

        record1.add_report(100)
        self.assertEqual(record1.max, 101)
        self.assertEqual(record1.min, -2) #see if values save

    def test_add_report(self):
        '''Tests add report for a record with no recorded temp'''

        record1 = LocalRecord((20, 50))
        record1.add_report(24)
        self.assertEqual(record1.max, 24)
        self.assertEqual(record1.min, 24)

        record1.add_report(28)
        self.assertEqual(record1.max, 28)
        self.assertEqual(record1.min, 24)

class TestRecordsMap(unittest.TestCase):

    def test_TestRecordMap_empty(self):
        '''Tests to see if initialzer works on empty map'''

        weather_map = RecordsMap()
        self.assertEqual(len(weather_map), 0) #tests to see if len is 0 initally

    def test_add_one_report(self):
        """Tests to see if adding a report works properly"""

        recordmap = RecordsMap()
        self.assertEqual(len(recordmap), 0)
        p1 = (20, 40)
        self.assertFalse(p1 in recordmap)
        recordmap.add_report(p1, 4)
        self.assertTrue(p1 in recordmap)

        self.assertEqual(recordmap[p1], (4, 4))
        recordmap.add_report(p1, 8)
        self.assertEqual(recordmap[p1], (4, 8))
        self.assertEqual(len(recordmap), 1)

        p2 = (90, 99)
        with self.assertRaises(KeyError): recordmap[p2]

    def test_add_many_reports(self):
        """Sees if everything works properly when adding multiple records"""

        recordmap = RecordsMap()
        self.assertEqual(len(recordmap), 0)
        p1 = (10, 10)
        p2 = (10.1, 10.3)
        self.assertFalse(p1 in recordmap and p2 in recordmap)
        
        recordmap.add_report(p1, 99)
        self.assertTrue(p1 in recordmap and p2 in recordmap)
        self.assertEqual(recordmap[p1], (99, 99))
        recordmap.add_report(p2, 20)
        self.assertEqual(len(recordmap), 1) #sees if "equal" coordinates are considred equal
        self.assertEqual(recordmap[p2], (20, 99))

        p3 = (50, 40)
        recordmap.add_report(p3, 2)
        self.assertEqual(len(recordmap), 2)

        p4 = (40, 10.2)
        self.assertFalse(p4 in recordmap)

    def test_rehash(self):
        '''Ensures mapping is O(1). I ran my own test in a seperate file for checking if value
        in 10000000 len list, it took 0.33959 seconds to reach 99999999'''

        n = 10000000
        recordsmap = RecordsMap()
        p0 = (2000, 5000)
        recordsmap.add_report(p0, 3)
        start = time.time()
        for i in range(n):
            p1Long = random.randrange(0, 1000)
            p1Lang = random.randrange(0, 1000)
            recordsmap.add_report((p1Long, p1Lang), 9)

        start = time.time()
        recordsmap.add_report((401, 303), 1)
        end = time.time() - start
        self.assertLess(end, 0.001) #checks if adding random report to dictionary O(1)
    
        start = time.time()
        p0 in recordsmap
        end = time.time() - start
        self.assertLess(end, 0.001) #went from .33959 to less than 0.001, O(1)

        start = time.time()
        recordsmap[p0]
        end = time.time() - start
        self.assertLess(end, 0.001) #checks if retrieving item O(1)
        self.assertEqual(recordsmap[p0], (3, 3))

if __name__ == '__main__':
    unittest.main()