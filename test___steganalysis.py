from unittest import TestCase

from __steganalysis import StegAnalysis

class TestStegAnalysis(TestCase):
    __analyzer = StegAnalysis()

    def test_calculate_percentage_zero_for_sectors_when_less_then_60_expect_all_zeroes(self):
        sectors = self.__create_list_with_items(59)
        result = self.__analyzer.calculate_percentage_zero_for_sectors(sectors)
        self.assertEqual(100, result)

    def test_calculate_percentage_zero_for_sectors_when_60_expect_all_zeroes(self):
        sectors = self.__create_list_with_items(60)
        result = self.__analyzer.calculate_percentage_zero_for_sectors(sectors)
        self.assertEqual(100, result)

    def test_calculate_percentage_zero_for_sectors_when_above_60_expect_all_zeroes(self):
        sectors = self.__create_list_with_items(61)
        result = self.__analyzer.calculate_percentage_zero_for_sectors(sectors)
        self.assertEqual(100, result)

    def test_calculate_percentage_zero_for_sectors_when_difference_expect_zero(self):
        sectors = [[100, 101]]
        result = self.__analyzer.calculate_percentage_zero_for_sectors(sectors)
        self.assertEqual(0, result)

    def test_calculate_percentage_zero_for_sectors_when_no_difference_expect_hundred(self):
        sectors = [[100, 100]]
        result = self.__analyzer.calculate_percentage_zero_for_sectors(sectors)
        self.assertEqual(100, result)

    def test_calculate_percentage_zero_for_sectors_when_no_difference_expect_one_third(self):
        sectors = [[100, 101, 101, 100], [103, 100, 100, 100], [100, 100, 101, 102], [130, 131, 130, 131]]
        result = self.__analyzer.calculate_percentage_zero_for_sectors(sectors)
        self.assertEqual(33, result)

    def __create_list_with_items(self, n_items) -> list:
        items = []
        for _ in range(0, n_items):
            items.append([100])
        return items

