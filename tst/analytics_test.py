import unittest
from analytics import sum_deviations_squared, list_to_dataframe


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