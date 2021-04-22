#import qiskit
#import csv
#import os

def generate_commutative_cancellations(training_data_file: str):
    dictionary = ['x', 'h', 'i', 'rx(pi)']
    qubits = [1, 2, 3]
    file = open(training_data_file, "a")
    for i in range(1, 3):
        # Picking 'irrelevant' qubit
        irrel_qubit = i

        # Set commutative qubits
        qubits_without_irrelevant = set(qubits) - set([irrel_qubit])
        data = [None] * 3
        for q in dictionary:
            for k in range(len(qubits_without_irrelevant)):
                for qwi in qubits_without_irrelevant:
                    data[qwi-1] = q + '_' + 'q' + str(list(qubits_without_irrelevant)[k])
            for w in dictionary:
                data[irrel_qubit-1] = w + '_' + 'q' + str(irrel_qubit)
                data_str = ""
                for j in range(3):
                    data_str += data[j]
                    if j != 2:
                        data_str += ','
                data_str += ',' + str(1)
                file.write(data_str + "\n")
    file.close()

def generate_no_opts():
    pass

def generate_cx_cancellations():
    pass

generate_commutative_cancellations("commut_canc_train.csv")
generate_no_opts("no_opt_train.csv")