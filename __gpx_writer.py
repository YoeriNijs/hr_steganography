class GpxWriter:
    __begin_tag = '<ns3:hr>'
    __end_tag = '</ns3:hr>'

    def write(self, from_file_name, to_file_name, heart_rates) -> None:
        if len(heart_rates) < 1:
            return

        heart_rates_index = 0
        new_lines = []
        with open(from_file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if self.__begin_tag in line and self.__end_tag in line:
                    if heart_rates_index >= len(heart_rates):
                        break

                    begin_index = line.index(self.__begin_tag)+len(self.__begin_tag)
                    end_index = line.index(self.__end_tag)
                    heart_rate = line[begin_index:end_index]
                    updated_heart_rate = heart_rates[heart_rates_index]
                    updated_heart_rate_str = str(updated_heart_rate)
                    new_line = line.replace(heart_rate, updated_heart_rate_str)
                    new_lines.append(new_line)

                    heart_rates_index += 1
                else:
                    new_lines.append(line)

        with open(to_file_name, 'w') as file:
            for new_line in new_lines:
                file.write(new_line)

