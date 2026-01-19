from qiskit.quantum_info import Statevector
from numpy import sqrt
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

u = Statevector([1 / sqrt(2), 1 / sqrt(2)]); #Initialisation of colomn vector. Note that it can be written as 1/sqrt(2)(|0⟩ + |1⟩) in mathematical notation.
display(u.draw("latex")); #print the equation in the mathematical way


statistics = u.sample_counts(500); #run simulation 500 times
for key in statistics:
    statistics[key] = float(statistics[key]) / 500  # Normalizing the data

plot_histogram(statistics) #plot the results
plt.show()



