
import unittest, random
from dictionary_bst import Node
from dictionary_bst import DictionaryBST

class TestNode(unittest.TestCase):

    def test_node_init(self):
        '''Tests to see if node properties work as intended'''

        test_node = Node('Modric', 'The greatest midfielder')
        self.assertEqual(test_node.word, 'Modric')
        self.assertEqual(test_node.meaning, 'The greatest midfielder')

class TestDictionaryBST(unittest.TestCase):

    def test_Dictionary_empty_init(self):
        '''Tests to see if dictionary intialzed works properly'''

        new_dict = DictionaryBST()
        self.assertIsNone(new_dict.entries)

    def test_Dictionary_one_item(self):
        '''Sees if one item works right'''

        entry = {'POAK': 'Winner of Greek Super League'} 
        new_dict = DictionaryBST(entry)
        self.assertEqual(new_dict.search('POAK'), 'Winner of Greek Super League')

        new_dict.insert('POAK', 'Winner of Greek Super League 2023/24')
        self.assertEqual(new_dict.search('POAK'), 'Winner of Greek Super League 2023/24')
    
    def test_Dictionary_adding_many_items(self):
        '''Sees if everything runs smoothly when many items added to dictionary'''

        entries = {
        'Leverkusen': 'Title Holder of Bundesliga',
        'Dinamo Zagreb': 'Title Holder of HNL',
        'Internazionale de Milano': 'Title Holder of Serie A'
        }

        new_dict = DictionaryBST(entries)
        self.assertEqual(new_dict.search('Internazionale de Milano'), 'Title Holder of Serie A')

        new_dict.insert('Galatasary', 'Title Holder of Turkish Super Lig')
        self.assertEqual(new_dict.search('Galatasary'), 'Title Holder of Turkish Super Lig') 
        #Sees if insert and dictionary initialzer both insert correctly
        
        Alphabetical = [
            ('Dinamo Zagreb', 'Title Holder of HNL'), 
            ('Galatasary', 'Title Holder of Turkish Super Lig'),
            ('Internazionale de Milano', 'Title Holder of Serie A'), 
            ('Leverkusen', 'Title Holder of Bundesliga')
        ]
        self.assertEqual(new_dict.print_alphabetical(), Alphabetical)

    def test_balance(self):
        '''Sees if adding many things maintains balance'''

        new_dict = DictionaryBST()
        n = 1000
        for i in range(n):
            i = random.randrange(0, 1000000)
            new_dict.insert(str(i), str(i+3))
        self.assertTrue(new_dict.is_balanced())

if __name__ == '__main__':
    unittest.main()