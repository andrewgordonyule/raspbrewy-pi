import matplotlib.pyplot as plt
from time import time

# set up graph
plt.ion()
x = []
y = []


# Displays data on graph
def plot_graph(temp_log):
    y.append(temp_log)
    x.append(time())
    plt.clf()
    plt.scatter(x, y)
    plt.plot(x, y)

    plt.pause(0.1)
    plt.draw()