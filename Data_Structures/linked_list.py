# data_structures/linked_list.py

class Node:
    """Node class to represent each element in the linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """Adds a node with the given value to the end of the list."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert(self, index, value):
        """Inserts a node with the given value at the specified index."""
        if index < 0:
            raise IndexError("Index out of bounds")
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        current_index = 0
        while current and current_index < index - 1:
            current = current.next
            current_index += 1
        if not current:
            raise IndexError("Index out of bounds")
        new_node.next = current.next
        current.next = new_node

    def delete(self, value):
        """Deletes the first occurrence of the node with the given value."""
        if not self.head:
            raise ValueError("Value not found")
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.value != value:
            current = current.next
        if not current.next:
            raise ValueError("Value not found")
        current.next = current.next.next

    def search(self, value):
        """Searches for the first occurrence of the node with the given value and returns its index."""
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def reverse(self):
        """Reverses the linked list."""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def __str__(self):
        """Returns a string representation of the linked list."""
        result = []
        current = self.head
        while current:
            result.append(str(current.value))
            current = current.next
        return " -> ".join(result)