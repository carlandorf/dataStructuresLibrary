# data_structures/queue.py

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        """Add an element to the end of the queue."""
        self.queue.append(value)

    def dequeue(self):
        """Remove and return the element from the front of the queue."""
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def peek(self):
        """Return the front element without removing it."""
        if not self.is_empty():
            return self.queue[0]
        return None

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def __str__(self):
        """Return a string representation of the queue."""
        return str(self.queue)