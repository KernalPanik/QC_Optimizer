from qiskit.transpiler import PassManager
from Learner import OptimizationLearner

class AdaptiveScheduler():
    """
    A Main entry point class.
    Instantiate it and use it's methods to pass custom optimization schedules and
    run Pass Manager passes.
    """
    def __init__(self):
        self.pass_manager = PassManager()
        self.learner = OptimizationLearner()

    def run_optimization(self, quantum_circuit):
        """Runs Qiskit Pass Manager"""
        return self.pass_manager.run(quantum_circuit)

    def add_optimization(self, optimization):
        """Add Qiskit optimization pass to the Pass Manager"""
        self.pass_manager.append(optimization)
