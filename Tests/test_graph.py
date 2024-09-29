# tests/test_graph.py

import unittest
import sys
import os

# Add the parent directory to the system path to resolve the import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the Graph class from the Data_Structures module
from Data_Structures.graph import Graph

class TestGraph(unittest.TestCase):
    
    def setUp(self):
        """Setup a new Graph instance before each test."""
        print("\nSetting up a new Graph instance for the test...")
        self.graph = Graph()

    def test_add_vertex(self):
        """Test adding vertices to the graph."""
        print("Testing add_vertex method:")
        print("Adding vertex 'A' to the graph.")
        self.graph.add_vertex('A')
        print("Adding vertex 'B' to the graph.")
        self.graph.add_vertex('B')
        print("Adding vertex 'C' to the graph.")
        self.graph.add_vertex('C')
        
        print(f"Current graph: {self.graph}")
        self.assertIn('A', self.graph.graph)
        self.assertIn('B', self.graph.graph)
        self.assertIn('C', self.graph.graph)

    def test_add_edge(self):
        """Test adding edges to the graph."""
        print("Testing add_edge method:")
        print("Adding vertices 'A' and 'B' to the graph.")
        self.graph.add_vertex('A')
        self.graph.add_vertex('B')
        
        print("Adding edge between 'A' and 'B'.")
        self.graph.add_edge('A', 'B')
        print(f"Current graph: {self.graph}")
        
        self.assertIn('B', self.graph.graph['A'])
        self.assertIn('A', self.graph.graph['B'])

    def test_remove_vertex(self):
        """Test removing vertices from the graph."""
        print("Testing remove_vertex method:")
        print("Adding vertices 'A', 'B', and 'C' to the graph.")
        self.graph.add_vertex('A')
        self.graph.add_vertex('B')
        self.graph.add_vertex('C')
        
        print("Adding edges between 'A' and 'B', 'A' and 'C'.")
        self.graph.add_edge('A', 'B')
        self.graph.add_edge('A', 'C')
        
        print(f"Initial graph: {self.graph}")
        
        print("Removing vertex 'A' from the graph.")
        self.graph.remove_vertex('A')
        print(f"Graph after removing 'A': {self.graph}")
        
        self.assertNotIn('A', self.graph.graph)
        self.assertNotIn('A', self.graph.graph['B'])
        self.assertNotIn('A', self.graph.graph['C'])

    def test_remove_edge(self):
        """Test removing edges from the graph."""
        print("Testing remove_edge method:")
        print("Adding vertices 'A' and 'B' to the graph.")
        self.graph.add_vertex('A')
        self.graph.add_vertex('B')
        
        print("Adding edge between 'A' and 'B'.")
        self.graph.add_edge('A', 'B')
        print(f"Current graph: {self.graph}")
        
        print("Removing edge between 'A' and 'B'.")
        self.graph.remove_edge('A', 'B')
        print(f"Graph after removing edge between 'A' and 'B': {self.graph}")
        
        self.assertNotIn('B', self.graph.graph['A'])
        self.assertNotIn('A', self.graph.graph['B'])

    def test_bfs(self):
        """Test BFS traversal of the graph."""
        print("Testing BFS traversal method:")
        print("Adding vertices 'A', 'B', 'C', 'D', 'E' to the graph.")
        vertices = ['A', 'B', 'C', 'D', 'E']
        for vertex in vertices:
            self.graph.add_vertex(vertex)
        
        print("Adding edges: A-B, A-C, B-D, C-E.")
        self.graph.add_edge('A', 'B')
        self.graph.add_edge('A', 'C')
        self.graph.add_edge('B', 'D')
        self.graph.add_edge('C', 'E')
        
        print(f"Current graph: {self.graph}")
        
        print("Performing BFS traversal starting from 'A'.")
        bfs_result = self.graph.bfs('A')
        print(f"BFS traversal result: {bfs_result}")
        self.assertEqual(bfs_result, ['A', 'B', 'C', 'D', 'E'])

    def test_dfs(self):
        """Test DFS traversal of the graph."""
        print("Testing DFS traversal method:")
        print("Adding vertices 'A', 'B', 'C', 'D', 'E' to the graph.")
        vertices = ['A', 'B', 'C', 'D', 'E']
        for vertex in vertices:
            self.graph.add_vertex(vertex)
        
        print("Adding edges: A-B, A-C, B-D, C-E.")
        self.graph.add_edge('A', 'B')
        self.graph.add_edge('A', 'C')
        self.graph.add_edge('B', 'D')
        self.graph.add_edge('C', 'E')
        
        print(f"Current graph: {self.graph}")
        
        print("Performing DFS traversal starting from 'A'.")
        dfs_result = self.graph.dfs('A')
        print(f"DFS traversal result: {dfs_result}")
        self.assertEqual(dfs_result, ['A', 'C', 'E', 'B', 'D'])

if __name__ == '__main__':
    unittest.main()