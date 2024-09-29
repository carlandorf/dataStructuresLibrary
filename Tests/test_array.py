# tests/test_array.py

import unittest
import sys
import os

# Add the parent directory to the system path to resolve the import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the Array class from the Data_Structures module
from Data_Structures.array import Array

class TestArray(unittest.TestCase):
    
    def setUp(self):
        """Setup a new Array instance before each test."""
        print("\nSetting up a new Array instance for the test...")
        self.array = Array()

    def test_append(self):
        """Test appending elements to the array."""
        print("Testing append method:")
        print("Appending 10 to the array.")
        self.array.append(10)
        print("Appending 20 to the array.")
        self.array.append(20)
        print(f"Current array: {self.array}")
        self.assertEqual(self.array.data, [10, 20])
        self.assertEqual(self.array.size, 2)

    def test_insert(self):
        """Test inserting elements at specific indices."""
        print("Testing insert method:")
        print("Appending 10 to the array.")
        self.array.append(10)
        print("Appending 20 to the array.")
        self.array.append(20)
        print("Inserting 15 at index 1.")
        self.array.insert(1, 15)
        print(f"Current array: {self.array}")
        self.assertEqual(self.array.data, [10, 15, 20])
        
        # Test inserting at the beginning
        print("Inserting 5 at index 0.")
        self.array.insert(0, 5)
        print(f"Current array: {self.array}")
        self.assertEqual(self.array.data, [5, 10, 15, 20])
        
        # Test inserting at the end
        print("Inserting 25 at index 4.")
        self.array.insert(4, 25)
        print(f"Current array: {self.array}")
        self.assertEqual(self.array.data, [5, 10, 15, 20, 25])

    def test_insert_index_error(self):
        """Test inserting at an index out of bounds."""
        print("Testing insert method with out-of-bounds index:")
        with self.assertRaises(IndexError):
            print("Attempting to insert 10 at index -1 (should raise IndexError).")
            self.array.insert(-1, 10)  # Negative index
        with self.assertRaises(IndexError):
            print("Attempting to insert 10 at index 1 in an empty array (should raise IndexError).")
            self.array.insert(1, 10)  # Index out of bounds

    def test_delete(self):
        """Test deleting elements at specific indices."""
        print("Testing delete method:")
        self.array.append(10)
        self.array.append(20)
        self.array.append(30)
        print(f"Initial array: {self.array}")
        
        print("Deleting element at index 1 (value 20).")
        value = self.array.delete(1)
        print(f"Deleted value: {value}")
        print(f"Current array: {self.array}")
        self.assertEqual(value, 20)
        self.assertEqual(self.array.data, [10, 30])
        self.assertEqual(self.array.size, 2)

    def test_delete_index_error(self):
        """Test deleting at an index out of bounds."""
        print("Testing delete method with out-of-bounds index:")
        with self.assertRaises(IndexError):
            print("Attempting to delete from an empty array (should raise IndexError).")
            self.array.delete(0)  # Empty array
        self.array.append(10)
        print("Array after appending 10: ", self.array)
        with self.assertRaises(IndexError):
            print("Attempting to delete from index 1 (out of bounds, should raise IndexError).")
            self.array.delete(1)  # Index out of bounds

    def test_search(self):
        """Test searching for elements in the array."""
        print("Testing search method:")
        self.array.append(10)
        self.array.append(20)
        self.array.append(30)
        print(f"Array: {self.array}")
        
        index = self.array.search(20)
        print(f"Searching for value 20, found at index: {index}")
        self.assertEqual(index, 1)
        
        # Test searching for a non-existent element
        index = self.array.search(40)
        print(f"Searching for value 40 (not present), found at index: {index}")
        self.assertEqual(index, -1)

    def test_update(self):
        """Test updating elements at specific indices."""
        print("Testing update method:")
        self.array.append(10)
        self.array.append(20)
        self.array.append(30)
        print(f"Initial array: {self.array}")
        
        print("Updating index 1 from 20 to 25.")
        self.array.update(1, 25)
        print(f"Updated array: {self.array}")
        self.assertEqual(self.array.data, [10, 25, 30])
        
    def test_update_index_error(self):
        """Test updating an element at an index out of bounds."""
        print("Testing update method with out-of-bounds index:")
        with self.assertRaises(IndexError):
            print("Attempting to update index 0 in an empty array (should raise IndexError).")
            self.array.update(0, 10)  # Empty array
        self.array.append(10)
        print("Array after appending 10: ", self.array)
        with self.assertRaises(IndexError):
            print("Attempting to update index 1 (out of bounds, should raise IndexError).")
            self.array.update(1, 20)  # Index out of bounds

    def test_str(self):
        """Test the string representation of the array."""
        print("Testing __str__ method:")
        self.array.append(10)
        self.array.append(20)
        result = str(self.array)
        print(f"Array string representation: {result}")
        self.assertEqual(result, '[10, 20]')

if __name__ == '__main__':
    unittest.main()