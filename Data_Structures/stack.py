# data_structures/stack.py

class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        """Pushes a value onto the stack."""
        self.data.append(value)

    def pop(self):
        """Removes and returns the top element of the stack."""
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.data.pop()

    def peek(self):
        """Returns the top element without removing it."""
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.data[-1]

    def is_empty(self):
        """Checks if the stack is empty."""
        return len(self.data) == 0

    def __str__(self):
        """Returns a string representation of the stack."""
        return str(self.data)