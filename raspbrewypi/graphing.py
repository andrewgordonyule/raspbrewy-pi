import matplotlib.pyplot as plt

# set up graph
plt.ion()
x = []
y = []



# Displays data on graph
def plot_graph(temp_log, current_time):
    y.append(temp_log)
    x.append(current_time)
    plt.clf()
    plt.scatter(x, y)
    plt.plot(x, y)

    plt.pause(0.1)
    plt.draw()