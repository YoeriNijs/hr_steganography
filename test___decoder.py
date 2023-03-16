from unittest import TestCase

from __decoder import Decoder


class TestDecoder(TestCase):

    decoder = Decoder()

    def test_decode(self):
        heart_rates = [143, 144, 142, 143, 141, 144, 142, 141, 143, 144, 142, 143, 141, 140, 144, 145, 142, 143, 142,
                       143, 143, 142, 142, 141, 143, 144, 144, 145, 141, 143, 142, 140, 143, 142, 142, 143, 139, 138,
                       144, 145, 142, 144, 142, 143, 139, 143, 142, 143, 142, 141, 143, 143, 142, 144, 140, 144, 140,
                       140, 144, 144]
        bits = self.decoder.decode(heart_rates)
        self.assertEqual(bits, '011100110110010101100011011100100110010101110100')


    def test_sectors_to_bits_whenOnlyOneOddBit_thenExpectOne(self):
        sectors = [[150, 152, 154], [153]]
        result = self.decoder.sectors_to_bits(sectors)
        self.assertEqual(result, '1')

    def test_sectors_to_bits_whenOnlyOneEvenBit_thenExpectZero(self):
        sectors = [[150, 152, 154], [152]]
        result = self.decoder.sectors_to_bits(sectors)
        self.assertEqual(result, '0')

    def test_sectors_to_bits_whenFirstBitIsOddAndSecondBitIsHigher_thenExpectOneOne(self):
        sectors = [[150, 152, 154], [151, 152]]
        result = self.decoder.sectors_to_bits(sectors)
        self.assertEqual(result, '11')

    def test_sectors_to_bits_whenFirstBitIsOddAndSecondBitIsLower_thenExpectOneZero(self):
        sectors = [[150, 152, 154], [151, 150]]
        result = self.decoder.sectors_to_bits(sectors)
        self.assertEqual(result, '10')

    def test_sectors_to_bits_whenFirstBitIsEvenAndSecondBitIsHigher_thenExpectZeroOne(self):
        sectors = [[150, 152, 154], [150, 152]]
        result = self.decoder.sectors_to_bits(sectors)
        self.assertEqual(result, '01')

    def test_sectors_to_bits_whenFirstBitIsEvenAndSecondBitIsLower_thenExpectZeroZero(self):
        sectors = [[150, 152, 154], [150, 149]]
        result = self.decoder.sectors_to_bits(sectors)
        self.assertEqual(result, '00')

    def test_sectors_to_bits_whenOneSector_thenExpectNone(self):
        sectors = [[150, 152, 154]]
        result = self.decoder.sectors_to_bits(sectors)
        self.assertEqual(result, None)

    def test_sectors_to_bits_whenEmptyList_thenExpectNone(self):
        sectors = []
        result = self.decoder.sectors_to_bits(sectors)
        self.assertEqual(result, None)
