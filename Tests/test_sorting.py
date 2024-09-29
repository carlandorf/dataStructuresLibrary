# tests/test_sorting.py

import unittest
import sys
import os

# Add the parent directory to the system path to resolve the import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the sorting functions from the Algorithms module
from Algorithms.sorting import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    heap_sort,
)

class TestSortingAlgorithms(unittest.TestCase):
    
    def setUp(self):
        """Setup unsorted arrays for testing."""
        print("\nSetting up arrays for sorting tests...")
        self.arr1 = [64, 34, 25, 12, 22, 11, 90]
        self.arr2 = [4, 2, 2, 8, 3, 3, 1]
        self.arr_sorted1 = sorted(self.arr1)
        self.arr_sorted2 = sorted(self.arr2)

    def test_bubble_sort(self):
        """Test bubble sort algorithm."""
        print("Testing bubble sort...")
        self.assertEqual(bubble_sort(self.arr1[:]), self.arr_sorted1)
        self.assertEqual(bubble_sort(self.arr2[:]), self.arr_sorted2)

    def test_selection_sort(self):
        """Test selection sort algorithm."""
        print("Testing selection sort...")
        self.assertEqual(selection_sort(self.arr1[:]), self.arr_sorted1)
        self.assertEqual(selection_sort(self.arr2[:]), self.arr_sorted2)

    def test_insertion_sort(self):
        """Test insertion sort algorithm."""
        print("Testing insertion sort...")
        self.assertEqual(insertion_sort(self.arr1[:]), self.arr_sorted1)
        self.assertEqual(insertion_sort(self.arr2[:]), self.arr_sorted2)

    def test_merge_sort(self):
        """Test merge sort algorithm."""
        print("Testing merge sort...")
        self.assertEqual(merge_sort(self.arr1[:]), self.arr_sorted1)
        self.assertEqual(merge_sort(self.arr2[:]), self.arr_sorted2)

    def test_quick_sort(self):
        """Test quick sort algorithm."""
        print("Testing quick sort...")
        self.assertEqual(quick_sort(self.arr1[:]), self.arr_sorted1)
        self.assertEqual(quick_sort(self.arr2[:]), self.arr_sorted2)

    def test_heap_sort(self):
        """Test heap sort algorithm."""
        print("Testing heap sort...")
        self.assertEqual(heap_sort(self.arr1[:]), self.arr_sorted1)
        self.assertEqual(heap_sort(self.arr2[:]), self.arr_sorted2)

if __name__ == '__main__':
    unittest.main()