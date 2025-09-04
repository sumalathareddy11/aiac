import unittest
from task4 import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_item_new(self):
        self.cart.add_item("apple", 1.5)
        self.assertIn("apple", self.cart.items)
        self.assertEqual(self.cart.items["apple"], [1.5])

    def test_add_item_existing(self):
        self.cart.add_item("banana", 2.0)
        self.cart.add_item("banana", 3.0)
        self.assertEqual(self.cart.items["banana"], [2.0, 3.0])

    def test_remove_item_single(self):
        self.cart.add_item("orange", 1.0)
        self.cart.remove_item("orange")
        self.assertNotIn("orange", self.cart.items)

    def test_remove_item_multiple(self):
        self.cart.add_item("pear", 2.0)
        self.cart.add_item("pear", 3.0)
        self.cart.remove_item("pear")
        self.assertIn("pear", self.cart.items)
        self.assertEqual(self.cart.items["pear"], [2.0])
        self.cart.remove_item("pear")
        self.assertNotIn("pear", self.cart.items)

    def test_remove_item_not_found(self):
        # Should not raise, just print
        self.cart.remove_item("notfound")

    def test_total_cost_empty(self):
        self.assertEqual(self.cart.total_cost(), 0)

    def test_total_cost_multiple_items(self):
        self.cart.add_item("apple", 1.5)
        self.cart.add_item("banana", 2.5)
        self.cart.add_item("banana", 3.0)
        self.assertEqual(self.cart.total_cost(), 1.5 + 2.5 + 3.0)

if __name__ == "__main__":
    unittest.main()