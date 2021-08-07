import unittest
from analytics import sum_deviations_squared, list_to_dataframe, max_deviation
import numpy as np


class AnalyticsTests(unittest.TestCase):
    def test_sum_deviations_squared(self):
        a = [2, 5, 11]
        b = [1, 8, 3]

        expected = (2 - 1) ** 2 + (5 - 8) ** 2 + (11 - 3) ** 2
        self.assertEqual(expected, sum_deviations_squared(a, b))

    def test_list_to_dataframe(self):
        lst = [
            {'a': 1, 'b': 2},
            {'a': 3, 'b': 4},
        ]
        expected = {
            'a': {0: 1, 1: 3},
            'b': {0: 2, 1: 4}
        }
        self.assertEqual(expected, list_to_dataframe(lst).to_dict())

    def test_max_deviation(self):
        a = np.array([1, 2, 3])
        b = np.array([5, 1, 9.5])

        self.assertEqual(6.5, max_deviation(a, b))