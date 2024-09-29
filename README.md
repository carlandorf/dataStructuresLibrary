Data Structures Library

Overview----------------------------------------------------------

This project is a comprehensive implementation of common data structures and algorithms in Python. It serves as an educational tool for understanding the fundamentals of data structures, as well as a practical library that can be used in various applications. The library includes implementations of arrays, linked lists, stacks, queues, hash tables, trees, heaps, and graphs, along with a collection of algorithms such as sorting, searching, and graph traversal.

Table of Contents

    1.	Project Structure
    2.	Installation
    3.	Data Structures
    4.	Algorithms
    5.	Usage Examples
    6.	Testing
    7.	Contributing
    8.	License

Project Structure-------------------------------------------------

data_structures_library/
│
├── data_structures/
│ ├── **init**.py
│ ├── array.py
│ ├── linked_list.py
│ ├── stack.py
│ ├── queue.py
│ ├── hash_table.py
│ ├── binary_tree.py
│ ├── heap.py
│ └── graph.py
│
├── algorithms/
│ ├── **init**.py
│ ├── sorting.py
│ ├── searching.py
│ └── graph_algorithms.py
│
├── tests/
│ ├── **init**.py
│ ├── test_array.py
│ ├── test_linked_list.py
│ ├── test_stack.py
│ ├── test_queue.py
│ ├── test_hash_table.py
│ ├── test_binary_tree.py
│ ├── test_heap.py
│ └── test_graph.py
│
└── README.md

Data Structures---------------------------------------------------

The library includes the following data structures, each implemented as a separate class with standard methods:

    •	Array (array.py)
    •	Dynamic array implementation with operations such as insert, delete, and search.
    •	Linked List (linked_list.py)
    •	Singly and doubly linked list with methods for insertion, deletion, and reversal.
    •	Stack (stack.py)
    •	Stack implementation supporting push, pop, and peek operations.
    •	Queue (queue.py)
    •	Implementation of a queue with enqueue and dequeue operations.
    •	Hash Table (hash_table.py)
    •	Hash table implementation with separate chaining for collision resolution.
    •	Binary Tree (binary_tree.py)
    •	Binary search tree with methods for insertion, deletion, and traversal.
    •	Heap (heap.py)
    •	Min-heap and max-heap implementations with operations like insert and extract.
    •	Graph (graph.py)
    •	Graph representation using adjacency list, supporting BFS and DFS traversals.

Algorithms--------------------------------------------------------

The algorithms module includes common sorting and searching algorithms as well as graph traversal techniques:

    •	Sorting Algorithms (sorting.py)
    •	Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort, Heap Sort.
    •	Searching Algorithms (searching.py)
    •	Linear Search, Binary Search.
    •	Graph Algorithms (graph_algorithms.py)
    •	Depth-First Search (DFS), Breadth-First Search (BFS), Dijkstra’s Shortest Path.

Usage Examples----------------------------------------------------

Below are some basic usage examples for the data structures and algorithms in this library.

1.  Array

    from data_structures.array import Array

        arr = Array()
        arr.append(10)
        arr.append(20)
        arr.insert(1, 15)
        print(arr)  # Output: [10, 15, 20]
        arr.delete(1)
        print(arr)  # Output: [10, 20]

2.  Linked List

    from data_structures.linked_list import LinkedList

        ll = LinkedList()
        ll.append(5)
        ll.append(10)
        ll.insert(1, 7)
        ll.delete(10)
        print(ll)  # Output: 5 -> 7

3.  Graph - BFS Traversal

    from data_structures.graph import Graph

        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_edge("A", "B")
        print(graph.bfs("A"))  # Output: ['A', 'B']

Testing

To run the unit tests for each data structure and algorithm:

    1.	Install pytest if you don’t have it:
        pip install pytest

    2.	Run the tests:
        pytest tests/

The tests ensure the correctness and robustness of the library. Each data structure has its own test file under the tests/ directory.
