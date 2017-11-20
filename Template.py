import random
import math


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
    # Add code here


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
    # Add code here


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
    # Add code here


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
