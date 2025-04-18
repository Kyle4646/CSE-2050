
import unittest
from linkedlist import Node
from linkedlist import LinkedList

class TestNode(unittest.TestCase):
    
    def test_nodeinit(self):
        '''tests if node initializer is correct'''

        testnode = Node('Wolfsburg')
        self.assertEqual(testnode.item, 'Wolfsburg')
        self.assertEqual(testnode.link, None)

    
    def test_noderepr(self):
        '''tests if repr function works properly'''

        testnode = Node('Hoffeinheim')
        self.assertEqual(repr(testnode), 'Node(Hoffeinheim)')

class TestLinkedList(unittest.TestCase):

    def test_linkedlistinit(self):
        '''tests if linked list initialized as empty'''

        LL1 = LinkedList()
        self.assertEqual(len(LL1), 0)
        self.assertEqual(LL1.get_head(), None)
        self.assertEqual(LL1.get_tail(), None)

    
    def test_add_last(self):
        '''tests if see if it adds to end of linked list properly'''

        LL1 = LinkedList()
        
        for num in range(1, 20):
            LL1.add_last(num)
            self.assertEqual(len(LL1), num)
            self.assertEqual(LL1.get_head(), 1)
            self.assertEqual(LL1.get_tail(), num)

    
    def test_add_first(self):
        '''tests if see if it adds to beginning of linked list properly'''

        LL1 = LinkedList()
        
        for num in range(1, 20):
            LL1.add_first(num)
            self.assertEqual(len(LL1), (num))
            self.assertEqual(LL1.get_head(), num)
            self.assertEqual(LL1.get_tail(), 1)

   
    def test_nonemptyinit(self):
        '''tests if non empty initialzer works'''

        LL1 = LinkedList(range(10))
        liste = ['hello', 'hi', 'yo']
        LL2 = LinkedList(liste)
        LL3 = LinkedList()
        
        self.assertEqual(len(LL1), 10)
        self.assertEqual((LL1.get_head()), 0)
        self.assertEqual((LL1.get_tail()),9)

        self.assertEqual(len(LL2), 3)
        self.assertEqual((LL2.get_head()), 'hello')
        self.assertEqual((LL2.get_tail()), 'yo')
    
    
    def test_remove_first(self):
        '''tests to see if first value is removed properly'''
        
        LL1 = LinkedList()
        self.assertRaises(RuntimeError, LL1.remove_first)
        
        LL2 = LinkedList(range(20))
        for num in range(19):
            self.assertEqual(LL2.remove_first(), num)
            self.assertEqual(len(LL2), 19 - num)
            self.assertEqual((LL2.get_head()), 1 + num)
            self.assertEqual((LL2.get_tail()), 19)
        LL2.remove_first()
        self.assertEqual(LL2._head, None) #checks if empty list after removing everything gives empty head and tail
        self.assertEqual(LL2._tail, None)

    
    def test_remove_last(self):
        '''tests to see if last value is removed properly'''
        
        LL1 = LinkedList()
        self.assertRaises(RuntimeError, LL1.remove_last)
        
        LL2 = LinkedList(range(20))
        counter = 0
        for num in range(19):
            self.assertEqual(LL2.remove_last(), 19 - num)
            self.assertEqual(len(LL2), 19 - num)
            self.assertEqual(LL2.get_head(), 0)
            self.assertEqual(LL2.get_tail(), 18 - num)
        LL2.remove_first()
        self.assertEqual(LL2._head, None)
        self.assertEqual(LL2._tail, None)


if __name__ == '__main__':
    unittest.main()

