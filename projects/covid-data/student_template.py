import sys

from numpy.ma.core import argmax


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date, county, state, cases, deaths) information
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date, county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data

def first_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    :return:
    """
    Rockingham = []
    Harrisonburg = []
    Virginia = []

    ## This for loop makes a list of every Virginia Entry
    for i in range(0, len(data)):
        if 'Virginia' in data[i]:
            Virginia.append(data[i])
        else:
            i += i

    ## This for loop makes a list of every rockingham entry
    for i in range(0, len(Virginia)):
        if 'Rockingham' in Virginia[i]:
            Rockingham.append(Virginia[i])
        else:
            i += i

    ## This for loop makes a list of every harrisonburg entry
    for i in range(0, len(Virginia)):
        if 'Harrisonburg city' in Virginia[i]:
            Harrisonburg.append(Virginia[i])
        else:
            i += i

    #display the lists
   ## print(Rockingham)
   ## print(Harrisonburg)

    # the lists are already ordered chronologically so pulling the first entry
    Rockingham_start = Rockingham[0]
    Harrisonburg_start = Harrisonburg[0]

    # pulling the date from the entry
    Firstcase_R = Rockingham_start[0]
    Firstcase_H = Harrisonburg_start[0]

    print("The first cases for Rockingham and Harrisonburg occurred on " + Firstcase_R, "and", Firstcase_H,
          "respectively")
    return Firstcase_R, Firstcase_H

def second_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    :return:
    """
    Rockingham = []
    Harrisonburg = []
    Virginia = []

    ## This for loop makes a list of every Virginia Entry
    for i in range(0, len(data)):
        if 'Virginia' in data[i]:
            Virginia.append(data[i])
        else:
            i += i

    ## This for loop makes a list of every rockingham entry
    for i in range(0, len(Virginia)):
        if 'Rockingham' in Virginia[i]:
            Rockingham.append(Virginia[i])
        else:
            i += i

    ## This for loop makes a list of every harrisonburg entry
    for i in range(0, len(Virginia)):
        if 'Harrisonburg city' in Virginia[i]:
            Harrisonburg.append(Virginia[i])
        else:
            i += i

    ## Create a list of just the new cases for Rockingham
    NewCasesR = []
    for i in range(0, len(Rockingham)):
        EachEntryR = Rockingham[i]
        NewCasesR.append(EachEntryR[3])

    ## Create a list of just the new cases for Harrisonburg
    NewCasesH = []
    for i in range(0, len(Harrisonburg)):
        EachEntryH = Harrisonburg[i]
        NewCasesH.append(EachEntryH[3])

    # find the greatest valued cases index for rockingham
    Cum_New_cases_R = []                                    # create a list to track NonCum values
    for i in range(0, len(NewCasesR)):
        if i == 0:                                          # skip the first index
            Cum_New_cases_R.append(NewCasesR[0])
        else:
            NewCases_numerical = NewCasesR[i] - NewCasesR[i - 1]
            Cum_New_cases_R.append(NewCases_numerical)
    Greatest_IndexR = argmax(Cum_New_cases_R)               # index for the greatest number of new cases


    Cum_New_cases_H = []                                    # create a list to track NonCum values
    for i in range(0, len(NewCasesH)):
        if i == 0:                                          # skip the first index
            Cum_New_cases_H.append(NewCasesH[0])
        else:
            NewCases_numerical2 = NewCasesH[i] - NewCasesH[i - 1]
            Cum_New_cases_H.append(NewCases_numerical2)
    Greatest_IndexH = argmax(Cum_New_cases_H)               # index for the greatest number of new cases


    #Get the values of the Lists these cases occured
    GreatestTuple_R = Rockingham[Greatest_IndexR]
    GreatestTuple_H = Harrisonburg[Greatest_IndexH]

    #Get the dates from these lists
    GreatestDATE_R = GreatestTuple_R[0]
    GreatestDATE_H = GreatestTuple_H[0]

    print("The highest number of new cases for Rockingham and Harrisonburg occured on " + GreatestDATE_R, "and",
          GreatestDATE_H + " respectively")

    return GreatestDATE_R, GreatestDATE_H

