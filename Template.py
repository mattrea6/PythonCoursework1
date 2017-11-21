import random
import math
import csv


def nextTime(mean):
    return -mean * math.log(1 - random.random())


def theoreticalMeanQueueLength(alpha, beta):
    """
    >>> theoreticalMeanQueueLength(10, 2)
    0.25
    >>> theoreticalMeanQueueLength(5, 1)
    0.25
    >>> theoreticalMeanQueueLength(4, 2)
    1.0
    >>> theoreticalMeanQueueLength(5.5, 1.3)
    0.3095238095238095
    >>> theoreticalMeanQueueLength(5.5, 0)
    0.0
    >>> theoreticalMeanQueueLength(1, 1)
    -1
    >>> type(theoreticalMeanQueueLength(10, 2))
    <class 'float'>
    """

    #If either of these are true, the program will attempt to divide by 0.
    if beta/alpha == 1 or alpha == 0:
        return -1
    #This will only run if there is no 0 division.
    return (beta/alpha)/(1-(beta/alpha))


def checkMean(mean, iterations=10000):
    """
    >>> random.seed(57)
    >>> checkMean(5, 10)
    6.309113224728108
    >>> random.seed(57)
    >>> checkMean(5, 1000)
    4.973347344130324
    >>> random.seed(57)
    >>> checkMean(5, 100000)
    4.988076126529703
    >>> random.seed(57)
    >>> checkMean(195, 100000)
    194.53496893466047
    >>> random.seed(57)
    >>> checkMean(195)
    196.71853828860912
    >>> random.seed(57)
    >>> checkMean(31)
    31.273203522804728
    >>> type(checkMean(31, 5))
    <class 'float'>
    """
    #Initialises a list for all of the values returned from nextTime() to go into
    mean_list=[]
    #This will call the nextTime() function however many times it is needed
    for i in range(iterations):
        #Values are added to the list
        mean_list.append(nextTime(mean))
    #finds the average of all of the values returned from nextTime()
    average = sum(mean_list)/len(mean_list)
    return average


def readExperimentParameters(filename):
    """
    >>> readExperimentParameters('experiments.csv')[0]
    (10, 2, 480)
    >>> len(readExperimentParameters('experiments.csv'))
    5
    >>> readExperimentParameters('experiments.csv')[3]
    (20, 2, 480)
    >>> readExperimentParameters('experiments.csv')[2]
    (20, 15, 240)
    >>> type(readExperimentParameters('experiments.csv')[1])
    <class 'tuple'>
    """
    #initialise a list to return
    parameter_list=[]

    #open the .csv and start looking at it
    with open(filename) as csvfile:
        #This skips the header row of the file
        next(csvfile, None)
        for row in csv.reader(csvfile):
            #condition to detect if the time is in hours.
            if str(row[3]) == " h":
                #each element is added to a tuple, with hours multiplied by 60
                to_add = (int(row[0]),int(row[1]),int(row[2])*60)
            else:
                #each element is added to a tuple.
                #Each element needs to be converted into an integer for it to be used
                to_add = (int(row[0]),int(row[1]),int(row[2]))
            #add each new tuple to the list.
            parameter_list.append(to_add)
    return parameter_list


def singleQueue(alpha, beta, time=480):
    """
    >>> random.seed(57)
    >>> singleQueue(10, 3, 480)
    3
    >>> random.seed(101)
    >>> singleQueue(5, 3, 480)
    6
    >>> random.seed(101)
    >>> singleQueue(5, 3)
    6
    >>> random.seed(935)
    >>> singleQueue(10, 9, 280)
    10
    >>> type(singleQueue(10, 9, 280))
    <class 'int'>
    """
    # Add code here
    maxQ = 0
    Q = 1
    c = 0
    tarrival = nextTime(alpha)
    tserve = nextTime(beta)
    while c < time:
        if tarrival < tserve:
            tserve = tserve - tarrival
            c = c + tarrival
            Q += 1
            maxQ = max(maxQ, Q)
            tarrival = nextTime(alpha)
        else:
            tarrival = tarrival - tserve
            c += tserve
            Q -= 1
            tserve = nextTime(beta)
        while True:
            if Q != 0:
                break
            c = c + tarrival
            Q += 1
            maxQ = max(maxQ, Q)
            tarrival = nextTime(alpha)

    return maxQ
