import unittest
from hw6 import bubble_sort, selection_sort, insertion_sort, merge

class SortingTestFactory:
    """This class provides methods to generate test cases for sorting algorithms."""
    def setUp(self, sorting_alg):
        """
        Set up the sorting algorithm for testing.
        Args:
            sorting_alg (function): The sorting algorithm to be tested.
        """
        self.sorting_alg = sorting_alg

    def test_merge(self):
        """ Test case for the merge function to verify that it correctly merges three sorted rows."""
        # Define the sorted rows to test
        matrix = [[1, 4, 7, 10], [2, 5, 8, 11],[3, 6, 9, 12]] 
        # Expected merged result
        expected_merged = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

        # Call the merge function
        self.assertEqual(expected_merged, merge(matrix[0],matrix[1],matrix[2]))

    def is_sorted(self, L):
        """ Check if a list is sorted. """
        return all(L[i] <= L[i + 1] for i in range(len(L) - 1))

    def test_empty(self):
        """Tests an empty list and sees it returns empty list back"""

        matrix = [[],[],[]]
        new_L, numswaps = self.sorting_alg(matrix)
        self.assertEqual(new_L, [])
        self.assertEqual(numswaps, 0)

    def test_sorted(self):
        """Tests to see if an already sorted list returns correctly and has 0 swaps"""

        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        L, numswaps = self.sorting_alg(matrix)
        self.assertTrue(self.is_sorted(L))
        self.assertEqual(numswaps, 0)
    
    def test_reverse_sorted(self):
        """Tests reverse sorted items now"""

        matrix = [[4, 3, 2, 1], [4, 3, 2, 1], [4, 3, 2, 1]]
        self.assertEqual(self.sorting_alg(matrix), ([1, 2, 3, 4], 6)) #6, [4] moves 3 times to end, [3] moves 2, and [2] moves 1
    
    def test_random(self):
        """Sees if random matrix returns correct amount"""

        matrix = [[3, 5, 2, 4, 1], [2, 4, 1, 5, 3], [2, 4, 1, 5, 3]]
        L, numswaps = self.sorting_alg(matrix)
        self.assertTrue(self.is_sorted(L))
        self.assertGreater(numswaps, 0)

class TestBubble(SortingTestFactory, unittest.TestCase):
    """Test class for the bubble sort algorithm."""

    def setUp(self):
        """Set up the bubble sort algorithm for testing."""
        super().setUp(bubble_sort)

class TestInsertion(SortingTestFactory, unittest.TestCase):
    """Tests insertion sorting algorithm"""

    def setUp(self):
        '''Sets up insertion sort for testing'''
        super().setUp(insertion_sort)

class TestSelection(SortingTestFactory, unittest.TestCase):
    """Tests selection sorting algorithm"""

    def setUp(self):
        '''Sees is selection algorithm works'''
        super().setUp(selection_sort)

    def test_reverse_sorted(self):
        '''Tests to see if reverse selection works, should be less than
        bubble/insertion'''
        
        matrix = [[4, 3, 2, 1], [8, 7, 6, 5], [12, 11, 10, 9]]
        self.assertEqual(selection_sort(matrix), ([9, 10, 11, 12], 2))

    def test_random_sorted(self):
        '''Tests random for selection'''

        matrix = [[10, 2, 3, 7, 1], [7, 15, 14, 20, 8], [25, 13, 5, 3, 16]]
        self.assertEqual(selection_sort(matrix), ([3, 5, 13, 16, 25], 3))

if __name__ == "__main__":
    unittest.main()