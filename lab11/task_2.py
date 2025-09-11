"""
Queue Implementation Comparison: List vs Collections.deque

This module demonstrates two different implementations of a Queue data structure:
1. List-based implementation (less efficient)
2. Collections.deque-based implementation (more efficient)

A queue follows the FIFO (First In, First Out) principle.
"""

from collections import deque
import time


class ListQueue:
    """
    Queue implementation using Python lists.
    
    PERFORMANCE ANALYSIS:
    - enqueue(): O(1) - append() is O(1) amortized
    - dequeue(): O(n) - pop(0) requires shifting all elements
    - is_empty(): O(1) - len() check is O(1)
    
    The main performance issue is with dequeue() operation which is O(n)
    because removing from the front of a list requires shifting all remaining
    elements to the left.
    """
    
    def __init__(self):
        """Initialize an empty queue."""
        self.items = []
    
    def enqueue(self, item):
        """
        Add an item to the rear of the queue.
        
        Args:
            item: The item to be added to the queue.
        """
        self.items.append(item)
    
    def dequeue(self):
        """
        Remove and return the item from the front of the queue.
        
        Returns:
            The item at the front of the queue.
            
        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)  # O(n) operation - inefficient!
    
    def is_empty(self):
        """
        Check if the queue is empty.
        
        Returns:
            True if the queue is empty, False otherwise.
        """
        return len(self.items) == 0


class DequeQueue:
    """
    Queue implementation using collections.deque.
    
    PERFORMANCE ANALYSIS:
    - enqueue(): O(1) - append() is O(1)
    - dequeue(): O(1) - popleft() is O(1)
    - is_empty(): O(1) - len() check is O(1)
    
    This implementation is much more efficient because deque is optimized
    for operations at both ends, making both enqueue and dequeue O(1).
    """
    
    def __init__(self):
        """Initialize an empty queue."""
        self.items = deque()
    
    def enqueue(self, item):
        """
        Add an item to the rear of the queue.
        
        Args:
            item: The item to be added to the queue.
        """
        self.items.append(item)
    
    def dequeue(self):
        """
        Remove and return the item from the front of the queue.
        
        Returns:
            The item at the front of the queue.
            
        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.popleft()  # O(1) operation - efficient!
    
    def is_empty(self):
        """
        Check if the queue is empty.
        
        Returns:
            True if the queue is empty, False otherwise.
        """
        return len(self.items) == 0


def test_queue_operations(queue, queue_name):
    """
    Test queue operations with sample data.
    
    Args:
        queue: The queue instance to test
        queue_name: Name of the queue implementation for display
    """
    print(f"\n=== Testing {queue_name} ===")
    
    # Test initial state
    print(f"Is queue empty? {queue.is_empty()}")
    
    # Test enqueue operations
    print("\n--- Testing enqueue() operations ---")
    test_data = [10, 20, 30, "hello", 3.14, True]
    
    for item in test_data:
        queue.enqueue(item)
        print(f"Enqueued: {item}")
    
    print(f"Queue after enqueuing all items. Is empty? {queue.is_empty()}")
    
    # Test dequeue operations
    print("\n--- Testing dequeue() operations ---")
    while not queue.is_empty():
        try:
            dequeued_item = queue.dequeue()
            print(f"Dequeued: {dequeued_item}")
        except IndexError as e:
            print(f"Error: {e}")
    
    print(f"Queue after dequeuing all items. Is empty? {queue.is_empty()}")
    
    # Test error handling
    print("\n--- Testing error handling ---")
    try:
        queue.dequeue()
    except IndexError as e:
        print(f"Expected error when dequeuing from empty queue: {e}")


def performance_comparison():
    """
    Compare performance between ListQueue and DequeQueue implementations.
    """
    print("\n" + "="*60)
    print("PERFORMANCE COMPARISON")
    print("="*60)
    
    # Test data sizes
    sizes = [1000, 5000, 10000]
    
    for size in sizes:
        print(f"\nTesting with {size} operations:")
        
        # Test ListQueue
        list_queue = ListQueue()
        start_time = time.time()
        
        # Enqueue operations
        for i in range(size):
            list_queue.enqueue(i)
        
        # Dequeue operations
        for i in range(size):
            list_queue.dequeue()
        
        list_time = time.time() - start_time
        
        # Test DequeQueue
        deque_queue = DequeQueue()
        start_time = time.time()
        
        # Enqueue operations
        for i in range(size):
            deque_queue.enqueue(i)
        
        # Dequeue operations
        for i in range(size):
            deque_queue.dequeue()
        
        deque_time = time.time() - start_time
        
        print(f"  ListQueue time: {list_time:.4f} seconds")
        print(f"  DequeQueue time: {deque_time:.4f} seconds")
        print(f"  Speedup: {list_time/deque_time:.2f}x faster with deque")


def demonstrate_fifo_principle():
    """
    Demonstrate the FIFO (First In, First Out) principle of queues.
    """
    print("\n" + "="*60)
    print("FIFO PRINCIPLE DEMONSTRATION")
    print("="*60)
    
    # Use DequeQueue for demonstration
    queue = DequeQueue()
    
    print("Adding items in order: A, B, C, D")
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    queue.enqueue("D")
    
    print("\nRemoving items (should be in same order):")
    while not queue.is_empty():
        item = queue.dequeue()
        print(f"Removed: {item}")


if __name__ == "__main__":
    # Test both implementations
    test_queue_operations(ListQueue(), "List-based Queue")
    test_queue_operations(DequeQueue(), "Deque-based Queue")
    
    # Demonstrate FIFO principle
    demonstrate_fifo_principle()
    
    # Performance comparison
    performance_comparison()
    
    print("\n" + "="*60)
    print("RECOMMENDATION")
    print("="*60)
    print("Use collections.deque for queue implementation because:")
    print("1. Both enqueue() and dequeue() are O(1) operations")
    print("2. List-based implementation has O(n) dequeue() operation")
    print("3. Deque is specifically designed for efficient operations at both ends")
    print("4. Significant performance improvement for large datasets")
