
import unittest
from hw3 import generate_lists
from hw3 import find_common
from hw3 import find_common_efficient

class TestGenerateLists(unittest.TestCase):

    def test_unique_integers(self):
        '''Tests to see if items in list are unique'''
        
        checker = True
        
        listtuple = generate_lists(6)
        for list in listtuple:
            if len(list) != len(set(list)): #set removes duplicates so set length should equal list length
                checker = False
        self.assertEqual(checker, True)

    
    def test_unique_integers_wrong(self):
        '''Tests to see if items in list are unique and give wrong answers'''
        
        checker = True
        
        listtuple = generate_lists(6)
        for list in listtuple:
            if len(list) != len(set(list)):
                checker = False
        self.assertNotEqual(checker, False)


    def test_correct_size(self):
        '''Tests to see if lists are the correct size'''

        checker = True
        lists = generate_lists(7)
        
        for list in lists:
            if (len(list) != 7):
                checker = False #does loop to make sure each one is correct size 
        self.assertEqual(checker, True)


    def test_correct_size_II(self):
        '''Tests to see if lists are the correct size'''

        checker = True
        lists = generate_lists(0)
        
        for list in lists:
            if (len(list) != 0):
                checker = False
        self.assertEqual(checker, True)


        
class TestFindtCommon(unittest.TestCase):

    def test_pass(self):
        '''Tests to see if lists given returns number of correct commanalilties'''
        
        list1 = [1, 2, 3, 4, 5]
        list2 = [2, 3, 5, 7]
        self.assertEqual(find_common(list1, list2), 3)

    
    def test_fail(self):
        '''Tests to see if its exact and does not return true if wrong commanilities given'''

        list1 = [5, 6, 7, 8, 9]
        list2 = [5, 7, 8, 10, 11, 9]
        self.assertNotEqual(find_common(list1, list2), 3)


    def test_empty(self):
        '''Sees is empty list gives error or 0'''

        list1=[]
        list2=[]
        self.assertEqual(find_common(list1, list2), 0)
        


class TestFindCommonEfficient(unittest.TestCase):

    def test_first(self):
        '''Tests to see if lists given returns number of correct commanalilties'''
    
        list1 = [1, 2, 3, 4, 5]
        list2 = [2, 3, 5, 7]
        self.assertEqual(find_common_efficient(list1, list2), 3)

    
    def fail_test(self):
        '''Tests to see if its exact and does not return true if wrong commanilities given'''
    
        list1 = [5, 6, 7, 8, 9]
        list2 = [5, 7, 8, 10, 11, 9]
        self.assertNotEqual(find_common(list1, list2), 3)


    def test_empty(self):
        '''Sees is empty list gives error or 0'''

        list1=[]
        list2=[]
        self.assertEqual(find_common_efficient(list1, list2), 0)

    
if __name__ == '__main__':
    unittest.main()
        
