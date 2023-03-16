from itertools import chain

from __util import Util


class Encoder:

    def encode(self, heart_rates, binary_message) -> list:
        sector_length = Util.calculate_sector_length(heart_rates)
        sectors = Util.calculate_sectors(heart_rates, sector_length)
        self.update_sector_values(binary_message, sectors)
        return list(chain.from_iterable(sectors))

    def update_sector_values(self, binary_message, sectors) -> None:
        print(binary_message)
        bit_index = 0
        messaged_ended = False
        for sector in sectors[1:]:
            if messaged_ended:
                return

            sector_index = 0
            for value in sector:
                if bit_index >= len(binary_message):
                    sector[sector_index] = sector[0]
                    messaged_ended = True
                    sector_index += 1
                    continue

                bit = int(binary_message[bit_index])
                bit_index += 1

                if sector_index == 0:
                    should_be_even = bit == 0
                    is_even = (value % 2) == 0
                    if should_be_even and not is_even:
                        sector[sector_index] += 1
                    elif is_even and not should_be_even:
                        sector[sector_index] -= 1
                    # print('first', bit, value, should_be_even, is_even,  sector[sector_index-1])
                else:
                    should_be_higher = bit == 1
                    prev_value = sector[sector_index - 1]
                    is_equal = value == prev_value
                    is_higher = value > prev_value
                    if should_be_higher and not is_higher:
                        sector[sector_index] = prev_value + 1
                    elif is_higher and not should_be_higher:
                        sector[sector_index] = prev_value - 1
                    elif is_equal and not is_higher and not should_be_higher:
                        sector[sector_index] = prev_value - 1
                    # print('other', bit, prev_value, value, should_be_higher, is_higher, sector[sector_index])
                sector_index += 1
