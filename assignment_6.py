import os

import utility
from database import DatabaseUtil
import matplotlib.pyplot as plt


class Assignment6:
    __db = DatabaseUtil(utility.database_name)

    def __setup_db(self):
        date = utility.read_file("as5.txt", 3)
        temp = utility.read_file("as5.txt", 8)
        hour = utility.read_file("as5.txt", 4)

        os.remove(utility.database_name)
        self.__db.create_db()

        i = 0
        while i < len(date):
            temp_id = '8' + date[i] + hour[i] + temp[i]
            self.__db.insert_temp_data(temp_id, date[i], temp[i], hour[i])
            i += 1

        unique_date = set(date)
        for day in unique_date:
            self.__db.insert_processed_data(day, str(self.__db.get_max_temp(day)), str(self.__db.get_min_temp(day)),
                                            str(round(self.__db.get_avg_temp(day), 2)))

    def draw(self):
        self.__setup_db()
        df = self.__db.get_table_as_df('PROCESSED_TEMP')

        plt.figure(figsize=(15, 7))
        plt.plot(df.MAX_TEMP, color='red')
        plt.plot(df.AVG_TEMP, color='grey', linestyle='dashed')
        plt.plot(df.MIN_TEMP, color='blue')

        plt.xlabel('Date [day]')
        plt.ylabel('Temperature [' + utility.degree_sign + 'C]')
        plt.title(
            'Temperature in August 2010 \n (Red: maximum temperature, grey: average temperature, blue: minimum temperature)')

        plt.show()
