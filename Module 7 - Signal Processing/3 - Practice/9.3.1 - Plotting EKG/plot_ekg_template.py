import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# import the CSV file using numpy
path = '../../../data/ekg/mitdb_201.csv'

# load data in matrix from CSV file; skip first two rows

### Your code here ###
Data = np.loadtxt(path, skiprows = 2, delimiter = ',')
# save each vector as own variable
Time = Data[:, 0]
MLII = Data[:, 1]
Voltage = Data[:, 2]

# use matplot lib to generate a single

plt.plot(Time, Voltage)
plt.title('Voltages vs. Time')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.legend()
plt.show()