import numpy as np

op_dict = {1: np.add, 2: np.multiply, 3: input, 4: print}


def load_input():
    return np.loadtxt("p1_input.txt", delimiter=",", dtype=np.int).reshape(-1)


def get_parameter_modes(instruction):
    instruction = str(instruction)
    op_code = int(instruction[-2:])
    params = instruction[:-2].zfill(2)
    p1, p2 = eval(params[1]), eval(params[0])
    return (op_code, p1, p2)


def get_instruction_parameters(instruction_ptr, curr_instruction):
    if curr_instruction in [3, 4]:
        new_ptr = instruction_ptr + 2
        param_indices = instruction_ptr + 1
    elif curr_instruction in [5, 6]:
        new_ptr = instruction_ptr + 3
        param_indices = slice(instruction_ptr + 1, instruction_ptr + 3)
    else:
        param_indices = slice(instruction_ptr + 1, instruction_ptr + 4)
        new_ptr = instruction_ptr + 4

    return param_indices, new_ptr


def get_next_instruction_set(ptr, instructions):
    p_modes = [0, 0]
    curr_instruction = instructions[ptr]
    if len(str(curr_instruction)) > 1:
        curr_instruction, *p_modes = get_parameter_modes(curr_instruction)

    param_indices, new_ptr = get_instruction_parameters(ptr, curr_instruction)
    params = instructions[param_indices]
    return curr_instruction, params, new_ptr, p_modes


def fetch_values(p_modes_and_params, instruction_set):
    values = []
    for p_mode, param in p_modes_and_params:
        if p_mode == 1:
            values.append(param)
        else:
            value = instruction_set[param]
            values.append(value)

    return values


def update_instructions(val1, val2, inst_set):
    inst_set[[1, 2]] = val1, val2
    return inst_set


def run_instructions(instruction_set):
    curr_ptr = 0
    while True:
        try:
            curr_instruction, params, new_ptr, p_modes = get_next_instruction_set(
                curr_ptr, instruction_set
            )
            if curr_instruction == 99:
                return instruction_set
            elif curr_instruction == 3:
                store_loc = params
                inp = op_dict[curr_instruction]("Enter input:")
                instruction_set[store_loc] = eval(inp)
            elif curr_instruction == 4:
                store_loc = params
                op_dict[curr_instruction](instruction_set[store_loc])

            elif curr_instruction == 5:
                inst_params = params
                p_mode_params = zip(p_modes, inst_params)
                values = fetch_values(p_mode_params, instruction_set)
                is_jump_true, val = values
                if is_jump_true:
                    curr_ptr = val
                    continue
            elif curr_instruction == 6:
                inst_params = params
                p_mode_params = zip(p_modes, inst_params)
                values = fetch_values(p_mode_params, instruction_set)
                is_jump_false, val = values
                if not is_jump_false:
                    curr_ptr = val
                    continue

            elif curr_instruction == 7:
                *inst_params, store_loc = params
                p_mode_params = zip(p_modes, inst_params)
                values = fetch_values(p_mode_params, instruction_set)
                param1, param2 = values
                is_less_than = param1 < param2
                instruction_set[store_loc] = is_less_than

            elif curr_instruction == 8:
                *inst_params, store_loc = params
                p_mode_params = zip(p_modes, inst_params)
                values = fetch_values(p_mode_params, instruction_set)
                param1, param2 = values
                is_less_than = param1 == param2
                instruction_set[store_loc] = is_less_than

            else:
                *inst_params, store_loc = params
                p_mode_params = zip(p_modes, inst_params)
                values = fetch_values(p_mode_params, instruction_set)
                op = op_dict[curr_instruction]
                result = op(*values)
                instruction_set[store_loc] = result

            curr_ptr = new_ptr
        except (KeyError, IndexError):
            raise


if __name__ == "__main__":
    instructions = load_input()
    inst_res = run_instructions(instructions)
