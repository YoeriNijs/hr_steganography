import math
import os

from __gpx_reader import GpxReader

from __util import Util


def is_zero(value):
    return int(value) == 0

# Responsible for detecting steganography in gpx files. For this, it uses a baseline that holds valid
# gpx files, and calculates an average of the number of zeroes (i.e. the times when subsequent heart rates are equal).
# The baseline is calculated using existing gpx files that are stored in the __baseline__ dir.
class StegAnalysis:

    __reader = GpxReader()

    def detect(self, file) -> bool:
        zeroes = []
        baseline_dir = os.path.join(os.getcwd(), '__baseline__')
        baseline_files = os.listdir(baseline_dir)
        for baseline_file in baseline_files:
            if baseline_file.endswith('.gpx'):
                baseline_file_path = os.path.join(baseline_dir, baseline_file)
                baseline_sectors = self.__calculate_sectors_for_file(baseline_file_path)
                n_zeroes = self.calculate_percentage_zero_for_sectors(baseline_sectors)
                zeroes.append(n_zeroes)
        avg_zeroes = float(sum(zeroes) / len(zeroes))
        current_sectors = self.__calculate_sectors_for_file(file)
        detected_zeroes = self.calculate_percentage_zero_for_sectors(current_sectors)
        return detected_zeroes < avg_zeroes

    def calculate_percentage_zero_for_sectors(self, sectors) -> int:
        differences = []
        for sector_index in range(0, 60):
            if sector_index > len(sectors) - 1:
                continue
            sector = sectors[sector_index]
            for heart_rate_index in range(0, len(sector)):
                current_heart_rate = sector[heart_rate_index]
                if heart_rate_index > 0:
                    prev_heart_rate = sector[heart_rate_index - 1]
                    difference = current_heart_rate - prev_heart_rate
                    differences.append(difference)
        total_count = len(differences)
        if total_count == 0:
            return 100
        total_zeros = len(list((filter(is_zero, differences))))
        return math.floor((100 / total_count) * total_zeros)

    def __calculate_sectors_for_file(self, file_path) -> list:
        heart_rates = self.__reader.read(file_path)
        sector_length = Util.calculate_sector_length(heart_rates)
        return Util.calculate_sectors(heart_rates, sector_length)
