from __util import Util


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
            if sector_length < 2:
                current_sector = sector[0]
                is_even = (current_sector % 2) == 0
                if is_even:
                    bits += '0'
                else:
                    bits += '1'
            else:
                for sector_index in range(0, sector_length):
                    if sector_index == sector_length:
                        break

                    current_sector = sector[sector_index]
                    if sector_index == 0:
                        if sector[sector_index+1] == current_sector:
                            return bits

                        is_even = (current_sector % 2) == 0
                        if is_even:
                            bits += '0'
                        else:
                            bits += '1'
                    else:
                        if sector[sector_index-1] == current_sector:
                            return bits

                        prev_sector = sector[sector_index-1]
                        distance = prev_sector - current_sector
                        if distance < 0:
                            bits += '1'
                        elif distance > 0:
                            bits += '0'
        return bits



  