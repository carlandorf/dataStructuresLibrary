# data_structures/binary_tree.py

class TreeNode:
    """Node class for the binary tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a new value into the binary search tree."""
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """Helper method to insert a value in the tree recursively."""
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        """Search for a value in the binary search tree."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """Helper method to search for a value recursively."""
        if node is None or node.value == value:
            return node is not None
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def delete(self, value):
        """Delete a value from the binary search tree."""
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        """Helper method to delete a node recursively."""
        if node is None:
            return None

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children, get the inorder successor (smallest in the right subtree)
            min_larger_node = self._find_min(node.right)
            node.value = min_larger_node.value
            node.right = self._delete_recursive(node.right, min_larger_node.value)

        return node

    def _find_min(self, node):
        """Find the node with the minimum value."""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def in_order_traversal(self):
        """In-order traversal of the binary tree."""
        return self._in_order_recursive(self.root)

    def _in_order_recursive(self, node):
        """Helper method for in-order traversal."""
        result = []
        if node:
            result += self._in_order_recursive(node.left)
            result.append(node.value)
            result += self._in_order_recursive(node.right)
        return result

    def pre_order_traversal(self):
        """Pre-order traversal of the binary tree."""
        return self._pre_order_recursive(self.root)

    def _pre_order_recursive(self, node):
        """Helper method for pre-order traversal."""
        result = []
        if node:
            result.append(node.value)
            result += self._pre_order_recursive(node.left)
            result += self._pre_order_recursive(node.right)
        return result

    def post_order_traversal(self):
        """Post-order traversal of the binary tree."""
        return self._post_order_recursive(self.root)

    def _post_order_recursive(self, node):
        """Helper method for post-order traversal."""
        result = []
        if node:
            result += self._post_order_recursive(node.left)
            result += self._post_order_recursive(node.right)
            result.append(node.value)
        return result