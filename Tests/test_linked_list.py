# tests/test_linked_list.py

import unittest
import sys
import os

# Add the parent directory to the system path to resolve the import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the LinkedList class from the Data_Structures module
from Data_Structures.linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    
    def setUp(self):
        """Setup a new LinkedList instance before each test."""
        print("\nSetting up a new LinkedList instance for the test...")
        self.linked_list = LinkedList()

    def test_append(self):
        """Test appending elements to the linked list."""
        print("Testing append method:")
        print("Appending 10 to the linked list.")
        self.linked_list.append(10)
        print(f"Current list: {self.linked_list}")
        
        print("Appending 20 to the linked list.")
        self.linked_list.append(20)
        print(f"Current list: {self.linked_list}")
        
        self.assertEqual(str(self.linked_list), "10 -> 20")

    def test_insert(self):
        """Test inserting elements at specific indices."""
        print("Testing insert method:")
        print("Appending 10 to the linked list.")
        self.linked_list.append(10)
        
        print("Appending 30 to the linked list.")
        self.linked_list.append(30)
        
        print("Inserting 20 at index 1.")
        self.linked_list.insert(1, 20)
        print(f"Current list: {self.linked_list}")
        self.assertEqual(str(self.linked_list), "10 -> 20 -> 30")
        
        print("Inserting 5 at index 0.")
        self.linked_list.insert(0, 5)
        print(f"Current list: {self.linked_list}")
        self.assertEqual(str(self.linked_list), "5 -> 10 -> 20 -> 30")
        
        print("Inserting 35 at index 4 (end of list).")
        self.linked_list.insert(4, 35)
        print(f"Current list: {self.linked_list}")
        self.assertEqual(str(self.linked_list), "5 -> 10 -> 20 -> 30 -> 35")

    def test_insert_index_error(self):
        """Test inserting at an index out of bounds."""
        print("Testing insert method with out-of-bounds index:")
        with self.assertRaises(IndexError):
            print("Attempting to insert 10 at index -1 (should raise IndexError).")
            self.linked_list.insert(-1, 10)  # Negative index
        with self.assertRaises(IndexError):
            print("Attempting to insert 10 at index 1 in an empty list (should raise IndexError).")
            self.linked_list.insert(1, 10)  # Index out of bounds

    def test_delete(self):
        """Test deleting elements with a specific value."""
        print("Testing delete method:")
        self.linked_list.append(10)
        self.linked_list.append(20)
        self.linked_list.append(30)
        print(f"Initial list: {self.linked_list}")
        
        print("Deleting value 20 from the list.")
        self.linked_list.delete(20)
        print(f"Current list: {self.linked_list}")
        self.assertEqual(str(self.linked_list), "10 -> 30")
        
        print("Deleting value 10 from the list (head).")
        self.linked_list.delete(10)
        print(f"Current list: {self.linked_list}")
        self.assertEqual(str(self.linked_list), "30")
        
        print("Deleting value 30 from the list (last element).")
        self.linked_list.delete(30)
        print(f"Current list: {self.linked_list}")
        self.assertEqual(str(self.linked_list), "")

    def test_delete_value_error(self):
        """Test deleting a non-existent element from the list."""
        print("Testing delete method with a non-existent value:")
        self.linked_list.append(10)
        print(f"Initial list: {self.linked_list}")
        with self.assertRaises(ValueError):
            print("Attempting to delete value 20 (not in the list, should raise ValueError).")
            self.linked_list.delete(20)

    def test_search(self):
        """Test searching for elements in the linked list."""
        print("Testing search method:")
        self.linked_list.append(10)
        self.linked_list.append(20)
        self.linked_list.append(30)
        print(f"Current list: {self.linked_list}")
        
        index = self.linked_list.search(20)
        print(f"Searching for value 20, found at index: {index}")
        self.assertEqual(index, 1)
        
        index = self.linked_list.search(40)
        print(f"Searching for value 40 (not present), found at index: {index}")
        self.assertEqual(index, -1)

    def test_reverse(self):
        """Test reversing the linked list."""
        print("Testing reverse method:")
        self.linked_list.append(10)
        self.linked_list.append(20)
        self.linked_list.append(30)
        print(f"Initial list: {self.linked_list}")
        
        print("Reversing the linked list.")
        self.linked_list.reverse()
        print(f"Reversed list: {self.linked_list}")
        self.assertEqual(str(self.linked_list), "30 -> 20 -> 10")

    def test_str(self):
        """Test the string representation of the linked list."""
        print("Testing __str__ method:")
        self.linked_list.append(10)
        self.linked_list.append(20)
        result = str(self.linked_list)
        print(f"Linked list string representation: {result}")
        self.assertEqual(result, "10 -> 20")

if __name__ == '__main__':
    unittest.main()