from __util import Util

# Responsible for decoding a sequence of heart rates to a binary string.
class Decoder:
    def decode(self, heart_rates) -> str | None:
        sector_length = Util.calculate_sector_length(heart_rates)
        sectors = Util.calculate_sectors(heart_rates, sector_length)
        return self.sectors_to_bits(sectors)

    def sectors_to_bits(self, sectors) -> str | None:
        if len(sectors) < 2:
            return None

        bits = ''
        for sector in sectors[1:]:
            sector_length = len(sector)

            # If we only have one sector here, we just handle that one.
            if sector_length < 2:
                current_sector = sector[0]
                is_even = (current_sector % 2) == 0
                if is_even:
                    bits += '0'
                else:
                    bits += '1'

            # If we have more than one sector, we iterate over all sectors
            else:
                for sector_index in range(0, sector_length):
                    # If we have had all sectors, just break
                    if sector_index == sector_length:
                        break

                    current_sector = sector[sector_index]
                    if sector_index == 0:
                        # Of the current sector bit is the next sector bit,
                        # we know that we have reached the end of our encoded message.
                        if sector[sector_index+1] == current_sector:
                            return bits

                        # Validate the first hr value of the sector. If it is even, decode it to
                        # 0. If it is odd, decode it to 1.
                        is_even = (current_sector % 2) == 0
                        if is_even:
                            bits += '0'
                        else:
                            bits += '1'
                    else:
                        # If the current sector is the same as the previous sector,
                        # we know that we have reached the end of our encoded message.
                        if sector[sector_index-1] == current_sector:
                            return bits

                        # If the current sector value is lower than the previous value,
                        # we know we can decode it to 0. If the current value is higher,
                        # this means we can decode it to 1.
                        prev_sector = sector[sector_index-1]
                        distance = prev_sector - current_sector
                        if distance < 0:
                            bits += '1'
                        elif distance > 0:
                            bits += '0'
        return bits



  