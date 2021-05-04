import os

import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import host_subplot

import utility
from database import DatabaseUtil


class Assignment7:
    __db = DatabaseUtil(utility.database_name)

    def __setup_db(self, region_text_file):
        if os.path.exists(utility.database_name):
            os.remove(utility.database_name)

        hour = utility.read_file(region_text_file, 4)
        wind_s = utility.read_file(region_text_file, 7)
        wind_d = utility.read_file(region_text_file, 6)

        self.__db.create_db()

        i = 0
        while i < 24:
            temp_id = '8' + hour[i] + wind_s[i] + wind_d[i]
            self.__db.insert_wind_data(temp_id, hour[i], wind_s[i], wind_d[i])
            i += 1

    def draw(self, region_text_file='as7.txt'):
        self.__setup_db(region_text_file)
        df = self.__db.get_table_as_df('WIND_REC')

        host = host_subplot(111)

        par = host.twinx()

        host.set_xlabel("Time [Hour]")
        host.set_ylabel("Wind Speed [m/s]")
        par.set_ylabel("Wind Direction [degree]")

        p1, = host.plot(df.HOUR, df.WIND_S, color='black')
        p2, = par.plot(df.HOUR, df.WIND_D, linestyle="dotted", color='black')

        plt.title('Wind direction and speed on August 17, 2010\n(Line: wind speed, dot: wind direction)')
        plt.show()
