from unittest import TestCase

from __util import Util
from encoding_exception import EncodingException


class TestUtil(TestCase):

    def test_when_calculate_sector_length_with_invalid_values_then_expect_encoding_exception(self):
        with self.assertRaises(EncodingException):
            Util.calculate_sector_length([])
            Util.calculate_sector_length([1])

    def test_when_calculate_sector_length_with_valid_values_then_expect_valid_values(self):
        self.assertEqual(Util.calculate_sector_length([1, 2]), 2)
        self.assertEqual(Util.calculate_sector_length([3, 5]), 2),
        self.assertEqual(Util.calculate_sector_length([1, 1]), 2)
        self.assertEqual(Util.calculate_sector_length([1, 3]), 2)

    def test_when_calculate_sectors_with_length_even_then_expect_valid_value(self):
        sectors = Util.calculate_sectors([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)
        self.assertEqual(sectors, [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])

    def test_when_calculate_sectors_with_length_odd_then_expect_valid_value(self):
        sectors = Util.calculate_sectors([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)
        self.assertEqual(sectors, [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]])