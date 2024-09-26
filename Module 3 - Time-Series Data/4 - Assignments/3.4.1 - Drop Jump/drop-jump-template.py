import numpy as np
from os import path
import scipy.constants as constants


def main(full_path_to_file):
    """
    Given a file containing force plate drop jump data, find the first/second landings and take off point

    :param full_path_to_file: A file path to a text file
    :return: signal, first_landing_index, take_off_index, second_landing_index, RSI:
    signal: The signal data from the force plate file
    first_landing_index: Index within the signal of the first landing point
    take_off_index: Index within the signal of the take-off point
    second_landing_index: Index within the signal of the first landing point
    RSI: Calculated reactive strength index
    """


    # perform a basic check to see if the file exists. If not, exit the program
    if not path.exists(full_path_to_file):
        print("File does not exist", full_path_to_file)

    # load the data from the file
    data = np.loadtxt(full_path_to_file, delimiter=",")

    # select the 8th column as the force plate data
    force_plate = data[:, 8]

    # save the sampling rate for this data (samples/second)
    sampling_rate = 1000

    # Step 1: Establish a baseline by examining the force data the after for first ~20 points

    # set an amount of time to average and find the baseline
    baseline_length = 1 ### your code here ###

    # over the baseline, determine the average signal value
    ### your code here ###
    baseline = np.average(force_plate[0:baseline_length])

    # Step 2: After the baseline, find the first point that rises above that value
    # given some acceptable delta
    force_plate_list = force_plate.tolist()
    # when the signal exceeds the baseline plus delta, that is the landing point
    delta = 5
    first_landing_index = -1

    for i in range(baseline_length, len(force_plate_list)):
        if force_plate_list[i] > baseline + delta:
            first_landing_index = i
            break


    # make a variable to hold the INDEX of that landing point. We will later convert that
    # index to time based upon the force plate sample rate

    # Step 3: When force measurements return to the initial baseline the user has left the plate.
    # Consider this the take off point.
    take_off_index = -1

    for i in range(first_landing_index + 10, len(force_plate_list)):
        if force_plate_list[i] < baseline + delta:
            take_off_index = i
            break
    # when the signal falls below the baseline plus delta, that is the take off point

    second_landing_index = -1

    for i in range(take_off_index + 10, len(force_plate_list)):
        if force_plate_list[i] > baseline + delta:
            second_landing_index = i
            break


    # Step 5: calculate the time of contact on plate and time of flight in air

    # calculate tc and convert to seconds using the sampling rate
    time_of_contact = (take_off_index - first_landing_index) / 1000 ### your code here ###

    # calculate tf and convert to seconds using the sampling rate
    time_of_flight = (second_landing_index - take_off_index) / 1000 ### your code here ###

    # Step 6: Calculate the Reactive Strength Index

    # pull the local gravitational acceleration from scipy
    g = constants.g

    # RSI = (g*tf^2) / (8*tc)
    RSI = (g * (time_of_flight**2)) / (8 * time_of_contact) ### your code here ###

    ### Do not modify below this line ###

    # normalize the force plate data so that it will plot correctly when complete
    signal = force_plate - baseline

    return signal, first_landing_index, take_off_index, second_landing_index, RSI


if __name__ == "__main__":
    # need to import this here so it won't eventually affect the autograder
    import matplotlib.pyplot as plt

    # change this file name to load other datasets
    filename = "FP3.txt"

    # load force plate data (this path may change based upon where you place this file in your project)
    path_to_data_folder = "../../../data/drop-jump/force-plate/"

    ### Do not modify below this line ###

    # put together directory and file to make a single relative path
    full_path_to_file = path_to_data_folder + filename

    # call the student function to return the signal and jump/landing indices
    (signal, first_landing_index, take_off_index, second_landing_index, RSI) = main(full_path_to_file)

    # print out some debug information
    print("First landing: ", first_landing_index)
    print("Take off: ", take_off_index)
    print("Second landing: ", second_landing_index)
    print("Calculated RSI: ", RSI)

    # plot the data with matplotlib
    # make a nice plt of results
    plt.title('RSI Force Plate Data for Trial ' + filename)

    # plot the signal itself
    plt.plot(signal, label="Force Plate Data")

    # plot the various landing points
    plt.plot(first_landing_index, signal[first_landing_index], 'v', label="First Landing")
    plt.plot(take_off_index, signal[take_off_index], 'v', label="Jump / Take-Off")
    plt.plot(second_landing_index, signal[second_landing_index], 'v', label="Second Landing")

    # show the legend
    plt.legend()

    # uncomment line to show the plot
    plt.show()
