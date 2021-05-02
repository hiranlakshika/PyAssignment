import numpy as np
import matplotlib.pyplot as plt
from itertools import accumulate
import pandas as pd
import seaborn as sns


class Assignment5:

    def __init__(self, file, column, my_list, limit):
        self.file = file
        self.column = column
        self.my_list = my_list
        self.limit = limit

    def read_file(self):
        f = open(self.file, "r")
        lines = f.readlines()
        output = []
        i = 0
        while i < len(lines):
            result = lines[i].split()
            if result[self.column] != '999.0':
                output.append(result[self.column])
            i += 1
        f.close()

        return output

    def count_frequency(self, rec_list):
        count = {}
        for i in rec_list:
            count[i] = count.get(i, 0) + 1
        return count

    def draw(self, limit_value):
        dictionary = count_frequency(self, read_file("as5.txt", 8))
        x = np.array(list(dictionary.keys()))
        y = np.array(list(dictionary.values()))
        if self.limit:
            x = x[:limit_value]
            y = y[:limit_value]

        cum = list(accumulate(y))
        if self.limit:
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
