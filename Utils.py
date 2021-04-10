import csv
from qiskit import Aer, execute
from Scheduler.DagHandler import hash_adj_list
import qiskit

def compare_qasm_execs(qasm_file_1, qasm_file_2) -> bool:
    simulator = Aer.get_backend('qasm_simulator')
    qc1 = qiskit.QuantumCircuit.from_qasm_file(qasm_file_1)
    qc2 = qiskit.QuantumCircuit.from_qasm_file(qasm_file_2)
    
    job1 = execute(qc1, simulator, shots=1000)
    result1 = job1.result()

    job2 = execute(qc2, simulator, shots=1000)
    result2 = job2.result()

    return result1.get_counts(qc1) == result2.get_counts(qc2)

def put_subdags_into_csv(csv_path: str, subdags: list):
    with open(csv_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for subdag in subdags:
            if(len(subdag) < 3):
                for i in range(3 - len(subdag)):
                    subdag.append("i_q0")
            writer.writerow(subdag)

def hash_training_data(training_data_path: str, hashed_data_path: str, col_count = 4) -> str:
    with open(training_data_path, newline='') as entry:
        with open(hashed_data_path, 'w', newline='') as output:
            writer = csv.writer(output, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            reader = csv.reader(entry)

            for row in reader:
                hashed_row = hash_adj_list(row[0:3])

                if(col_count == 4):
                    hashed_row.append(row[-1])
                writer.writerow(hashed_row)