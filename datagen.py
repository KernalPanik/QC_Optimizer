import numpy as np
import os
from Utils import hash_training_data
from Scheduler.DagHandler import hash_adj_list

def generate_commutative_cancellations(training_data_file: str, qubit_count: int):
    dictionary = ['x', 'h', 'i', 'rx(pi)'] # You can add more operations to the dictionary
    qubits = np.array([i for i in range(1, qubit_count + 1)]) 
    #temp_filename = "training_data_temp.csv"
    temp_filename = training_data_file
    file = open(temp_filename, "a")
    for i in range(1, qubit_count + 1):
        # Picking 'irrelevant' qubit
        irrel_qubit = i

        # Set commutative qubits
        qubits_without_irrelevant = set(qubits) - set([irrel_qubit])
        data = [None] * qubit_count
        for q in dictionary:
            if(q == "h"):
                continue
            else:
                for k in range(len(qubits_without_irrelevant)):
                    for qwi in qubits_without_irrelevant:
                        data[qwi-1] = q + '_' + 'q' + str(list(qubits_without_irrelevant)[k])
                for w in dictionary:
                    data[irrel_qubit-1] = w + '_' + 'q' + str(irrel_qubit)
                    data_str = ""
                    for j in range(qubit_count):
                        data_str += data[j]
                        if j != 2:
                            data_str += ','
                    data_str += ',' + str(1)
                    file.write(data_str + "\n")
    file.close()
    #hash_training_data(temp_filename, training_data_file, 4)

# This function assumes that all sub-graphs are of length 3 only
def generate_no_opts(training_data_file: str):
    dictionary = ['x', 'h', 'i', 'rx(pi)'] # You can add more operations to the dictionary
    qubits = np.array([i for i in range(1, 4)]) 
    #temp_filename = "training_data_temp.csv"
    temp_filename = training_data_file
    file = open(temp_filename, "a")
    for i in range(1, 4):
        data = [None] * 3
        for w in dictionary:
            for q in set(dictionary) - set([w]):
                for r in set(dictionary) - set([q]) - set([w]):
                    for h in qubits:
                        for g in set(qubits) - set([h]):
                            for l in set(qubits) - set([g]) - set([h]):
                                data[0] = w + '_' + 'q' + str(h-1)
                                data[1] = q + '_' + 'q' + str(g-1)
                                data[2] = r + '_' + 'q' + str(l-1)

                                data_str = ""
                                for k in range(3):
                                    data_str += data[k]
                                    if k != 2:
                                        data_str += ','
                                data_str += ',' + str(0)
                                file.write(data_str + "\n")
    file.close()
    #hash_training_data(temp_filename, training_data_file, 4)

def generate_complete_training_data(training_data_file: str):
    generate_commutative_cancellations("commut.csv", 3)
    generate_no_opts("noopt.csv")

    filenames = ["commut.csv", "noopt.csv"]
    with open(training_data_file, 'w') as outfile:
        for filename in filenames:
            with open(filename) as infile:
                for line in infile:
                    outfile.write(line)
    #os.remove("commut.csv")
    #os.remove("noopt.csv")

generate_complete_training_data("generated_training_data.csv")
hash_training_data("generated_training_data.csv", "hashed_training_data.csv", 4)

#print(hash_adj_list(["h_q2", "x_q0", "i_q1"]))