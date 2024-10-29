import matplotlib.pyplot as plt
import numpy as np

"""
Step 0: Select which database you wish to use.
"""

# database name
database_name = 'mitdb_201'

# path to ekg folder
path_to_folder = "../../../data/ekg/"

# select a signal file to run
signal_filepath = path_to_folder + database_name + ".csv"

"""
Step #1: load data in matrix from CSV file; skip first two rows. Call the data signal.
"""

signal = np.loadtxt(signal_filepath, skiprows=2, delimiter=',')

Time = signal[:, 0]
MLII = signal[:, 1]
Voltage = signal[:, 2]

plt.title('Process Signal for ' + database_name)
plt.plot(Time, Voltage)
plt.xlabel('Time (s)')
plt.ylabel('Voltage')
plt.show()

"""
Step 2: (OPTIONAL) pass data through LOW PASS FILTER (fs=250Hz, fc=15, N=6). These may not be correctly in radians
"""

"""
Step 3: Pass data through weighted differentiator
"""

Diff_time = np.diff(Time)
Diff_volt = np.diff(Voltage)
plt.plot(Diff_volt)
plt.title('Differential signal for ' + database_name)
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.show()

"""
Step 4: Square the results of the previous step
"""
Square_time = np.square(Diff_time)
Square_volt = np.square(Diff_volt)
plt.plot(Square_volt)
plt.title('Squared signal for ' + database_name)
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.show()

"""
Step 5: Pass a moving filter over your data
"""
ones = np.ones(5)
MovAverage_time = np.convolve(Square_time,ones)
MovAverage_volt = np.convolve(Square_volt,ones)
plt.plot(MovAverage_volt)
plt.title('Moving average signal for ' + database_name)
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.show()

## YOUR CODE HERE
# make a plot of the results. Can change the plot() parameter below to show different intermediate signals


