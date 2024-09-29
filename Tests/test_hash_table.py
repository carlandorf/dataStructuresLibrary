# tests/test_hash_table.py

import unittest
import sys
import os

# Add the parent directory to the system path to resolve the import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the HashTable class from the Data_Structures module
from Data_Structures.hash_table import HashTable

class TestHashTable(unittest.TestCase):
    
    def setUp(self):
        """Setup a new HashTable instance before each test."""
        print("\nSetting up a new HashTable instance for the test...")
        self.hash_table = HashTable()

    def test_insert_and_search(self):
        """Test inserting and searching elements in the hash table."""
        print("Testing insert and search methods:")
        
        # Insert key-value pairs
        print("Inserting key 'apple' with value 10.")
        self.hash_table.insert('apple', 10)
        print("Inserting key 'banana' with value 20.")
        self.hash_table.insert('banana', 20)
        print("Inserting key 'orange' with value 30.")
        self.hash_table.insert('orange', 30)
        print(f"Current hash table: {self.hash_table}")
        
        # Search for keys
        value = self.hash_table.search('apple')
        print(f"Searching for key 'apple': Found value {value}")
        self.assertEqual(value, 10)
        
        value = self.hash_table.search('banana')
        print(f"Searching for key 'banana': Found value {value}")
        self.assertEqual(value, 20)
        
        value = self.hash_table.search('orange')
        print(f"Searching for key 'orange': Found value {value}")
        self.assertEqual(value, 30)
        
        # Search for a non-existent key
        value = self.hash_table.search('grape')
        print(f"Searching for key 'grape': Found value {value}")
        self.assertIsNone(value)

    def test_update_value(self):
        """Test updating the value of an existing key."""
        print("Testing update value for an existing key:")
        
        # Insert key-value pairs
        print("Inserting key 'apple' with value 10.")
        self.hash_table.insert('apple', 10)
        print(f"Current hash table: {self.hash_table}")
        
        # Update the value of the key 'apple'
        print("Updating key 'apple' to new value 15.")
        self.hash_table.insert('apple', 15)
        print(f"Current hash table after update: {self.hash_table}")
        
        value = self.hash_table.search('apple')
        print(f"Searching for key 'apple' after update: Found value {value}")
        self.assertEqual(value, 15)

    def test_delete(self):
        """Test deleting elements from the hash table."""
        print("Testing delete method:")
        
        # Insert key-value pairs
        print("Inserting key 'apple' with value 10.")
        self.hash_table.insert('apple', 10)
        print("Inserting key 'banana' with value 20.")
        self.hash_table.insert('banana', 20)
        print("Inserting key 'orange' with value 30.")
        self.hash_table.insert('orange', 30)
        print(f"Current hash table: {self.hash_table}")
        
        # Delete 'banana' from the hash table
        print("Deleting key 'banana' from the hash table.")
        deleted = self.hash_table.delete('banana')
        print(f"Deleted 'banana': {deleted}")
        print(f"Current hash table after deletion: {self.hash_table}")
        self.assertTrue(deleted)
        
        # Try to delete a non-existent key
        print("Trying to delete key 'grape' (not present in the hash table).")
        deleted = self.hash_table.delete('grape')
        print(f"Deleted 'grape': {deleted}")
        self.assertFalse(deleted)

    def test_collision_handling(self):
        """Test handling of hash collisions."""
        print("Testing collision handling:")
        
        # Using a custom small table size to force collisions
        small_hash_table = HashTable(size=2)
        
        # Insert key-value pairs that will collide
        print("Inserting key 'key1' with value 100.")
        small_hash_table.insert('key1', 100)
        print("Inserting key 'key2' with value 200.")
        small_hash_table.insert('key2', 200)
        print(f"Current hash table with potential collisions: {small_hash_table}")
        
        # Check both values are stored correctly
        value = small_hash_table.search('key1')
        print(f"Searching for key 'key1': Found value {value}")
        self.assertEqual(value, 100)
        
        value = small_hash_table.search('key2')
        print(f"Searching for key 'key2': Found value {value}")
        self.assertEqual(value, 200)
        
        # Ensure the collision was handled correctly
        self.assertEqual(len(small_hash_table.table[0]) + len(small_hash_table.table[1]), 2)

    def test_str(self):
        """Test the string representation of the hash table."""
        print("Testing __str__ method:")
        
        # Insert key-value pairs
        print("Inserting key 'apple' with value 10.")
        self.hash_table.insert('apple', 10)
        print("Inserting key 'banana' with value 20.")
        self.hash_table.insert('banana', 20)
        print(f"Current hash table: {self.hash_table}")
        
        result = str(self.hash_table)
        print(f"Hash table string representation: {result}")
        self.assertIn('[', result)  # Checking that the representation is in list form

if __name__ == '__main__':
    unittest.main()