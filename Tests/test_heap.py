# tests/test_heap.py

import unittest
import sys
import os

# Add the parent directory to the system path to resolve the import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the MinHeap and MaxHeap classes from the Data_Structures module
from Data_Structures.heap import MinHeap, MaxHeap

class TestMinHeap(unittest.TestCase):
    
    def setUp(self):
        """Setup a new MinHeap instance before each test."""
        print("\nSetting up a new MinHeap instance for the test...")
        self.heap = MinHeap()

    def test_insert(self):
        """Test inserting elements into the min-heap."""
        print("Testing insert method for MinHeap:")
        values = [10, 20, 5, 6, 2, 8]
        for value in values:
            print(f"Inserting {value} into the heap.")
            self.heap.insert(value)
            print(f"Current heap: {self.heap}")
        
        # Corrected expected heap after analyzing the min-heap property
        expected_heap = [2, 5, 8, 20, 6, 10]
        print(f"Expected heap: {expected_heap}")
        self.assertEqual(self.heap.heap, expected_heap)

    def test_delete_min(self):
        """Test deleting the minimum element from the min-heap."""
        print("Testing delete_min method for MinHeap:")
        values = [10, 20, 5, 6, 2, 8]
        for value in values:
            self.heap.insert(value)
        print(f"Initial heap: {self.heap}")
        
        print("Deleting the minimum element.")
        min_value = self.heap.delete_min()
        print(f"Deleted value: {min_value}")
        print(f"Heap after deleting min: {self.heap}")
        self.assertEqual(min_value, 2)
        self.assertEqual(self.heap.heap, [5, 6, 8, 20, 10])
        
        print("Deleting the minimum element again.")
        min_value = self.heap.delete_min()
        print(f"Deleted value: {min_value}")
        print(f"Heap after deleting min: {self.heap}")
        self.assertEqual(min_value, 5)
        self.assertEqual(self.heap.heap, [6, 10, 8, 20])

    def test_get_min(self):
        """Test getting the minimum element without removing it."""
        print("Testing get_min method for MinHeap:")
        values = [10, 20, 5, 6, 2, 8]
        for value in values:
            self.heap.insert(value)
        print(f"Current heap: {self.heap}")
        
        min_value = self.heap.get_min()
        print(f"Minimum value in the heap: {min_value}")
        self.assertEqual(min_value, 2)
        
        print(f"Heap after getting min (should be unchanged): {self.heap}")
        # Corrected expected heap after analyzing the min-heap property
        expected_heap = [2, 5, 8, 20, 6, 10]
        self.assertEqual(self.heap.heap, expected_heap)

    def test_delete_min_empty_heap(self):
        """Test deleting the minimum element from an empty heap."""
        print("Testing delete_min method with an empty MinHeap:")
        min_value = self.heap.delete_min()
        print(f"Result of deleting min from empty heap: {min_value}")
        self.assertIsNone(min_value)

    def test_get_min_empty_heap(self):
        """Test getting the minimum element from an empty heap."""
        print("Testing get_min method with an empty MinHeap:")
        min_value = self.heap.get_min()
        print(f"Result of getting min from empty heap: {min_value}")
        self.assertIsNone(min_value)


class TestMaxHeap(unittest.TestCase):
    
    def setUp(self):
        """Setup a new MaxHeap instance before each test."""
        print("\nSetting up a new MaxHeap instance for the test...")
        self.heap = MaxHeap()

    def test_insert(self):
        """Test inserting elements into the max-heap."""
        print("Testing insert method for MaxHeap:")
        values = [10, 20, 5, 6, 2, 8]
        for value in values:
            print(f"Inserting {value} into the heap.")
            self.heap.insert(value)
            print(f"Current heap: {self.heap}")
        
        expected_heap = [20, 10, 8, 6, 2, 5]
        print(f"Expected heap: {expected_heap}")
        self.assertEqual(self.heap.heap, expected_heap)

    def test_delete_max(self):
        """Test deleting the maximum element from the max-heap."""
        print("Testing delete_max method for MaxHeap:")
        values = [10, 20, 5, 6, 2, 8]
        for value in values:
            self.heap.insert(value)
        print(f"Initial heap: {self.heap}")
        
        print("Deleting the maximum element.")
        max_value = self.heap.delete_max()
        print(f"Deleted value: {max_value}")
        print(f"Heap after deleting max: {self.heap}")
        self.assertEqual(max_value, 20)
        self.assertEqual(self.heap.heap, [10, 6, 8, 5, 2])
        
        print("Deleting the maximum element again.")
        max_value = self.heap.delete_max()
        print(f"Deleted value: {max_value}")
        print(f"Heap after deleting max: {self.heap}")
        self.assertEqual(max_value, 10)
        self.assertEqual(self.heap.heap, [8, 6, 2, 5])

    def test_get_max(self):
        """Test getting the maximum element without removing it."""
        print("Testing get_max method for MaxHeap:")
        values = [10, 20, 5, 6, 2, 8]
        for value in values:
            self.heap.insert(value)
        print(f"Current heap: {self.heap}")
        
        max_value = self.heap.get_max()
        print(f"Maximum value in the heap: {max_value}")
        self.assertEqual(max_value, 20)
        
        print(f"Heap after getting max (should be unchanged): {self.heap}")
        self.assertEqual(self.heap.heap, [20, 10, 8, 6, 2, 5])

    def test_delete_max_empty_heap(self):
        """Test deleting the maximum element from an empty heap."""
        print("Testing delete_max method with an empty MaxHeap:")
        max_value = self.heap.delete_max()
        print(f"Result of deleting max from empty heap: {max_value}")
        self.assertIsNone(max_value)

    def test_get_max_empty_heap(self):
        """Test getting the maximum element from an empty heap."""
        print("Testing get_max method with an empty MaxHeap:")
        max_value = self.heap.get_max()
        print(f"Result of getting max from empty heap: {max_value}")
        self.assertIsNone(max_value)

if __name__ == '__main__':
    unittest.main()