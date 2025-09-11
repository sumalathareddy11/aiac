class Stack:
    """
    A simple Stack implementation using a Python list.
    """

    def __init__(self):
        """
        Initialize an empty stack.
        """
        self.items = []

    def push(self, item):
        """
        Push an item onto the stack.

        Args:
            item: The item to be pushed onto the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Remove and return the top item from the stack.

        Returns:
            The item at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """
        Return the top item from the stack without removing it.

        Returns:
            The item at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0


# Test stack operations using sample data
if __name__ == "__main__":
    stack = Stack()
    print("Is stack empty?", stack.is_empty())  # True

    # Push elements
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Stack after pushes:", stack.items)  # [10, 20, 30]

    # Peek at the top element
    print("Peek:", stack.peek())  # 30

    # Pop elements
    print("Pop:", stack.pop())  # 30
    print("Pop:", stack.pop())  # 20

    # Check if stack is empty
    print("Is stack empty?", stack.is_empty())  # False

    # Pop last element
    print("Pop:", stack.pop())  # 10

    # Now stack should be empty
    print("Is stack empty?", stack.is_empty())  # True

    # Uncomment to test error handling
    # print("Pop from empty stack:", stack.pop())
