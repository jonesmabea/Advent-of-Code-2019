import numpy as np

op_dict = {1: np.add, 2: np.multiply}


def load_input():
    return np.loadtxt("p1_input.txt", delimiter=",", dtype=np.int).reshape(-1)


def resolve_instruction(index):
    start = index * 4
    return slice(start, start + 4)


def get_next_instruction_set(index, instructions):
    inst_slice = resolve_instruction(index)
    return instructions[inst_slice]


def update_instructions(val1, val2, inst_set):
    inst_set[[1, 2]] = val1, val2
    return inst_set


def run_instructions(instruction_set):
    curr_ptr = 0
    while True:
        try:
            op, *data_ind, result_ind = get_next_instruction_set(
                curr_ptr, instruction_set
            )
            if op == 99:
                return instruction_set
            elif op in [1, 2]:
                values = instruction_set[data_ind]
                op = op_dict[op]
                op_result = op(*values)
                instruction_set[result_ind] = op_result
                curr_ptr += 1
            else:
                raise Exception("Op Code not implemented")
        except (KeyError, IndexError):
            raise
