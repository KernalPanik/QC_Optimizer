from qiskit.dagcircuit import DAGCircuit
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.converters import circuit_to_dag

#TODO Implement Dag to adjacency list conversion (both sides)

'''
This Module provides all neccessary functionality for DAGCircuit parsing, comparing and divinding.
'''
class Dag():
    '''
    Main DAG Handling class, which provides all important functionality for sub-DAG generation
    '''
    def __init__(self, dag_circuit: DAGCircuit):
        self.dag_circuit = dag_circuit
        self.size = len(self.dag_circuit.op_nodes())
        self.possible_optimization_type = 0
    
    def divide(self, max_node_count = 3) -> list:
        '''
        Method to divide given dag into smaller sub-dags.
        dag - DAG to parse
        max_node_count - max amount of nodes in a dag. Defaults to 3
        '''
        if(self.size <= max_node_count):
            raise ValueError("Provided dag must be larger than max_node_count") 
            # It this is going to be a recursive function, then this condition would work as a stopper

        return None

def dag_to_list(dag: Dag):
    '''
    A function that gives adjacency list of a dag
    '''
    adj_list = list()
    for node in dag.dag_circuit.op_nodes():
        entry = node.name + '_'
        for qarg in node.qargs:
            entry += 'q' + str(qarg.index) + '.'
        
        for carg in node.cargs:
            entry += 'c' + str(carg.index) + '.'


        print(entry)
        adj_list.append(entry)
    
    return adj_list

def list_to_dag(dag_list: list):
    '''
    A function that gives a DAG from a list
    [Possibly not needed]
    '''
    return None

def check_if_interchangeable(op1, op2) -> bool:
    pass


#Testing, remove when done
q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
circ = QuantumCircuit(q, c)
circ.h(q[0])
circ.cx(q[0], q[1])
circ.measure(q[0], c[0])
circ.rz(0.5, q[1]).c_if(c, 2)

print(circ)

dag = circuit_to_dag(circ)

my_dag = Dag(dag)
dag_to_list(my_dag)
