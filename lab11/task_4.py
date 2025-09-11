class Node:
    """
    Node class for Binary Search Tree.
    Each node contains data, and pointers to left and right children.
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    """
    Binary Search Tree implementation with insert, search, and inorder traversal.
    """
    def __init__(self):
        self.root = None

    def insert(self, data):
        """
        Insert a new node with the given data into the BST.

        Args:
            data: The value to insert.
        """
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(node.right, data)
        # If data == node.data, do not insert duplicates (BST property)

    def search(self, data):
        """
        Search for a value in the BST.

        Args:
            data: The value to search for.

        Returns:
            True if found, False otherwise.
        """
        return self._search_recursive(self.root, data)

    def _search_recursive(self, node, data):
        if node is None:
            return False
        if data == node.data:
            return True
        elif data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)

    def inorder_traversal(self):
        """
        Perform inorder traversal of the BST.

        Returns:
            A list of elements in sorted order.
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)

# Test the BST implementation
if __name__ == "__main__":
    bst = BST()
    elements = [50, 30, 70, 20, 40, 60, 80]
    for el in elements:
        bst.insert(el)

    print("Inorder traversal (should be sorted):", bst.inorder_traversal())

    # Test search for present elements
    present = [30, 70, 50]
    for val in present:
        print(f"Search {val}: {bst.search(val)} (expected: True)")

    # Test search for absent elements
    absent = [10, 35, 90]
    for val in absent:
        print(f"Search {val}: {bst.search(val)} (expected: False)")
