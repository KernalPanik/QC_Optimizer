from Optimizer_main import Adaptive_Optimizer

if __name__ == '__main__':
    ao = Adaptive_Optimizer()
    ao.run_optimization("TestScripts/transpiled_hhl_2x2.qasm")
    ao.run_optimization("TestScripts/transpiled_hhl_3x3.qasm")
    ao.run_optimization("TestScripts/transpiled_hhl_4x4.qasm")
