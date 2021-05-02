import os

import utility
from database import DatabaseUtil
import matplotlib.pyplot as plt


class Assignment6:
    def setup_db(self):
        date = utility.read_file("as5.txt", 3)
        temp = utility.read_file("as5.txt", 8)
        hour = utility.read_file("as5.txt", 4)
        db = DatabaseUtil("test.db")
        if not os.path.isfile("test.db"):
            db.create_db()

            i = 0
            while i < len(date):
                temp_id = '8' + date[i] + hour[i] + temp[i]
                db.insert_temp_data(temp_id, date[i], temp[i], hour[i])
                i += 1

            unique_date = set(date)
            for day in unique_date:
                db.insert_processed_data(day, str(db.get_max_temp(day)), str(db.get_min_temp(day)),
                                         str(round(db.get_avg_temp(day), 2)))

    def draw(self):
        self.setup_db()
        db = DatabaseUtil("test.db")
        df = db.get_processed_df()

        plt.figure(figsize=(15, 7))
        plt.plot(df.MAX_TEMP, color='red')
        plt.plot(df.AVG_TEMP, color='grey', linestyle='dashed')
        plt.plot(df.MIN_TEMP, color='blue')

        plt.xlabel('Date [day]')
        plt.ylabel('Temperature [' + utility.degree_sign + 'C]')
        plt.title(
            'Temperature in August 2010 \n (Red: maximum temperature, grey: average temperature, blue: minimum temperature)')

        plt.show()
