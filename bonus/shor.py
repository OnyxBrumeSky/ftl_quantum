from qiskit import QuantumCircuit
from qiskit.primitives import BackendSamplerV2
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel 
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
import sys
from qiskit.visualization import plot_histogram

#M2
# here we describe the action M2|1> = |2> ... M2|8> = |1>
# basicly a Qbit shifting
M2 = QuantumCircuit(4)
M2.swap(2,3)
M2.swap(1,2)
M2.swap(0,1)
M2.to_gate()
M2.name = f"M_2"
M2_control = M2.control()
display(M2.decompose().draw("mpl"))
#display(M2.draw("mpl"))


#M4
# here we describe the action M4|1> = |4> and M4|4> = |1>
# basicly a Qbit shifting by 2
M4 = QuantumCircuit(4)
M4.swap(1,3)
M4.swap(0,2)
M4.to_gate()
M4.name = f"M_4"
M4_control = M4.control()
display(M4.decompose().draw("mpl"))
#display(M4.draw("mpl"))


N = 15
a = 2

Qbit_nb = floor(


circuit = QuantumCircuit(5)
circuit.compose(M4_control, inplace=True)
display(circuit.decompose().draw("mpl"))


