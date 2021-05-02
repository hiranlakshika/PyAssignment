from itertools import accumulate

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

import utility


class Assignment5:

    def count_frequency(self, my_list):
        count = {}
        for i in my_list:
            count[i] = count.get(i, 0) + 1
        return count

    def draw(self, limit: bool, limit_value):
        dictionary = self.count_frequency(utility.read_file("as5.txt", 8))
        x = np.array(list(dictionary.keys()))
        y = np.array(list(dictionary.values()))
        if limit:
            x = x[:limit_value]
            y = y[:limit_value]

        cum = list(accumulate(y))
        if limit:
            cum = cum[:limit_value]

        x.sort()

        x_key = 'Temperature [' + utility.degree_sign + 'C]'
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
