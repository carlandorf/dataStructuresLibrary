# tests/test_binary_tree.py

import unittest
import sys
import os

# Add the parent directory to the system path to resolve the import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the BinaryTree class from the Data_Structures module
from Data_Structures.binary_tree import BinaryTree

class TestBinaryTree(unittest.TestCase):
    
    def setUp(self):
        """Setup a new BinaryTree instance before each test."""
        print("\nSetting up a new BinaryTree instance for the test...")
        self.bst = BinaryTree()

    def test_insert(self):
        """Test inserting elements into the binary search tree."""
        print("Testing insert method:")
        print("Inserting 50 into the binary tree.")
        self.bst.insert(50)
        print("Inserting 30 into the binary tree.")
        self.bst.insert(30)
        print("Inserting 70 into the binary tree.")
        self.bst.insert(70)
        print("Inserting 20 into the binary tree.")
        self.bst.insert(20)
        print("Inserting 40 into the binary tree.")
        self.bst.insert(40)
        print("Inserting 60 into the binary tree.")
        self.bst.insert(60)
        print("Inserting 80 into the binary tree.")
        self.bst.insert(80)
        
        in_order = self.bst.in_order_traversal()
        print(f"In-order traversal result: {in_order}")
        self.assertEqual(in_order, [20, 30, 40, 50, 60, 70, 80])

    def test_search(self):
        """Test searching for elements in the binary search tree."""
        print("Testing search method:")
        values = [50, 30, 70, 20, 40, 60, 80]
        for value in values:
            self.bst.insert(value)
        
        print("Searching for value 40 in the tree.")
        found = self.bst.search(40)
        print(f"Result of searching for 40: {found}")
        self.assertTrue(found)
        
        print("Searching for value 25 in the tree (not present).")
        found = self.bst.search(25)
        print(f"Result of searching for 25: {found}")
        self.assertFalse(found)

    def test_delete(self):
        """Test deleting elements from the binary search tree."""
        print("Testing delete method:")
        values = [50, 30, 70, 20, 40, 60, 80]
        for value in values:
            self.bst.insert(value)
        
        print(f"Initial in-order traversal: {self.bst.in_order_traversal()}")
        
        print("Deleting value 20 from the tree (no children).")
        self.bst.delete(20)
        print(f"In-order traversal after deleting 20: {self.bst.in_order_traversal()}")
        self.assertEqual(self.bst.in_order_traversal(), [30, 40, 50, 60, 70, 80])
        
        print("Deleting value 30 from the tree (one child).")
        self.bst.delete(30)
        print(f"In-order traversal after deleting 30: {self.bst.in_order_traversal()}")
        self.assertEqual(self.bst.in_order_traversal(), [40, 50, 60, 70, 80])
        
        print("Deleting value 50 from the tree (two children).")
        self.bst.delete(50)
        print(f"In-order traversal after deleting 50: {self.bst.in_order_traversal()}")
        self.assertEqual(self.bst.in_order_traversal(), [40, 60, 70, 80])

    def test_in_order_traversal(self):
        """Test in-order traversal of the binary search tree."""
        print("Testing in-order traversal method:")
        values = [50, 30, 70, 20, 40, 60, 80]
        for value in values:
            self.bst.insert(value)
        
        print("Performing in-order traversal.")
        result = self.bst.in_order_traversal()
        print(f"In-order traversal result: {result}")
        self.assertEqual(result, [20, 30, 40, 50, 60, 70, 80])

    def test_pre_order_traversal(self):
        """Test pre-order traversal of the binary search tree."""
        print("Testing pre-order traversal method:")
        values = [50, 30, 70, 20, 40, 60, 80]
        for value in values:
            self.bst.insert(value)
        
        print("Performing pre-order traversal.")
        result = self.bst.pre_order_traversal()
        print(f"Pre-order traversal result: {result}")
        self.assertEqual(result, [50, 30, 20, 40, 70, 60, 80])

    def test_post_order_traversal(self):
        """Test post-order traversal of the binary search tree."""
        print("Testing post-order traversal method:")
        values = [50, 30, 70, 20, 40, 60, 80]
        for value in values:
            self.bst.insert(value)
        
        print("Performing post-order traversal.")
        result = self.bst.post_order_traversal()
        print(f"Post-order traversal result: {result}")
        self.assertEqual(result, [20, 40, 30, 60, 80, 70, 50])

if __name__ == '__main__':
    unittest.main()