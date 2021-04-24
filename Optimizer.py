import qiskit
from qiskit.dagcircuit import DAGCircuit
from qiskit.transpiler.passes import CommutativeCancellation
from Scheduler.DagHandler import dag_to_list, hash_adj_list, chop_subdag
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.converters import circuit_to_dag
from Utils import put_subdags_into_csv, hash_training_data
from Scheduler.Scheduler import AdaptiveScheduler
from qiskit.transpiler import PassManager

#ser_circ = serialize_circuit(dag)
#print(ser_circ)
#print(dag)

#circuit.qasm(False, "Test_Qasm.qasm")

qcc = qiskit.QuantumCircuit.from_qasm_file("Test_Qasm.qasm")

asc = AdaptiveScheduler()
pm = PassManager()
pm.append(CommutativeCancellation())
qcco = pm.run(qcc)
#asc.pass_manager.append(CommutativeCancellation)
#qcco = asc.run_optimization(qcc)

qcco.qasm(False, "Test_qasm_opt1.qasm")

pass