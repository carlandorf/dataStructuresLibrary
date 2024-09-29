# data_structures/array.py

class Array:
    def __init__(self):
        self.data = []
        self.size = 0

    def append(self, value):
        """Adds a value to the end of the array."""
        self.data.append(value)
        self.size += 1

    def insert(self, index, value):
        """Inserts a value at the specified index."""
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        self.data.insert(index, value)
        self.size += 1

    def delete(self, index):
        """Deletes the element at the specified index."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        value = self.data.pop(index)
        self.size -= 1
        return value

    def search(self, value):
        """Searches for a value and returns its index. Returns -1 if not found."""
        try:
            return self.data.index(value)
        except ValueError:
            return -1

    def update(self, index, value):
        """Updates the element at the specified index."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        self.data[index] = value

    def __str__(self):
        """Returns a string representation of the array."""
        return str(self.data)