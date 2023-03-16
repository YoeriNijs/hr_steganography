from unittest import TestCase

from __util import Util

from __encoder import Encoder


class TestEncoder(TestCase):
    encoder = Encoder()

    def test_when_update_sector_values_with_empty_sectors_then_expect_none(self):
        sectors = []
        self.encoder.update_sector_values('010', sectors)
        self.assertEqual([], sectors)

    def test_when_update_sector_values_with_zero_bit_expect_first_even(self):
        sectors = [[140, 142], [141]]
        self.encoder.update_sector_values('0', sectors)
        self.assertEqual([[140, 142], [142]], sectors)

    def test_when_update_sector_values_with_one_bit_expect_first_odd(self):
        sectors = [[140, 142], [141]]
        self.encoder.update_sector_values('1', sectors)
        self.assertEqual([[140, 142], [141]], sectors)

    def test_when_update_sector_values_with_second_first_bit_expect_increase(self):
        sectors = [[140, 142], [140, 140]]
        self.encoder.update_sector_values('01', sectors)
        self.assertEqual([[140, 142], [140, 141]], sectors)

    def test_when_update_sector_values_with_second_zero_bit_expect_decrease(self):
        sectors = [[140, 142], [140, 140]]
        self.encoder.update_sector_values('00', sectors)
        self.assertEqual([[140, 142], [140, 139]], sectors)

    def test_when_update_sector_values_with_range_zero_one_bits_expect_same_values(self):
        sectors = [[140, 142], [140, 140], [139, 140]]
        self.encoder.update_sector_values('0101', sectors)
        self.assertEqual([[140, 142], [140, 141], [140, 141]], sectors)

    def test_when_update_sector_values_with_only_one_bits_expect_same_values(self):
        sectors = [[140, 142], [140, 140], [139, 140]]
        self.encoder.update_sector_values('1111', sectors)
        self.assertEqual([[140, 142], [139, 140], [139, 140]], sectors)

    def test_when_update_sector_values_with_only_zero_bits_expect_same_values(self):
        sectors = [[140, 142], [140, 140], [139, 140]]
        self.encoder.update_sector_values('0000', sectors)
        self.assertEqual([[140, 142], [140, 139], [140, 139]], sectors)

    def test_when_update_sector_values_with_range_one_zero_bits_expect_same_values(self):
        sectors = [[140, 142], [140, 140], [139, 140]]
        self.encoder.update_sector_values('1010', sectors)
        self.assertEqual([[140, 142], [139, 138], [139, 138]], sectors)

    def test_when_sector_is_three_long_and_starts_with_zero_expect_valid(self):
        sectors = [[143, 140], [144, 140, 140]]
        self.encoder.update_sector_values('011', sectors)
        self.assertEqual([[143, 140], [144, 145, 146]], sectors)

    def test_when_sector_is_three_long_and_starts_with_zero_and_second_value_lower_expect_valid(self):
        sectors = [[143, 140], [144, 140, 140]]
        self.encoder.update_sector_values('100', sectors)
        self.assertEqual([[143, 140], [143, 140, 139]], sectors)

    def test_when_sector_is_three_long_and_starts_with_zero_and_second_value_higher_expect_valid(self):
        sectors = [[143, 140], [144, 150, 140]]
        self.encoder.update_sector_values('100', sectors)
        self.assertEqual([[143, 140], [143, 142, 140]], sectors)

    # FIXME: This test should not exist
    def test_integration(self):
        raw_values = [143, 144, 141, 142, 142, 144, 142, 141, 143, 143, 141, 140, 141, 141, 144, 140, 142, 143, 142,
                      143, 144, 142, 142, 142, 143, 140, 143, 144, 142, 143, 142, 140, 143, 144, 142, 141, 140, 141,
                      144, 140, 141, 144, 142, 140, 140, 143, 142, 141, 141, 141, 143, 144, 142, 144, 140, 144, 140,
                      140, 144, 144]
        sectors = Util.calculate_sectors(raw_values, 2)
        self.encoder.update_sector_values('011100110110010101100011011100100110010101110100', sectors)
        self.assertEqual([[143, 144], [142, 143], [141, 144], [142, 141], [143, 144], [142, 143], [141, 140],
                          [144, 145], [142, 143], [142, 143], [143, 142], [142, 141], [143, 144], [144, 145],
                          [141, 143], [142, 140], [143, 142], [142, 143], [139, 138], [144, 145], [142, 144],
                          [142, 143], [139, 143], [142, 143], [142, 141], [143, 143], [142, 144], [140, 144],
                          [140, 140], [144, 144]], sectors)
