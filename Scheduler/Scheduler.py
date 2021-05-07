from qiskit.transpiler import PassManager, passes, CouplingMap
from qiskit.providers.aer import QasmSimulator
from qiskit import Aer

def get_optimization_type(opt_id):
    if(opt_id == 1):
        return passes.CommutativeCancellation()
    elif(opt_id == 2):
        return passes.CXCancellation()
    elif(opt_id == 3):
        return passes.Optimize1qGates()
    else:
        return None

class AdaptiveScheduler():
    """
    A Main entry point class.
    Instantiate it and use it's methods to pass custom optimization schedules and
    run Pass Manager passes.
    """
    def __init__(self):
        self.pass_manager = PassManager()

    def run_optimization(self, quantum_circuit):
        """Runs Qiskit Pass Manager"""
        return self.pass_manager.run(quantum_circuit)

    def add_optimization(self, optimization):
        """Add Qiskit optimization pass to the Pass Manager"""
        self.pass_manager.append(optimization)
