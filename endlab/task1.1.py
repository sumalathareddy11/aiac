import unittest
from task1 import SearchStack

class TestSearchStack(unittest.TestCase):
    def setUp(self):
        self.stack = SearchStack()
    
    def test_push_and_peek(self):
        self.stack.push("Pizza")
        self.assertEqual(self.stack.peek(), "Pizza")
    
    def test_push_multiple_and_peek_latest(self):
        self.stack.push("Pizza")
        self.stack.push("Burger")
        self.stack.push("Biryani")
        self.assertEqual(self.stack.peek(), "Biryani")
    
    def test_pop(self):
        self.stack.push("Pizza")
        self.stack.push("Burger")
        self.assertEqual(self.stack.pop(), "Burger")
        self.assertEqual(self.stack.peek(), "Pizza")
    
    def test_pop_empty_stack(self):
        self.assertIsNone(self.stack.pop())
    
    def test_peek_empty_stack(self):
        self.assertIsNone(self.stack.peek())
    
    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push("Pizza")
        self.assertFalse(self.stack.is_empty())
    
    def test_get_all_searches(self):
        self.stack.push("Pizza")
        self.stack.push("Burger")
        self.stack.push("Biryani")
        self.assertEqual(self.stack.get_all_searches(), ["Biryani", "Burger", "Pizza"])
    
    def test_get_all_searches_empty(self):
        self.assertEqual(self.stack.get_all_searches(), [])


if __name__== "__main__":
    unittest.main()