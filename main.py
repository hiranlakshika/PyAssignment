import os
from itertools import accumulate

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from database import DatabaseUtil


def read_file(file, column):
    f = open(file, "r")
    lines = f.readlines()
    output = []
    i = 0
    while i < len(lines):
        result = lines[i].split()
        if result[column] != '999.0':
            output.append(result[column])
        i += 1
    f.close()

    return output


def count_frequency(my_list):
    count = {}
    for i in my_list:
        count[i] = count.get(i, 0) + 1
    return count


def draw(limit: bool, limit_value):
    dictionary = count_frequency(read_file("as5.txt", 8))
    x = np.array(list(dictionary.keys()))
    y = np.array(list(dictionary.values()))
    if limit:
        x = x[:limit_value]
        y = y[:limit_value]

    cum = list(accumulate(y))
    if limit:
        cum = cum[:limit_value]

    x.sort()

    degree_sign = u'\N{DEGREE SIGN}'
    x_key = 'Temperature [' + degree_sign + 'C]'
    y_key = 'Frequency'

    data = {x_key: x, y_key: y, 'Cumulative Frequency': cum}
    df = pd.DataFrame(data)
    plt.title('Temperature in Tokyo in August 2010')

    color = 'tab:green'
    ax1 = sns.barplot(x=x_key, y=y_key, data=df, palette='summer')
    ax1.tick_params(axis='y')

    ax2 = ax1.twinx()
    color = 'tab:red'

    ax2 = sns.lineplot(x=x_key, y='Cumulative Frequency', data=df, sort=False, color=color)
    ax2.tick_params(axis='y', color=color)
    plt.show()


# draw(True, 45)


def setup_db():
    date = read_file("as5.txt", 3)
    temp = read_file("as5.txt", 8)
    hour = read_file("as5.txt", 4)
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


setup_db()


def test():
    db = DatabaseUtil("test.db")
    df = db.get_processed_df()

    plt.figure(figsize=(15, 7))
    plt.plot(df.MAX_TEMP, color='red')
    plt.plot(df.AVG_TEMP, color='grey', linestyle='dashed')
    plt.plot(df.MIN_TEMP, color='blue')
    degree_sign = u'\N{DEGREE SIGN}'
    plt.xlabel('Date [day]')
    plt.ylabel('Temperature [' + degree_sign + 'C]')
    plt.title(
        'Temperature in August 2010 \n (Red: maximum temperature, grey: average temperature, blue: minimum temperature)')

    plt.show()


test()
