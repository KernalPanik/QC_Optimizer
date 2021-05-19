# Adaptive Quantum Circuit Optimizer

## Structure

This project is split into two different Modules: Scheduler and Learner. Scheduler is a Qiskit package responsible for DAG parsing, optimization pass scheduling, and actual circuit optimization run. Learner is responsible for analysing QC DAG adjacency lists and determining possible optimizations.

Learner should be working on Mac M1 chips, while Scheduler can be run on a Mac M1 via Rosetta2 only, since Scipy fails to install when running qiskit on M1 natively. Will make sure it works without any trouble on windows, but will add some workarounds on a Mac M1, unfortunately.

### On Windows and Linux-based systems (x86, x64)
Import the Adaptive_Optimizer class from Optimizer_main.py. Usage example:
```
from Optimizer_main import Adaptive_Optimizer
ao = Adaptive_Optimizer()
ao.run_optimization(<path to circuit qasm file>)
``` 
This code will generate _optimized qasm file.

### On Mac M1
Optimizer can't be easily imported on Mac M1, so to run optimizations, a shell script 
```
Optimizer_m1.sh
```
Needs to be executed.

python3 Optimizer_mac_DagHash.py -> Generate a QC here, it will return a csv file containing hashed dag  
python3 Optimizer_mac_Ml.py <hashed dag path> -> Will generate optimization schedule based on provided hashed dag path, and will return a file containing the optimization names  
python3 Optimizer_mac_final.py <circuit json> <optimizations> -> run optimizations on a circuit, return serialized optimized circuit  

### How training data is being generated
Random circuits are converted into adjacency lists, then these lists are split into 3 element lists and put in a csv file. This file is later analyzed manually, and optimization (0 - no opt; 1 - same opt) is set for each subdag list. Then hashing is used to convert strings into numbers, and these values are used to train ML model.

### Test Scripts
There are several Python test scripts which were used to generate test data, perform additional quantum algorithm tests. Please see TestScripts folder for more info. Provided files contain methods to generate circuit qasm files based on given qubit count. Use these methods to generate qasm file to optimize, and then use AdaptiveOptimizer class to perform optimizations on created files. Sometimes, a circuit can be optimized several times (i.e. performing optimization on already optimized qasm).


