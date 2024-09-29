# tests/test_stack.py

import unittest
import sys
import os

# Add the parent directory to the system path to resolve the import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the Stack class from the Data_Structures module
from Data_Structures.stack import Stack

class TestStack(unittest.TestCase):
    
    def setUp(self):
        """Setup a new Stack instance before each test."""
        print("\nSetting up a new Stack instance for the test...")
        self.stack = Stack()

    def test_push(self):
        """Test pushing elements onto the stack."""
        print("Testing push method:")
        print("Pushing 10 onto the stack.")
        self.stack.push(10)
        print(f"Current stack: {self.stack}")
        
        print("Pushing 20 onto the stack.")
        self.stack.push(20)
        print(f"Current stack: {self.stack}")
        
        self.assertEqual(str(self.stack), '[10, 20]')

    def test_pop(self):
        """Test popping elements from the stack."""
        print("Testing pop method:")
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(30)
        print(f"Initial stack: {self.stack}")
        
        value = self.stack.pop()
        print(f"Popped value: {value}")
        print(f"Current stack: {self.stack}")
        self.assertEqual(value, 30)
        self.assertEqual(str(self.stack), '[10, 20]')
        
        value = self.stack.pop()
        print(f"Popped value: {value}")
        print(f"Current stack: {self.stack}")
        self.assertEqual(value, 20)
        self.assertEqual(str(self.stack), '[10]')

    def test_pop_empty_stack(self):
        """Test popping from an empty stack."""
        print("Testing pop method with an empty stack:")
        with self.assertRaises(IndexError):
            print("Attempting to pop from an empty stack (should raise IndexError).")
            self.stack.pop()

    def test_peek(self):
        """Test peeking at the top element of the stack."""
        print("Testing peek method:")
        self.stack.push(10)
        self.stack.push(20)
        print(f"Current stack: {self.stack}")
        
        value = self.stack.peek()
        print(f"Peeked value: {value}")
        self.assertEqual(value, 20)
        
        # Peeking again should not modify the stack
        print(f"Current stack after peeking: {self.stack}")
        self.assertEqual(str(self.stack), '[10, 20]')

    def test_peek_empty_stack(self):
        """Test peeking at an empty stack."""
        print("Testing peek method with an empty stack:")
        with self.assertRaises(IndexError):
            print("Attempting to peek at an empty stack (should raise IndexError).")
            self.stack.peek()

    def test_is_empty(self):
        """Test checking if the stack is empty."""
        print("Testing is_empty method:")
        print(f"Is the stack empty? {self.stack.is_empty()}")
        self.assertTrue(self.stack.is_empty())
        
        self.stack.push(10)
        print(f"Is the stack empty after pushing 10? {self.stack.is_empty()}")
        self.assertFalse(self.stack.is_empty())

    def test_str(self):
        """Test the string representation of the stack."""
        print("Testing __str__ method:")
        self.stack.push(10)
        self.stack.push(20)
        result = str(self.stack)
        print(f"Stack string representation: {result}")
        self.assertEqual(result, '[10, 20]')

if __name__ == '__main__':
    unittest.main()