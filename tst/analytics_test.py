import unittest
from analytics import sum_deviations_squared


class AnalyticsTests(unittest.TestCase):
    def test_sum_deviations_squared(self):
        a = [2, 5, 11]
        b = [1, 8, 3]

        expected = (2 - 1) ** 2 + (5 - 8) ** 2 + (11 - 3) ** 2
        self.assertEqual(expected, sum_deviations_squared(a, b))