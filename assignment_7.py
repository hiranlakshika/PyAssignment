import os

import utility
from database import DatabaseUtil
import matplotlib.pyplot as plt


class Assignment7:
    __db = DatabaseUtil(utility.database_name)

    def __setup_db(self, region_text_file):
        hour = utility.read_file(region_text_file, 4)
        wind_s = utility.read_file(region_text_file, 7)
        wind_d = utility.read_file(region_text_file, 6)

        os.remove(utility.database_name)
        self.__db.create_db()

        i = 0
        while i < 24:
            temp_id = '8' + hour[i] + wind_s[i] + wind_d[i]
            self.__db.insert_wind_data(temp_id, hour[i], wind_s[i], wind_d[i])
            i += 1

    def draw(self, region_text_file='as7.txt'):
        self.__setup_db(region_text_file)
        df = self.__db.get_table_as_df('WIND_REC')

        plt.figure(figsize=(15, 7))
        plt.plot(df.WIND_S, color='black')
        plt.plot(df.WIND_D, color='black', linestyle='dotted')

        plt.xlabel('Time [Hour]')
        plt.ylabel('Wind Speed [m/s]')
        plt.title('Wind direction and speed on August 17, 2010\n(Line: wind speed, dot: wind direction)')
        plt.show()
