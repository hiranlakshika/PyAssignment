import numpy as np
import matplotlib.pyplot as plt
from itertools import accumulate
import pandas as pd
import seaborn as sns


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


def draw(limit: bool):
    dictionary = count_frequency(read_file("as5.txt", 8))
    x = np.array(list(dictionary.keys()))
    y = np.array(list(dictionary.values()))
    if limit:
        x = x[:45]
        y = y[:45]

    cum = list(accumulate(y))
    if limit:
        cum = cum[:45]

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


draw(True)
