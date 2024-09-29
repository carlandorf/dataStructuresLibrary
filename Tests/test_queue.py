# tests/test_queue.py

import unittest
import sys
import os

# Add the parent directory to the system path to resolve the import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the Queue class from the Data_Structures module
from Data_Structures.queue import Queue

class TestQueue(unittest.TestCase):
    
    def setUp(self):
        """Setup a new Queue instance before each test."""
        print("\nSetting up a new Queue instance for the test...")
        self.queue = Queue()

    def test_enqueue(self):
        """Test enqueuing elements to the queue."""
        print("Testing enqueue method:")
        print("Enqueuing 10 to the queue.")
        self.queue.enqueue(10)
        print(f"Current queue: {self.queue}")
        
        print("Enqueuing 20 to the queue.")
        self.queue.enqueue(20)
        print(f"Current queue: {self.queue}")
        
        print("Enqueuing 30 to the queue.")
        self.queue.enqueue(30)
        print(f"Current queue: {self.queue}")
        
        self.assertEqual(str(self.queue), '[10, 20, 30]')

    def test_dequeue(self):
        """Test dequeuing elements from the queue."""
        print("Testing dequeue method:")
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.queue.enqueue(30)
        print(f"Initial queue: {self.queue}")
        
        value = self.queue.dequeue()
        print(f"Dequeued value: {value}")
        print(f"Queue after dequeue: {self.queue}")
        self.assertEqual(value, 10)
        self.assertEqual(str(self.queue), '[20, 30]')
        
        value = self.queue.dequeue()
        print(f"Dequeued value: {value}")
        print(f"Queue after dequeue: {self.queue}")
        self.assertEqual(value, 20)
        self.assertEqual(str(self.queue), '[30]')

    def test_peek(self):
        """Test peeking at the front element of the queue."""
        print("Testing peek method:")
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        print(f"Current queue: {self.queue}")
        
        value = self.queue.peek()
        print(f"Peeked value: {value}")
        self.assertEqual(value, 10)
        
        print(f"Queue after peeking (should be unchanged): {self.queue}")
        self.assertEqual(str(self.queue), '[10, 20]')

    def test_is_empty(self):
        """Test checking if the queue is empty."""
        print("Testing is_empty method:")
        print(f"Is the queue empty? {self.queue.is_empty()}")
        self.assertTrue(self.queue.is_empty())
        
        self.queue.enqueue(10)
        print(f"Is the queue empty after enqueuing 10? {self.queue.is_empty()}")
        self.assertFalse(self.queue.is_empty())

    def test_dequeue_empty_queue(self):
        """Test dequeuing from an empty queue."""
        print("Testing dequeue method with an empty queue:")
        value = self.queue.dequeue()
        print(f"Result of dequeuing from empty queue: {value}")
        self.assertIsNone(value)

    def test_peek_empty_queue(self):
        """Test peeking at an empty queue."""
        print("Testing peek method with an empty queue:")
        value = self.queue.peek()
        print(f"Result of peeking at empty queue: {value}")
        self.assertIsNone(value)

if __name__ == '__main__':
    unittest.main()