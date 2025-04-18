from solve_puzzle import solve_puzzle as puzzle
import unittest

class TestSolvePuzzle(unittest.TestCase):
        def testClockwise(self):
                """Tests a board solveable using only CW moves"""

                liste = [3, 1, 2, 0]
                self.assertEqual(puzzle(liste), True)


        def testCounterClockwise(self):
                """Tests a board solveable using only CCW moves"""

                liste = [1, 2, 8, 7, 4, 0]
                self.assertEqual(puzzle(liste), True)


        def testMixed(self):
                """Tests a board solveable using only a combination of CW and CCW moves"""
        
                liste = [4, 3, 2, 5, 5, 0]
                self.assertEqual(puzzle(liste), True)
        
        def testUnsolveable(self):
                """Tests an unsolveable board"""

                liste = [3, 4, 1, 2, 0]
                self.assertEqual(puzzle(liste), False)

if __name__ == '__main__':
    unittest.main()