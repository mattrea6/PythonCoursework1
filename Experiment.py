import matplotlib.pyplot as plt
import Simulation as sim

#These commands set the title and labels for the graph.
plt.title("Theoretical Mean Queue Length Variation")
plt.ylabel("Theoretical Mean Queue Length")
plt.xlabel("Alpha value")

#This creates a list of values for alpha from 1.1 to 10.0
values = []
for i in list(range(11,101)):
    values.append(i/10)

#This creates a list of queue lengthsn using the alpha values.
#This uses the function in the Simulation file.
meanValues = []
for i in values:
    meanValues.append(sim.theoreticalMeanQueueLength(i,1))

#This plots and then shows the graph.
#The values for alpha are used on the x-axis
#The values obtained from passing alpha into the mean length function are used for the y-axis.
plt.plot(values, meanValues)
plt.show()
