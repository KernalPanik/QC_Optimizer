import qiskit
import sys
import os

from qiskit.dagcircuit import DAGCircuit
from Scheduler.DagHandler import dag_to_list, hash_adj_list, chop_subdag
from qiskit import QuantumCircuit
from qiskit.converters import circuit_to_dag
from Utils import put_subdags_into_csv, hash_training_data

'''
This module parses the given qasm file into QC, converts it into DAG,
returns a temporary csv file containing hashed circuit data to be analyzed
by Learner class 
'''

qasm_file = ""

if(len(sys.argv) < 2):
    print("Qasm file not provided. Exiting")
    sys.exit(1)
else:
    if(os.path.splitext(sys.argv[1])[1] != ".qasm"):
        print("Incorrect file provided, expected .qasm file")
        sys.exit(1)
    qasm_file = sys.argv[1]


circuit = qiskit.QuantumCircuit.from_qasm_file(qasm_file)
dag = circuit_to_dag(circuit)
adj_list = dag_to_list(dag)
chopped_dag = list(chop_subdag(adj_list))
put_subdags_into_csv("temp_eval.csv", chopped_dag)
hash_training_data("temp_eval.csv", "temp_eval_hashed.csv", 3)

sys.exit(0)
