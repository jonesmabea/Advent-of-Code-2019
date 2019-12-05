from day2.src.utils import load_input, update_instructions, get_next_instruction_set, run_instructions


if __name__ == "__main__":
    instructions = load_input()
    instructions = update_instructions(12, 2, instructions)
    inst_res = run_instructions(instructions)
    print(inst_res)