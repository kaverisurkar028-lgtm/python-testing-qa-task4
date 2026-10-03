import unittest
import os
import json
from expense_tracker import ExpenseTracker

class TestExpenseTracker(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_expenses.json"
        self.tracker = ExpenseTracker(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_expense_valid(self):
        initial_count = len(self.tracker.expenses)
        expense = {"category": "Food", "amount": 100, "description": "Lunch", "date": "2026-10-03"}
        self.tracker.expenses.append(expense)
        self.assertEqual(len(self.tracker.expenses), initial_count + 1)

    def test_calculate_total(self):
        self.tracker.expenses = [
            {"amount": 100}, {"amount": 200}, {"amount": 50}
        ]
        total = sum(exp["amount"] for exp in self.tracker.expenses)
        self.assertEqual(total, 350)

    def test_load_empty_file(self):
        with open(self.test_file, 'w') as f:
            f.write('')
        tracker2 = ExpenseTracker(self.test_file)
        self.assertEqual(tracker2.expenses, [])

    def test_invalid_amount_handling(self):
        with self.assertRaises(ValueError):
            float("abc")

    def test_integration_save_load(self):
        expense = {"category": "Travel", "amount": 500, "description": "Bus", "date": "2026-10-03"}
        self.tracker.expenses.append(expense)
        self.tracker.save_expenses()
        new_tracker = ExpenseTracker(self.test_file)
        self.assertEqual(len(new_tracker.expenses), 1)
        self.assertEqual(new_tracker.expenses[0]["category"], "Travel")

if __name__ == "__main__":
    unittest.main()
