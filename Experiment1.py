import SimulationModified as sim

alpha = int(input("Input alpha value for mean arrival time: "))
beta = int(input("Input beta value for mean service time: "))
iterations = int(input("Input the number of times to run the simulation: "))

results = sim.experiment(alpha, beta, iterations)

print("")
print("The average maximum length the queue reached was: "+str(results[0]))
print("The range of maximum queue lengths was: "+str(results[1]))
print("The average of the average queue lengths was: "+str(results[2]))
