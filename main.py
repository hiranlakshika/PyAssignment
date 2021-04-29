import numpy as np
import matplotlib.pyplot as plt


def draw_histogram(bins):

    # example data
    mu = 100  # mean of distribution
    sigma = 15  # standard deviation of distribution
    x = mu + sigma * np.random.randn(15623)

    num_bins = bins

    fig, ax = plt.subplots()

    # the histogram of the data
    n, bins, patches = ax.hist(x, num_bins, density=True)

    degree_sign = u'\N{DEGREE SIGN}'

    # add a 'best fit' line
    y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
         np.exp(-0.5 * (1 / sigma * (bins - mu)) ** 2))
    print(type(y))
    ax.plot(bins, y, '-')
    ax.set_xlabel('Temperature [' + degree_sign + 'C]')
    ax.set_ylabel('Frequency')
    ax.set_title(r'Temperature in Tokyo in August 2010')

    # Tweak spacing to prevent clipping of ylabel
    fig.tight_layout()
    plt.show()


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


def set_values():
    temp_list = read_file("h201008", 8)
    min_temp = min(temp_list)
    max_temp = max(temp_list)


# dictionary = count_frequency(read_file("as5.txt", 8))
# plt.bar(list(dictionary.keys()), dictionary.values(), color='g')
# plt.show()

draw_histogram(20)
