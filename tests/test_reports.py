import unittest

from features import reports


class TestReports(unittest.TestCase):

    def test_average_score_empty_history(self):
        """Test that an empty history list returns 0.0."""
        data = {"history": []}
        self.assertEqual(reports.average_score(data), 0.0)

    def test_average_score_with_data(self):
        """Test that average score is correctly computed for a list of scores."""
        data = {"history": [80, 90, 100]}
        self.assertEqual(reports.average_score(data), 90.0)


if __name__ == "__main__":
    unittest.main()