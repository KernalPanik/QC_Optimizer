from qiskit.transpiler import PassManager
from qiskit import QuantumCircuit
from Learner import OptimizationLearner

class AdaptiveScheduler():
    def __init__(self):
        self.PassManager = PassManager()
        self.Learner = OptimizationLearner()
        
    def run_optimization(self, circuit: QuantumCircuit(), transpiler_passes: list()) -> QuantumCircuit():
        self.Learner.schedule_optimizations()
        #TODO

    def run_optimization(self, circuit: QuantumCircuit()) -> QuantumCircuit():
        self.Learner.schedule_optimizations()
        return self.PassManager.run(circuit)



