
import unittest
import trib 

class TestTrib(unittest.TestCase):

    def test_trib_first_ten(self):
        '''Tests to see if first 10 digits of trib are correct'''
        
        rightdict = {1:0, 2:0, 3:1, 4:1, 5:2, 6:4, 7:7, 8:13, 9:24, 10:44}
        for num in range(1, 11):
            self.assertEqual(trib.trib(num), rightdict[num])

    def test_trib_100th_value(self):
        '''Tests to see if large value runs(meaning no exponential time)
        and returns correct value'''
        
        self.assertEqual(trib.trib(100), 28992087708416717612934417)

if __name__ == '__main__':
    unittest.main()