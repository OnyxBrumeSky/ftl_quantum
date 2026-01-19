from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram
from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator
from numpy import sqrt


circuit = QuantumCircuit(2);
circuit.h(0);
circuit.cx(0,1);

ket00 = Statevector([1, 0, 0, 0]);

v = ket00.evolve(circuit);

display(v.draw("latex"));
display(circuit.draw(output="mpl"));

sample = 500;

statistics = v.sample_counts(sample);

for key in statistics:
    statistics[key] = float(statistics[key]) / sample;
    
display(plot_histogram(statistics));
