import random
import math
import csv


def nextTime(mean):
    return -mean * math.log(1 - random.random())


def theoreticalMeanQueueLength(alpha, beta):
    #If either of these are true, the program will attempt to divide by 0.
    if beta/alpha == 1 or alpha == 0:
        return -1
    #This will only run if there is no 0 division.
    return (beta/alpha)/(1-(beta/alpha))


def checkMean(mean, iterations=10000):
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
    #initialise all variables
    maxQ = 0
    Q = 1
    c = 0
    tarrival = 0
    tserve = 0
    queueLengths=[1]

    #This acts as the first "is c < time?" if statement in the flowchart.
    while c < time:
        if tarrival < tserve:
            #Code for an arrival
            tserve = tserve - tarrival
            c = c + tarrival
            Q = Q + 1
            queueLengths.append(Q)
            maxQ = max(maxQ, Q)
            tarrival = nextTime(alpha)
        else:
            #Code for a service finishing
            tarrival = tarrival - tserve
            c += tserve
            Q -= 1
            queueLengths.append(Q)
            tserve = nextTime(beta)
        #This loop acts as the "is Q = 0?" if statement at the bottom of the flowchat.
        #if Q is not equal to 0, it returns to the top of the flowchart.
        while Q == 0:
            c = c + tarrival
            Q = Q + 1
            queueLengths.append(Q)
            maxQ = max(maxQ, Q)
            tarrival = nextTime(alpha)

    return maxQ, (sum(queueLengths)/len(queueLengths))


def experiment(alpha, beta, iterations=100000):
    results = []
    maxQueueLengths = []
    averages = []

    #This will run the singleQueue function the amount of times specified by iterations
    #and will return the results to lists
    for i in range(iterations):
        results.append(singleQueue(alpha, beta))
        maxQueueLengths.append(results[i][0])
        averages.append(results[i][1])

    #This block calculates statistics based on the experiment just run.
    shortest = min(maxQueueLengths)
    longest = max(maxQueueLengths)
    lengthRange = longest - shortest
    averageMaxQueueLength = sum(maxQueueLengths)/len(maxQueueLengths)
    averageAverageQueueLength = sum(averages)/len(averages)
    theoreticalLength = theoreticalMeanQueueLength(alpha, beta)

    #This returns a tuple containing the statistics that can be used for analysis.
    return (averageMaxQueueLength,lengthRange,averageAverageQueueLength,theoreticalLength)
