from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram
from qiskit import QuantumCircuit

circuit = QuantumCircuit(1);
circuit.h(0);

ket0 = Statevector([1, 0]);
v = ket0.evolve(circuit);

display(v.draw("latex"));
display(circuit.draw(output="mpl"));

sample = 500;

statistics = v.sample_counts(sample);

for key in statistics:
    statistics[key] = float(statistics[key]) / sample  # Normalizing the data
    
display(plot_histogram(statistics));
