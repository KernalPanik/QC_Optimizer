#%%
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.dagcircuit import DAGCircuit
from qiskit.converters import circuit_to_dag
from qiskit.converters import dag_to_circuit
from qiskit.transpiler.passes import CommutativeCancellation
from qiskit.tools.visualization import dag_drawer
from qiskit.transpiler import PassManager
from qiskit.compiler import transpile
from qiskit.test.mock import FakeMelbourne
from Adaptive_Scheduler import AdaptiveScheduler

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')

circuit = QuantumCircuit(q, c)
circuit.h(q[0])
circuit.h(q[0])
circuit.h(q[0])
circuit.cx(q[0], q[1])
circuit.measure(q[0], c[0]) # pylint: disable=no-member
circuit.rz(0.5, q[1]).c_if(c, 2)

adaptive_scheduler = AdaptiveScheduler()

commutative_cancellation = CommutativeCancellation()

adaptive_scheduler.PassManager.append(commutative_cancellation)
transformed_circuit = adaptive_scheduler.run_optimization(circuit)

#print(commutative_cancellation.name())
#commutative_cancellation.run(dag)
#circuit = dag_to_circuit(dag)
print(circuit)
print(transformed_circuit)


#circuit.draw(output='mpl')

 # %%
