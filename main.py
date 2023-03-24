from __decoder import Decoder
from __encoder import Encoder
from __gpx_reader import GpxReader
from __gpx_writer import GpxWriter
from __steganalysis import StegAnalysis
from __util import Util
import logging

from cryptography.fernet import Fernet

class HrSteganography:

    __encoder = Encoder()
    __decoder = Decoder()
    __reader = GpxReader()
    __writer = GpxWriter()

    def encode(self, raw_heart_rates, secret_message) -> list:
        binary_message = Util.convert_message_to_binary(secret_message)
        logging.info(f"Converted message to binary message: '{binary_message}' with length: {len(binary_message)}")

        if len(binary_message) > len(raw_heart_rates):
            exit("Message is larger than number of heart rates!")

        return self.__encoder.encode(raw_heart_rates, binary_message)

    def decode(self, raw_heart_rates) -> str:
        binary = self.__decoder.decode(raw_heart_rates)
        return Util.convert_binary_to_message(binary)

    def read(self, file_name) -> list:
        return self.__reader.read(file_name)

    def write(self, from_file_name, to_file_name, heart_rates) -> None:
        self.__writer.write(from_file_name, to_file_name, heart_rates)

if __name__ == '__main__':
    while True:
        app = HrSteganography()

        choice = input("What do you want to do: (r)ead, (w)rite, (d)etect or (q)uit? ").lower()
        if choice == 'w':
            from_file_name = input("Enter the path of the file you want to use to hide your message: ")
            to_file_name = input('Enter file name of new activity file containing your secret message: ')
            message = input("Enter your secret message: ")
            if from_file_name and to_file_name and message:
                encryption_key = Fernet.generate_key()
                fernet = Fernet(encryption_key)
                encrypted_message_in_bytes = fernet.encrypt(message.encode())

                heart_rates = app.read(from_file_name)
                encrypted_message_str = encrypted_message_in_bytes.decode("utf-8")
                encoded_heart_rates = app.encode(heart_rates, encrypted_message_str)

                app.write(from_file_name, to_file_name, encoded_heart_rates)

                encryption_key_string = encryption_key.decode("utf-8")
                logging.info(f"Message successfully written to: '{to_file_name}' "
                             f"using encryption key: {encryption_key_string}")
            else:
                exit("No file names or message provided!")
        elif choice == 'r':
            from_file_name = input('Enter activity file name: ')
            decryption_key = input("Enter your encryption key for decryption: ")

            if not from_file_name or not decryption_key:
                exit("No file or decryption key provided!")

            written_heart_rates = app.read(from_file_name)
            decoded_message = app.decode(written_heart_rates)

            fernet = Fernet(decryption_key.encode())
            decrypted_message = fernet.decrypt(str.encode(decoded_message))
            decrypted_message_str = decrypted_message.decode("utf-8")
            logging.info(f"Decrypted message: {decrypted_message_str}")
        elif choice == 'd':
            file_name = input('Enter activity file name to detect steganography: ')
            if file_name:
                analysis = StegAnalysis()
                is_steganography_detected = analysis.detect(file_name)
                logging.info(f"Hidden message discovered: {is_steganography_detected}")
            else:
                exit("Invalid file")
        elif choice == 'q':
            exit("Bye")
        else:
            exit("Cannot determine what to do. Please enter 'r' or 'w' for read or write respectively.")




# D5lnQ99Mr6z-Mzr2FBedMKbPtGZ0831nWgw6h6vyvT0=