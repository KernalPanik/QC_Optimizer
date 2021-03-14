from qiskit.dagcircuit import DAGCircuit
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.converters import circuit_to_dag

'''
This Module provides all neccessary functionality for DAGCircuit parsing, comparing and divinding.
'''
def dag_to_list(dag: DAGCircuit):
    '''
    A function that returns adjacency list of a dag
    '''
    adj_list = list()
    for node in dag.op_nodes():
        entry = node.name + '_'
        for qarg in node.qargs:
            entry += 'q' + str(qarg.index) + '_'
        
        for carg in node.cargs:
            entry += 'c' + str(carg.index) + '_'
        adj_list.append(entry)

    return adj_list

def hash_adj_list(adj_list: list) -> list:
    '''
    Hashes the entries in the adjacency list.
    '''
    # Some thoughts on hashing... First of all.. Why?
    # To make string comparisons faster? I don't know if regular string comparison is fast enough
    # I could compute CRC32 for string hashes, but is it needed though?
    # I need to get some testing data beforehand first...
    raise NotImplementedError

def _parse_adj_list_entry(entry: str) ->  dict:
    split_string = entry.split('_')
    entry_dict = dict()
    entry_dict["op"] = split_string[0]
    if(split_string[1] != ''):
        entry_dict["arg1"] = split_string[1]
    if(split_string[2] != ''):
        entry_dict["arg2"] = split_string[2]

    return entry_dict


def check_if_interchangeable(n1, n2) -> bool:
    '''
    Returns true if both nodes n1 and n2 can be swapped without changing the logic of
    the Quantum Algorithm
    '''
    # Known interchanges
    # xq xq; hq hq, cx01 cx01; [x0; h0, Rz0] cx_0
    if(n1 == n2):
        return True

    d1 = _parse_adj_list_entry(n1)
    d2 = _parse_adj_list_entry(n2)

    got_h = False
    if(d1["op"] == 'h' or d2["op"] == 'h'):
        got_h = True

    if(got_h and d1["arg1"] == d2["arg1"]):
        return False

    if(d1["op"] != d2["op"] and d1["arg1"] == d2["arg1"]):
        return False

    got_two_cx = False
    if(d1["op"] == 'cx' and d2["op"] == 'cx'):
        got_two_cx = True

    if(got_two_cx and d1["arg1"] == d2["arg2"]):
        return False

    return True

def divide_into_subdags(adj_list: list):
    '''
    Returns an array of lists - sub-dags of a dag
    '''
    x = 0
    y = 1
    skip_one = False
    subdag_list = list()
    current_subdag = list()
    for i in range(0, len(adj_list), 1):
        if(skip_one):
            skip_one = False
            continue
        if(y+i > len(adj_list)-1):
            current_subdag.append(adj_list[x+i])
            break
        print(x+i, y+i)
        print('<' + adj_list[x+i] + ';' + adj_list[y+i] + '>')
        interchangeable = check_if_interchangeable(adj_list[x+i], adj_list[y+i])
        print("Interchangeable:", str(interchangeable))
        if(check_if_interchangeable(adj_list[x+i], adj_list[y+i])):
            current_subdag.append(adj_list[x+i])
            #current_subdag.append(adj_list[y+i])
        else:
            current_subdag.append(adj_list[x+i])
            current_subdag.append(adj_list[y+i])
            subdag_list.append(current_subdag)
            current_subdag = list()
            skip_one = True
            #current_subdag.append(adj_list[y+i])
    if(len(current_subdag) > 0):
        subdag_list.append(current_subdag)
    
    return subdag_list
        
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

op1 = 'h_q0_'
op2 = 'cx_q0_q1'
op3 = 'cx_q1_q0'
op4 = 'h_q0_'
op5 = 'x_q0_'

print(check_if_interchangeable(op1, op2))
print(check_if_interchangeable(op1, op3))
print(check_if_interchangeable(op1, op4))
print(check_if_interchangeable(op1, op5))
print(check_if_interchangeable(op2, op3))
print(check_if_interchangeable(op3, op2))
print(check_if_interchangeable(op4, op5))
print(check_if_interchangeable(op2, op1))

# Sub-dag gen test
q1 = QuantumRegister(2, 'q')
c1 = ClassicalRegister(2, 'c')
circ1 = QuantumCircuit(q1, c1)
circ1.x(q1[0])
circ1.x(q1[0])
circ1.cx(q1[0], q1[1])
circ1.cx(q1[1], q1[0])
circ1.x(q1[0])
circ1.cx(q1[0], q1[1])
circ1.x(q1[1])
circ1.x(q1[1])

print(circ1)
dag1 = circuit_to_dag(circ1)
listx1 = dag_to_list(dag1)

print(listx1)

subdags = divide_into_subdags(listx1)

print(subdags)