def third_question(data):
    # Write code to address the following question:Use print() to display your responses.
    # What was the worst 7-day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    Rockingham = []
    Harrisonburg = []
    Virginia = []

    ## This for loop makes a list of every Virginia Entry
    for i in range(0, len(data)):
        if 'Virginia' in data[i]:
            Virginia.append(data[i])
        else:
            i += i

    ## This for loop makes a list of every rockingham entry
    for i in range(0, len(Virginia)):
        if 'Rockingham' in Virginia[i]:
            Rockingham.append(Virginia[i])
        else:
            i += i

    ## This for loop makes a list of every harrisonburg entry
    for i in range(0, len(Virginia)):
        if 'Harrisonburg city' in Virginia[i]:
            Harrisonburg.append(Virginia[i])
        else:
            i += i

    ## Create a list of just the new cases for Rockingham
    NewCasesR = []
    for i in range(0, len(Rockingham)):
        EachEntryR = Rockingham[i]
        NewCasesR.append(EachEntryR[3])

    ## Create a list of just the new cases for Harrisonburg
    NewCasesH = []
    for i in range(0, len(Harrisonburg)):
        EachEntryH = Harrisonburg[i]
        NewCasesH.append(EachEntryH[3])

    # find the single dayed  cases index for rockingham
    Cum_New_cases_R = []                                    # create a list to track NonCum values
    for i in range(0, len(NewCasesR)):
        if i == 0:                                          # skip the first index
            Cum_New_cases_R.append(NewCasesR[0])
        else:
            NewCases_numerical = NewCasesR[i] - NewCasesR[i - 1]
            Cum_New_cases_R.append(NewCases_numerical)

    #Create a vector for weekly total the index of WeekR corrisponds to the start of every 7-day period
    # so @WeekR[5] the total will be the cum from 5 to 12
    WeekR = []
    for i in range(0,len(Cum_New_cases_R) - 6):                 #create new list of 7-day intervals
        WeekCumR = (Cum_New_cases_R[i] + Cum_New_cases_R[i + 1] + Cum_New_cases_R[i + 2] + Cum_New_cases_R[i + 3]
                  + Cum_New_cases_R[i + 4] + Cum_New_cases_R[i + 5] + Cum_New_cases_R[i + 6])
        WeekR.append(WeekCumR)
    GreatestWeekR = argmax(WeekR)

# find the single dayed  cases index for Harrisonburg
    Cum_New_cases_H = []                                    # create a list to track NonCum values
    for i in range(0, len(NewCasesH)):
        if i == 0:                                          # skip the first index
            Cum_New_cases_H.append(NewCasesH[0])
        else:
            NewCases_numerical2 = NewCasesH[i] - NewCasesH[i - 1]
            Cum_New_cases_H.append(NewCases_numerical2)

    # Create a vector for weekly total the index of WeekH corrisponds to the start of every 7-day period
    # so @WeekH[5] the total will be the cum from 5 to 12
    WeekH = []
    for i in range(0, len(Cum_New_cases_H) - 6):               # create new list of 7-day intervals
        WeekCumH = (Cum_New_cases_H[i] + Cum_New_cases_H[i + 1] + Cum_New_cases_H[i + 2] + Cum_New_cases_H[i + 3]
                    + Cum_New_cases_H[i + 4] + Cum_New_cases_H[i + 5] + Cum_New_cases_H[i + 6])
        WeekH.append(WeekCumH)
    GreatestWeekH = argmax(WeekH)

    #Getting the tuples from the start and end of the greatest period
    GreatestTuple_R1 = Rockingham[GreatestWeekR]
    GreatestTuple_R2 = Rockingham[GreatestWeekR + 6]
    GreatestTuple_H1 = Harrisonburg[GreatestWeekH]
    GreatestTuple_H2 = Harrisonburg[GreatestWeekH + 6]

    # Get the dates from these lists
    GreatestWeek_R = GreatestTuple_R1[0] + " to " + GreatestTuple_R2[0]
    GreatestWeek_H = GreatestTuple_H1[0] + " to " + GreatestTuple_H2[0]

    print("The greatest weeks for Rockingham and Harrisonburg are " + GreatestWeek_R, "and", GreatestWeek_H +
          " respectively")

    return GreatestWeek_R, GreatestWeek_H

if __name__ == "__main__":
    data = parse_nyt_data('us-counties.csv')

    ##for (date, county, state, cases, deaths) in data:
        ##print('On ', date, ' in ', county, ' ', state, ' there were ', cases, ' cases and ', deaths, ' deaths')


    # write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    first_question(data)


    # write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    second_question(data)

    # write code to address the following question:Use print() to display your responses.
    # What was the worst seven day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    third_question(data)


