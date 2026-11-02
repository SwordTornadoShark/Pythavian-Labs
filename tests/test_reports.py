# tests/test_reports.py

import unittest
from features.reports import category_report

class TestCategoryReport(unittest.TestCase):
    
    def test_category_report_sample_deck(self):
        data = {
            "cards": [
                {"question": "Q1", "answer": "A1", "category": "Python"},
                {"question": "Q2", "answer": "A2", "category": "Python"},
                {"question": "Q3", "answer": "A3", "category": "JavaScript"},
            ]
        }
        expected = {"Python": 2, "JavaScript": 1}
        self.assertEqual(category_report(data), expected)

    def test_category_report_empty_deck(self):
        data = {"cards": []}
        self.assertEqual(category_report(data), {})

if __name__ == "__main__":
    unittest.main()