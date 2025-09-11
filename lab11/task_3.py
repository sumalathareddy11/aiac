class Node:
    """
    Node class for singly linked list.
    Each node contains data and a pointer to the next node.
    """
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node


class LinkedList:
    """
    Singly linked list implementation with basic operations.
    """
    def __init__(self):
        self.head = None  # Start with an empty list

    def insert_at_end(self, data):
        """
        Insert a new node with the given data at the end of the list.
        """
        new_node = Node(data)
        if self.head is None:
            # If the list is empty, new node becomes the head
            self.head = new_node
        else:
            current = self.head
            # Traverse to the last node
            while current.next:
                current = current.next
            # Set the next pointer of the last node to the new node
            current.next = new_node  # Pointer update: last node now points to new node

    def delete_value(self, value):
        """
        Delete the first node in the list with the specified value.
        """
        current = self.head
        prev = None
        while current:
            if current.data == value:
                if prev is None:
                    # Deleting the head node
                    self.head = current.next  # Pointer update: head now points to next node
                else:
                    # Bypass the current node
                    prev.next = current.next  # Pointer update: previous node skips current
                return True  # Value found and deleted
            prev = current
            current = current.next
        return False  # Value not found

    def traverse(self):
        """
        Traverse the list and return a list of node data.
        """
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next  # Move to the next node
        return elements

# Example usage and demonstration
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    print("List after insertions:", ll.traverse())  # [10, 20, 30]

    ll.delete_value(20)
    print("List after deleting 20:", ll.traverse())  # [10, 30]

    ll.delete_value(10)
    print("List after deleting 10:", ll.traverse())  # [30]

    ll.delete_value(30)
    print("List after deleting 30:", ll.traverse())  # []

    ll.insert_at_end(40)
    print("List after inserting 40:", ll.traverse())  # [40]
