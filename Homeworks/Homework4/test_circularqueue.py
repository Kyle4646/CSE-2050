
import unittest
import process
import circularqueue

from process import Process
from circularqueue import CircularQueue

class TestCircularQueue(unittest.TestCase):
    
    def test_initializer_empty(self):
        '''checks to see if Circular Queue initialzer works'''

        CQ1 = CircularQueue()
        self.assertEqual(CQ1._head, None)
        self.assertEqual(CQ1._len, 0)

    
    def test_initializer_one(self):
        '''checks to see if Circular Queue initialzer works if has item'''

        process1 = [Process('openXL', 70)]
        CQ1 = CircularQueue(process1)
        self.assertEqual(CQ1._head, Process('openXL', 70))
        self.assertEqual(CQ1._len, 1)
    
    
    def test_add_one_item(self):
        '''checks if one item links and prevs itself'''
        
        process1 = [Process('openXL', 70)]
        CQ = CircularQueue(process1)
        self.assertEqual(CQ._head, Process('openXL', 70)) #sees first process links to itself
        self.assertEqual(CQ._head.link, Process('openXL', 70))
        self.assertEqual(CQ._head.prev, Process('openXL', 70))
        self.assertEqual(len(CQ), 1)
        

    def test_add_two_object(self):
        '''sees if adding two items works properly'''

        process1 = Process('openXL', 10)
        process2 = Process('openDoc', 8)
        processlist = [process1, process2]
        CQ = CircularQueue(processlist)
        self.assertEqual(CQ._head, process1)
        self.assertEqual(CQ._head.link, process2)
        self.assertEqual(CQ._head.prev, process2)
        self.assertEqual(len(CQ), 2)

    def test_add_three_object(self):
        '''sees if adding three items works properly'''

        process1 = Process('openXL', 10)
        process2 = Process('openDoc', 8)
        process3 = Process('openSheets', 12)
        processlist = [process1, process2, process3]
        CQ = CircularQueue(processlist)
        self.assertEqual(CQ._head, process1)
        self.assertEqual(CQ._head.link, process2) #head links to process2, in last
        self.assertEqual(CQ._head.prev, process3)
        self.assertEqual(len(CQ), 3)
        self.assertEqual(process3.prev, process2)
        self.assertEqual(process2.link, process3)

    def test_add_duplicates(self):
        '''tests to see if adding duplicates correctly does not make all items
        uses this on basis of same pip'''
        
        process1 = Process('openXL', 10)
        process2 = Process('openSheets', 20)
        process3 = Process('openXL', 20)
        processlist = [process1, process2, process3]
        processlist = processlist
        CQ = CircularQueue(processlist)
        self.assertEqual(len(CQ), 2)
        self.assertEqual(process1.prev, process2) #makes sure process3 converted to 1

    def test_remove_one_process(self):
        '''sees if removing one item works properly'''

        processlist = [Process('die', 46)]
        CQ = CircularQueue(processlist)
        CQ.remove_process(processlist[0])
        self.assertEqual(len(CQ), 0)
        self.assertEqual(CQ._head,  None)

    def test_remove_multi_process_middle(self):
        '''sees if removing one item in middle works properly'''

        process1 = Process('openDocs', 10)
        process2 = Process('openXL', 8)
        process3 = Process('openSheets', 12)
        processlist = [process1, process2, process3]
        CQ = CircularQueue(processlist)
        CQ.remove_process(process2)
        self.assertEqual(CQ._head, process1)
        self.assertEqual(CQ._head.link, process3)
        self.assertEqual(CQ._head.prev, process3)
        self.assertEqual(len(CQ), 2)

    def test_remove_multi_process_head(self):
        '''sees if removing one item works properly and alters head'''

        process1 = Process('openXL', 10)
        process2 = Process('openSheets', 8)
        process3 = Process('openPaint', 12)
        processlist = [process1, process2, process3]
        CQ3 = CircularQueue(processlist)
        CQ3.remove_process(process1)
        self.assertEqual(CQ3._head, process2)
        self.assertEqual(CQ3._head.link, process3)
        self.assertEqual(CQ3._head.prev, process3)
        self.assertEqual(len(CQ3), 2)

    def test_remove_multi_process_last(self):
        '''sees if removing last item works properly'''

        process1 = Process('openPaint', 10)
        process2 = Process('openXL', 8)
        process3 = Process('openL', 12)
        processlist = [process1, process2, process3]
        CQ3 = CircularQueue(processlist)
        CQ3.remove_process(process2)
        self.assertEqual(CQ3._head, process1)
        self.assertEqual(CQ3._head.link, process3)
        self.assertEqual(CQ3._head.prev, process3)
        self.assertEqual(len(CQ3), 2)

    def test_remove_multi_process_more(self):
        '''bonus to see if runs properly with many processes'''

        process1 = Process('openPhoto', 10)
        process2 = Process('openFile', 8)
        process3 = Process('openVideo', 12)
        process4 = Process('closeMovie', 40)
        processlist = [process1, process2, process3, process4]
        CQ3 = CircularQueue(processlist)
        CQ3.remove_process(process3)
        self.assertEqual(CQ3._head, process1)
        self.assertEqual(CQ3._head.link, process2)
        self.assertEqual(CQ3._head.prev, process4)
        self.assertEqual(process2.link, process4)
        self.assertEqual(len(CQ3), 3)

    def test_kill(self):
        '''sees if killing on basis of pid works'''
        
        process1 = Process('video1', 10)
        process2 = Process('video2', 8)
        process3 = Process('video3', 12)
        processlist = [process1, process2, process3]
        CQ3 = CircularQueue(processlist)
        CQ3.kill('video2')
        self.assertEqual(CQ3._head, process1)
        self.assertEqual(CQ3._head.link, process3)
        self.assertEqual(CQ3._head.prev, process3)
        self.assertEqual(len(CQ3), 2)

    def test_repr(self):
        '''Tests to see is cq represented properly'''
        
        process1 = Process('openGame1', 10)
        process2 = Process('openGame2', 8)
        process3 = Process('openGame3', 12)
        processlist = [process1, process2, process3]
        CQ3 = CircularQueue(processlist)
        self.assertEqual(repr(CQ3), 'CircularQueue(Process(openGame1,10), Process(openGame2,8), Process(openGame3,12)')

    def test_hw4_example(self): 
        '''same overall test on homework, bonus test to make sure everything good'''

        p1 =Process('send_email',250)
        p2 =Process('open_word',100)
        p3 =Process('run_simulation',1000)
        cq =CircularQueue([p1,p2,p3])
        self.assertEqual(repr(cq), 'CircularQueue(Process(send_email,250), Process(open_word,100), Process(run_simulation,1000)')

        c1 =CircularQueue()
        c1.add_process(Process("send_email"))
        c1.add_process(Process("open_word"))
        c1.add_process(Process("simulate_transistor_fabrication"))
        self.assertEqual(len(cq), 3)


if __name__ == '__main__':
    unittest.main()