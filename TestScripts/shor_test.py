import math
import numpy as np
import time

import qiskit
from qiskit import Aer, IBMQ, execute
from qiskit.providers.aer.noise import NoiseModel
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import BasicAer
from qiskit.aqua import QuantumInstance
from qiskit.aqua.algorithms import Shor

def shor_ideal(N):
    shor = Shor(N)
    backend = Aer.get_backend("qasm_simulator")
    quantum_instance = QuantumInstance(backend, shots=1024)

    start = time.time()
    result = shor.run(quantum_instance)
    end = time.time()

    print(f"Elapsed: {end - start} seconds")

    circ = shor.construct_circuit(False)

    ops = circ.count_ops() # This thing over here is super important! Will use it as a metric

    print(ops)

    print(result['factors'][0])


def shor_noisy(N):
    provider = IBMQ.load_account()

    device = provider.get_backend('ibmq_16_melbourne')
    noise_model = NoiseModel.from_backend(device)
    shor = Shor(N)
    backend = Aer.get_backend("qasm_simulator")
    quantum_instance = QuantumInstance(backend, shots=1024, noise_model=noise_model)

    properties = device.properties()
    coupling_map = device.configuration().coupling_map

    start = time.time()
    result = shor.run(quantum_instance)
    end = time.time()

    print(f"Elapsed: {end - start} seconds")
    circ = shor.construct_circuit(False)
    ops = circ.count_ops() # This thing over here is super important! Will use it as a metric

    print(ops)

    print(result['factors'][0])

IBMQ.save_account("983977d6aef3832d4541ec1e9503cb4b9f93c811f3d61febe63db7f82276ee6a9887bc920bba11bcd838d04987bc8fac47c8cec22591a86eee11c16240f687b6")

print("running ideal tests")

print("factoring 9")
shor_ideal(9)
print("factoring 15")
shor_ideal(15)
print("factoring 21")
shor_ideal(21)
print("factoring 27")
shor_ideal(27)


print("running noisy tests")

print("factoring 9")
shor_noisy(9)
print("factoring 15")
shor_noisy(15)
print("factoring 21")
shor_noisy(21)
print("factoring 27")
shor_noisy(27)

