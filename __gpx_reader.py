class GpxReader:
    __begin_tag = '<ns3:hr>'
    __end_tag = '</ns3:hr>'

    def read(self, file_name) -> list:
        heart_rates = []
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if self.__begin_tag in line and self.__end_tag in line:
                    begin_index = line.index(self.__begin_tag)+len(self.__begin_tag)
                    end_index = line.index(self.__end_tag)
                    heart_rate = line[begin_index:end_index]
                    heart_rates.append(int(heart_rate))

        return heart_rates

