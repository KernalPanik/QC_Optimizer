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
    hadamard_subdags = list()
    for i in range(0, len(adj_list), 1):
        if(skip_one):
            skip_one = False
            continue
        # Check if we are dealing with Hadamard subdags
        if(adj_list[x+i].split('_')[0] == 'h'):
            counter = 0
            closure_found = False
            for hadamard_subdag in hadamard_subdags:
                # If we find same hadamard gate, we've got a complete hadamard subdag, close it,
                # add it to the rest of subdags, and remove from Hadamard subdag list
                if(hadamard_subdag[0] == adj_list[x+i]):
                    hadamard_subdag.append(adj_list[x+i])
                    #subdag_list.append(hadamard_subdag)
                    closure_found = True 
                    #closed_hadamard_subdag_id = counter
                    break
                counter += 1
            if(closure_found is False):
                new_hadamard_subdag = list()
                #new_hadamard_subdag.append(adj_list[x+i])
                hadamard_subdags.append(new_hadamard_subdag)
            else:
                subdag_list.append(hadamard_subdags[counter])
                del(hadamard_subdags[counter])
        

        if(y+i > len(adj_list)-1):
            current_subdag.append(adj_list[x+i])
            break
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

        for hadamard_subdag in hadamard_subdags:
            hadamard_subdag.append(adj_list[x+i])
            #hadamard_subdag.append(adj_list[y+i])
        
    if(len(current_subdag) > 0):
        subdag_list.append(current_subdag)
    
    return subdag_list
        
def sort_subdag(adj_list: list):
    '''
    Sorts the entries in a sub-dag so all identical operations are grouped.
    '''
    if(adj_list[0] is str and adj_list[0].split('_')[0] == 'h'):
        #We've got a Hadamard Sub-Dag, no sorting required
        return adj_list

    sorted_list = list()
    for entry in adj_list:
        if(entry in sorted_list):
            continue
        sorting_entry = entry
        for i in range(len(adj_list)):
            if(adj_list[i] == sorting_entry):
                sorted_list.append(adj_list[i])

    return sorted_list

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
circ1.cx(q1[1], q1[0])
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

sorted_subdags = list()
for subd in subdags:
    sorted_subdags.append(sort_subdag(subd))

print("=======")
print(sorted_subdags)
print("=======")

# hadamard subdags
q2 = QuantumRegister(3, 'q')
c2 = ClassicalRegister(3, 'c')
circ2 = QuantumCircuit(q2, c2)
circ2.h(q2[0])
circ2.x(q2[1])
circ2.h(q2[2])
circ2.x(q2[0])
circ2.cx(q2[2], q2[1])
circ2.x(q2[0])
circ2.h(q2[1])
circ2.x(q2[2])
circ2.cx(q2[0], q2[1])
circ2.h(q2[2])
circ2.h(q2[0])
circ2.h(q2[1])

print(circ2)
dag2 = circuit_to_dag(circ2)
listx2 = dag_to_list(dag2)

#print(listx2)

subdags2 = divide_into_subdags(listx2)
sorted_subdaggs = list()
for subdagg in subdags2:
    print(subdagg)
    sorted_subdaggs.append(sort_subdag(subdagg))
print("-----------------------------------------")
for sorted_subdagg in sorted_subdaggs:
    print(sorted_subdagg)

test_list = [1, 2, 2, 1, 4, 2, 2, 1, 4, 5, 4, 5]
sorted_test_list = sort_subdag(test_list)
print(test_list)
print(sorted_test_list)