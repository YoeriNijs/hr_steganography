import binascii
import logging

from __constants import HEX_AND_BINARY
from encoding_exception import EncodingException


class Util:

    @staticmethod
    def convert_hex_to_binary(hex_value) -> str:
        hex_uppercase = hex_value.upper()
        return HEX_AND_BINARY.get(hex_uppercase)

    @staticmethod
    def convert_message_to_binary(message, result='') -> str:
        message_in_bytes = bytes(message, encoding='utf-8')
        message_in_hex_string = str(binascii.hexlify(message_in_bytes))
        message_in_hex_substring = message_in_hex_string[2:len(message_in_hex_string) - 1]
        for hex_value in message_in_hex_substring:
            result += Util.convert_hex_to_binary(hex_value)
        return result

    @staticmethod
    def convert_binary_to_message(binary) -> str:
        binary_length = len(binary)
        message = ''
        for byte_index in range(binary_length // 8):
            ordinal = int(binary[byte_index * 8: byte_index * 8 + 8], 2)
            char = chr(ordinal)
            message += char
        return message

    @staticmethod
    def calculate_sector_length(values) -> int:
        if len(values) < 2:
            raise EncodingException("Invalid length!")

        sector_length = values[0] - values[1]
        if sector_length < 0:
            sector_length *= -1

        if sector_length <= 1:
            sector_length = 2

        logging.info(f"Calculated sector length: {sector_length}")
        return sector_length

    @staticmethod
    def calculate_sectors(values, length):
        sectors = []
        for value in values:
            if len(sectors) < 1:
                sectors.append([value])
                continue

            last_sector = sectors[len(sectors) - 1]
            if len(last_sector) < length:
                sectors[len(sectors) - 1].append(value)
                continue

            sectors.append([value])
        return sectors