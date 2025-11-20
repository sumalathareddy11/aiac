class SearchStack:
    """
    A stack data structure for managing search queries in LIFO (Last-In-First-Out) order.
    This class implements a stack to store and retrieve search queries, with the most
    recent search always accessible at the top of the stack. It provides standard stack
    operations including push, pop, and peek, along with utility methods to check if
    the stack is empty and retrieve all searches in reverse chronological order.
    Attributes:
        searches (list): Internal list storing search queries in the order they were added.
    Methods:
        push(search_query): Add a new search query to the top of the stack.
        pop(): Remove and return the most recent search query from the stack.
        peek(): View the most recent search query without removing it from the stack.
        is_empty(): Check whether the stack contains any search queries.
        get_all_searches(): Retrieve all search queries with the most recent first.
    """
    def init(self):
        self.searches = []
    
    def push(self, search_query):
        """Add a new search to the stack"""
        self.searches.append(search_query)
    
    def pop(self):
        """Remove and return the most recent search"""
        if not self.is_empty():
            return self.searches.pop()
        return None
    
    def peek(self):
        """View the most recent search without removing it"""
        if not self.is_empty():
            return self.searches[-1]
        return None
    
    def is_empty(self):
        """Check if stack is empty"""
        return len(self.searches) == 0
    
    def get_all_searches(self):
        """Return all searches with latest first"""
        return self.searches[::-1]


# Example usage
if __name__ == "__main_":
    stack = SearchStack()
    
    # Get number of searches from user
    n = int(input("Enter the number of searches to add: "))
    
    # Get search queries from user
    print("Enter the search queries:")
    for i in range(n):
        search = input(f"Search {i+1}: ")
        stack.push(search)
    
    print("\nMost recent search:", stack.peek())
    print("All searches (latest first):", stack.get_all_searches())
    
    print("\nPopped:", stack.pop())
    print("Remaining searches:", stack.get_all_searches())