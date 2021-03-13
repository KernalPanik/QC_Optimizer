from qiskit.dagcircuit import DAGCircuit
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.converters import circuit_to_dag

'''
This Module provides all neccessary functionality for DAGCircuit parsing, comparing and divinding.
'''
def dag_to_list(dag: DAGCircuit):
    '''
    A function that gives sorted adjacency list of a dag
    '''
    adj_list = list()
    for node in dag.op_nodes():
        entry = node.name + '_'
        for qarg in node.qargs:
            entry += 'q' + str(qarg.index) + '.'
        
        for carg in node.cargs:
            entry += 'c' + str(carg.index) + '.'
        adj_list.append(entry)

    return adj_list

def hash_adj_list(adj_list: list) -> list:
    '''
    Hashes the entries in the adjacency list.
    '''
    raise NotImplementedError

def check_if_interchangeable(n1, n2) -> bool:
    '''
    Returns true if both nodes n1 and n2 can be swapped without changing the logic of
    the Quantum Algorithm
    '''
    raise NotImplementedError

def divide_into_subdags(adj_list: list):
    '''
    Returns an array of lists - sub-dags of a dag
    '''
    raise NotImplementedError

def sort_subdag(adj_list: list):
    '''
    Sorts the entries in a sub-dag so all identical operations are grouped.
    '''
    raise NotImplementedError

#Testing, remove when done
q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
circ = QuantumCircuit(q, c)
circ.h(q[0])
circ.cx(q[0], q[1])
circ.h(q[2])
circ.measure(q[0], c[0])
circ.rz(0.5, q[1]).c_if(c, 2)

print(circ)

dag = circuit_to_dag(circ)

listx = dag_to_list(dag)

print(listx)
