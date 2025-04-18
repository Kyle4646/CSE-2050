
import unittest
import circularqueue
import process

from process import Process
from circularqueue import CircularQueue


class TestProcess(unittest.TestCase):
    '''Tests to see if initializer properly works'''

    def test_initialpidcheck(self):
        '''checks to see if pid matches one entered. Also checks if cycles default 100'''

        processtest = Process('test if works')
        self.assertEqual(processtest.pid, 'test if works')
        self.assertEqual(processtest.cycles, 100)

    
    def test_initialpidandcycle(self):
        '''checks to see if initial pid and cycle match one entered. 
        Also sees if link prev intiialzed to None'''

        processtest = Process('atest', 800)
        self.assertEqual(processtest.pid, 'atest')
        self.assertEqual(processtest.cycles, 800)
        self.assertEqual(processtest.link, None)
        self.assertEqual(processtest.prev, None)

    
    def test_eq_function(self):
        '''checks to see if Processes with same pin are equal'''

        process1 = Process('OpenXL', 40)
        process2 = Process('OpenXL', 60)
        self.assertEqual(process1, process2)


    def test_eq_function_wrong(self):
        '''checks to see if Processes with same pin are not equal'''

        process1 = Process('OpenXL', 40)
        process2 = Process('OpenWord', 60)
        self.assertNotEqual(process1, process2)

    
    def test_repr_function(self):
        '''checks if rep puts out correct string'''

        process1 = Process('OpenXL')
        process2 = Process('OpenWord', 60)
        self.assertEqual(repr(process1), ('Process(OpenXL,100)')) 
        self.assertEqual(repr(process2), ('Process(OpenWord,60)'))
   
if __name__ == '__main__':
    unittest.main()