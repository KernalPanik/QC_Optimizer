# Adaptive Quantum Circuit Optimizer

## Structure

This project is split into two different Modules: Scheduler and Learner. Scheduler is a Qiskit package responsible for DAG parsing, optimization pass scheduling, and actual circuit optimization run. Learner is responsible for analysing QC DAG adjacency lists and determining possible optimizations.

Two different environments with different requirements must be created for these modules. All package requirements can be found in requirements.txt files.

Learner should be working on Mac M1 chips, while Scheduler can be run on a Mac M1 via Rosetta2 only, since Scipy fails to install when running qiskit on M1 natively.

### Virtual environments
Qiskit: conda activate qiskit_venv
TF: . "/Users/lukemichniewicz/tensorflow_macos_venv/bin/activate" 



