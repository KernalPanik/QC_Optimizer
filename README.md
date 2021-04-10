# Adaptive Quantum Circuit Optimizer

## Structure

This project is split into two different Modules: Scheduler and Learner. Scheduler is a Qiskit package responsible for DAG parsing, optimization pass scheduling, and actual circuit optimization run. Learner is responsible for analysing QC DAG adjacency lists and determining possible optimizations.

Learner should be working on Mac M1 chips, while Scheduler can be run on a Mac M1 via Rosetta2 only, since Scipy fails to install when running qiskit on M1 natively. Will make sure it works without any trouble on windows, but will add some workarounds on a Mac M1, unfortunately.

Use QASM files as an input, Optimizer will take path to qasm as a first arg

### On Windows
python3 Optimizer_win.py  <qasm file> -> Generate a QC there, and call optimizer pipeline, return serialized optimized circuit  

### On Mac M1
Instead of running an optimizer, run a special shell script TODO:  
sh Optimizer_m1.sh <qasm file>

python3 Optimizer_mac_DagHash.py -> Generate a QC here, it will return a csv file containing hashed dag  
python3 Optimizer_mac_Ml.py <hashed dag path> -> Will generate optimization schedule based on provided hashed dag path, and will return a file containing the optimization names  
python3 Optimizer_mac_final.py <circuit json> <optimizations> -> run optimizations on a circuit, return serialized optimized circuit  


### How training data is being generated
Random circuits are converted into adjacency lists, then these lists are split into 3 element lists and put in a csv file. This file is later analyzed manually, and optimization (0 - no opt; 1 - same opt) is set for each subdag list. Then hashing is used to convert strings into numbers, and these values are used to train ML model.

future work or next TODO: Automate this process by creating special helper functions that would allow to create subdags that: {can't be optimized, same optimization, hadamard optimization etc.}



