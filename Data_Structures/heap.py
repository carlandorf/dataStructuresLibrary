# data_structures/heap.py

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        """Insert a new value into the min-heap."""
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def delete_min(self):
        """Remove and return the minimum value from the heap."""
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def get_min(self):
        """Return the minimum value without removing it."""
        return self.heap[0] if self.heap else None

    def _heapify_up(self, index):
        """Move the value at index up to its correct position (MinHeap property)."""
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        """Move the value at index down to its correct position (MinHeap property)."""
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def __str__(self):
        """Return a string representation of the min-heap."""
        return str(self.heap)


class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        """Insert a new value into the max-heap."""
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def delete_max(self):
        """Remove and return the maximum value from the heap."""
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def get_max(self):
        """Return the maximum value without removing it."""
        return self.heap[0] if self.heap else None

    def _heapify_up(self, index):
        """Move the value at index up to its correct position (MaxHeap property)."""
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        """Move the value at index down to its correct position (MaxHeap property)."""
        largest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
            largest = left_child
        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
            largest = right_child
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def __str__(self):
        """Return a string representation of the max-heap."""
        return str(self.heap)