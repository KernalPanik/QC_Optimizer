import numpy as np
from Utils import hash_training_data

def generate_commutative_cancellations(training_data_file: str, qubit_count: int):
    dictionary = ['x', 'h', 'i', 'rx(pi)'] # You can add more operations to the dictionary
    qubits = np.array([i for i in range(1, qubit_count + 1)]) 
    temp_filename = "training_data_temp.csv"
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
    hash_training_data(temp_filename, training_data_file, 4)

# This function assumes that all sub-graphs are of length 3 only
def generate_no_opts(training_data_file: str):
    dictionary = ['x', 'h', 'i', 'rx(pi)'] # You can add more operations to the dictionary
    qubits = np.array([i for i in range(1, 4)]) 
    temp_filename = "training_data_temp.csv"
    file = open(temp_filename, "a")
    for i in range(1, 4):
        data = [None] * 3
        for w in dictionary:
            for q in set(dictionary) - set([w]):
                for r in set(dictionary) - set([q]) - set([w]):
                    for j in range(3):
                        data[0] = w + '_' + 'q' + str(i)
                        data[1] = q + '_' + 'q' + str(i)
                        data[2] = r + '_' + 'q' + str(i)

                        data_str = ""
                        for k in range(3):
                            data_str += data[k]
                            if k != 2:
                                data_str += ','
                        data_str += ',' + str(0)
                        file.write(data_str + "\n")
    file.close()
    #hash_training_data(temp_filename, training_data_file, 4)

#generate_commutative_cancellations("commut_canc_train.csv", 3)
generate_no_opts("no_opt_train.csv")