#%%
import numpy as np
#import matplotlib.pyplot as plt
from qiskit import(
    QuantumCircuit,
    execute,
    Aer
)
from qiskit.visualization import plot_histogram

simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(2, 2)

circuit.h(0)
circuit.cx(0, 1)
circuit.measure([0, 1], [0, 1]) # pylint: disable=no-member

job = execute(circuit, simulator, shots=1000)
result = job.result()

counts = result.get_counts(circuit)

print(circuit)

plot_histogram(counts)

# %%
