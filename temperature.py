import pandas as pd
from matplotlib import pyplot as plt


def read_data(num_measurements):
    """read data from file"""
    data = pd.read_csv("temperatures.csv", nrows=num_measurements)
    temperatures = data["Air temperature (degC)"]
    return temperatures


def compute_mean(temperatures, num_measurements):
    """compute statistics"""
    return sum(temperatures) / num_measurements
    

def plot_data(temperatures, mean, fname):
    """plot results"""
    plt.plot(temperatures, "r-")
    plt.title("temperatures in Helsinki")
    plt.xlabel("measurements")
    plt.ylabel("air temperature (deg C)")
    plt.axhline(y=mean, color="b", linestyle="--")
    plt.show()
    plt.savefig(fname)
    plt.clf()


for measurement in [25, 100, 500]:
    temperatures = read_data(measurement)
    mean = compute_mean(temperatures, measurement)
    plot_data(temperatures, mean, f"{measurement}.png")

