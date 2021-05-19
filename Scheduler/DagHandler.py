from qiskit.dagcircuit import DAGCircuit
import binascii

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
    Hashes the entries in the adjacency list
    '''
    hashed_adj_list = []
    known_hashes = dict()

    for adj in adj_list:
        f = adj.split('_')
        new_hash = 0
        for l in f:
            if(len(l) == 1):
                new_hash += 0 + 17 * ord(l)-97
            elif(len(l) == 2):
                #new_hash += ord(l[0])
                new_hash += ord(l[1])
            elif(len(l) >= 4):
                new_hash += ord(l[0])
                new_hash += ord(l[1])
                new_hash += ord(l[2])
                new_hash += ord(l[3])
                
        
        if(new_hash not in known_hashes.values()):
            known_hashes[adj] = new_hash
        elif(adj not in known_hashes.keys()):
            while(new_hash not in known_hashes.values()):
                new_hash += 1
            
            known_hashes[adj] = new_hash
        
        hashed_adj_list.append(new_hash/100)
    
    return hashed_adj_list

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
    cx_direction_exists = False
    skip_one = False
    subdag_list = list()
    current_subdag = list()
    hadamard_subdags = list()
    for i in range(0, len(adj_list), 1):
        if(skip_one):
            skip_one = False
            continue
        # Check if we are dealing with Hadamard subdags
        if(adj_list[i].split('_')[0] == 'h'):
            counter = 0
            closure_found = False
            for hadamard_subdag in hadamard_subdags:
                # If we find same hadamard gate, we've got a complete hadamard subdag, close it,
                # add it to the rest of subdags, and remove from Hadamard subdag list
                if(hadamard_subdag[0] == adj_list[i]):
                    hadamard_subdag.append(adj_list[i])
                    closure_found = True
                    break
                counter += 1
            if(closure_found is False):
                new_hadamard_subdag = list()
                hadamard_subdags.append(new_hadamard_subdag)
            else:
                subdag_list.append(hadamard_subdags[counter])
                cx_direction_exists = True
                del(hadamard_subdags[counter])
        

        if(i+1 > len(adj_list)-1):
            current_subdag.append(adj_list[i])
            break
        if(check_if_interchangeable(adj_list[i], adj_list[i+1])):
            current_subdag.append(adj_list[i])
        else:
            current_subdag.append(adj_list[i])
            current_subdag.append(adj_list[i+1])
            subdag_list.append(current_subdag)
            current_subdag = list()
            skip_one = True

        for hadamard_subdag in hadamard_subdags:
            hadamard_subdag.append(adj_list[i])
        
    if(len(current_subdag) > 0):
        subdag_list.append(current_subdag)
    
    return subdag_list, cx_direction_exists

def chop_subdag(adj_list: list, chop_size = 3):
    '''
    Divides given subdag into smaller subdags of a given size.
    Make sure to cast the result into list()
    '''
    for i in range(0, len(adj_list), chop_size):
        yield adj_list[i:i+chop_size]

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
