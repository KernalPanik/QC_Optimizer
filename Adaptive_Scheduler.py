from qiskit.transpiler import PassManager
from qiskit import QuantumCircuit
from Learner import OptimizationLearner

class AdaptiveScheduler():
    def __init__(self):
        self.PassManager = PassManager()
        self.Learner = OptimizationLearner()
        
    def run_optimization(self, quantum_circuit):
        print("optimizing...")
        return self.PassManager.run(quantum_circuit)



