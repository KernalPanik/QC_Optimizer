import qiskit
import math
import numpy as np
from numpy import pi
from qiskit import Aer
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.aqua.algorithms import Shor, Grover, VQE
from qiskit.compiler import transpile
from qiskit.aqua.components.oracles import LogicalExpressionOracle, TruthTableOracle
from qiskit.circuit.random import random_circuit

def transpile_into_basis(circ: QuantumCircuit, output_filename: str):
    rcirc = transpile(circ, basis_gates=['cx', 'u1', 'u2', 'u3'], optimization_level=1)

    circ_ops = circ.count_ops()
    circ_op_count = 0
    for op in circ_ops:
        circ_op_count += circ_ops[op]

    rcirc_ops = rcirc.count_ops()
    rcirc_op_count = 0
    for op in rcirc_ops:
        rcirc_op_count += rcirc_ops[op]

    print(output_filename + " op count before transpile: " + str(circ_op_count))
    print(output_filename + " op count after transpile: " + str(rcirc_op_count))

    with open(output_filename, 'a') as f:
        f.write(rcirc.qasm())

def random_gen(N):
    """N is for qubit count"""
    circ = random_circuit(N, N*N, 2, False, False, False, None)

    circ_ops = circ.count_ops()
    circ_op_count = 0
    for op in circ_ops:
        circ_op_count += circ_ops[op]

    print("random_" + str(N) + "_qubit.qasm" + " op count before transpile: " + str(circ_op_count))
    print("random_" + str(N) + "_qubit.qasm" + " op count after transpile: " + str(circ_op_count))
    #rcirc = transpile(circ, basis_gates=['cx', 'u1', 'u2', 'u3'], optimization_level=1)
    with open("random_" + str(N) + "_qubit.qasm", 'a') as f:
        f.write(circ.qasm())
#    transpile_into_basis(circ, "random_" + str(N) + "_qubit.qasm")

def shor_algo_gen(N: int):
    shor = Shor(N)
    circ = shor.construct_circuit(False)
    transpile_into_basis(circ, 'transpiled_shor_'+str(N)+'.qasm')

def swap_registers(circuit, n):
    for qubit in range(n//2):
        circuit.swap(qubit, n-qubit-1)
    return circuit

def qft_rotations(circuit, n):
    """Performs qft on the first n qubits in circuit (without swaps)"""
    if n == 0:
        return circuit
    n -= 1
    circuit.h(n)
    for qubit in range(n):
        circuit.cp(pi/2**(n-qubit), qubit, n)
    # At the end of our function, we call the same function again on
    # the next qubits (we reduced n by one earlier in the function)
    qft_rotations(circuit, n)


def qft(circuit, n):
    """QFT on the first n qubits in circuit"""
    qft_rotations(circuit, n)
    swap_registers(circuit, n)
    return circuit

def qft_algo_gen(N):
    circ = QuantumCircuit(N)
    qft(circ, N)
    transpile_into_basis(circ, 'transpiled_QFT_'+str(N)+'.qasm')

def qft_dagger(qc, n):
    """n-qubit QFTdagger the first n qubits in circ"""
    # Don't forget the Swaps!
    for qubit in range(n//2):
        qc.swap(qubit, n-qubit-1)
    for j in range(n):
        for m in range(j):
            qc.cp(-math.pi/float(2**(j-m)), m, j)
        qc.h(j)

def qpe_algo_gen(N):
    # Create and set up circuit
    qpe3 = QuantumCircuit(N, N-1)

    # Apply H-Gates to counting qubits:
    for qubit in range(N-1):
        qpe3.h(qubit)

    # Prepare our eigenstate |psi>:
    qpe3.x(N-1)

    # Do the controlled-U operations:
    angle = 2*math.pi/3
    repetitions = 1
    for counting_qubit in range(N-1):
        for i in range(repetitions):
            qpe3.cp(angle, counting_qubit, N-1);
        repetitions *= 2

    # Do the inverse QFT:
    qft_dagger(qpe3, N-1)

    # Measure of course!
    qpe3.barrier()
    for n in range(N-1):
        qpe3.measure(n,n)

    transpile_into_basis(qpe3, 'transpiled_QPE_'+str(N)+'.qasm')

random_gen(4)
random_gen(6)
random_gen(8)
random_gen(10)
random_gen(12)
random_gen(14)
random_gen(16)

shor_algo_gen(9)
shor_algo_gen(15)
shor_algo_gen(21)
shor_algo_gen(35)

qft_algo_gen(4)
qft_algo_gen(8)
qft_algo_gen(12)
qft_algo_gen(16)

qpe_algo_gen(4)
qpe_algo_gen(8)
qpe_algo_gen(12)
qpe_algo_gen(16)
