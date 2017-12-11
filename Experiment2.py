import matplotlib.pyplot as plt
import SimulationModified as sim
import time

alpha = int(input("Input alpha value for mean arrival time: "))
beta = int(input("Input beta value for initial mean service time: "))
iterations = int(input("Input the number of times to run each simulation: "))

#This creates the list of values that will be used to reduce beta.
reduction = list(range(100, 0, -5))
for i in range(len(reduction)):
    reduction[i] = reduction[i]/100


#These are empty lists for the statistics to go into.
maxLengths = []
averageLengths = []
theoreticalLengths = []


start = time.time()
#This will run every simulation and compile the statistics into lists
for i in reduction:
    results = sim.experiment(alpha, beta*i, iterations)
    maxLengths.append(results[0])
    averageLengths.append(results[2])
    theoreticalLengths.append(results[3])

end = time.time()
print(end - start)
#This creates a list of labels that can be used in the graph.
reductionLabels = list(range(0,100,5))

#This sets up the graphing environment.
fig = plt.figure()
ax = fig.add_subplot(111)

#This adds the lines to the graph using the gathered statistics and the values for percentage reduction.
ax.plot(reductionLabels, maxLengths, 'r-', label="Average Maximum Lengths")
ax.plot(reductionLabels, averageLengths, 'b-', label="Average of Average Lengths")
ax.plot(reductionLabels, theoreticalLengths, 'g-', label="Theoretical average lengths")
#This adds the legend
ax.legend(loc='upper left')
#This adds titles and axis labels.
plt.title("Queue length when average service time is reduced.")
plt.xlabel("Percentage Reduction of Beta Value.")
plt.ylabel("Queue Length.")
plt.show()
