#%%
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.transpiler.passes import CommutativeCancellation
from Adaptive_Scheduler import AdaptiveScheduler

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')

circuit = QuantumCircuit(q, c)
circuit.x(q[0])
circuit.h(q[1])
circuit.h(q[0])
circuit.h(q[1])
circuit.x(q[0])
circuit.cx(q[0], q[1])
circuit.measure(q[0], c[0]) # pylint: disable=no-member
circuit.rz(0.5, q[1]).c_if(c, 2)

adaptive_scheduler = AdaptiveScheduler()

commutative_cancellation = CommutativeCancellation()

adaptive_scheduler.pass_manager.append(commutative_cancellation) # pylint: disable=no-member
transformed_circuit = adaptive_scheduler.run_optimization(circuit)

print(circuit)
print(transformed_circuit)


#circuit.draw(output='mpl')

 # %%
