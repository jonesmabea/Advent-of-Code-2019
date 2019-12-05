from day2.src.utils import load_input, update_instructions, run_instructions
from itertools import product
import multiprocessing


def brute_force(arg):
    noun, verb = arg
    try:
        inst = instructions.copy()
        inst = update_instructions(noun, verb, inst)
        inst_res = run_instructions(inst)
        if inst_res[0] == 19690720:
            print(f"Noun:{noun} Verb:{verb}")
            print(f"Puzzle answer is {100*inst[1]+inst[2]}")
            return inst_res
    except Exception as e:
        print(e)
    return None


if __name__ == "__main__":

    nouns = list(range(0, 100))
    verbs = list(range(0, 100))

    all_list = [nouns, verbs]
    all_permutations = list(product(*all_list))
    instructions = load_input()

    with multiprocessing.Pool(4) as pool:
        reslist = pool.map(brute_force, all_permutations)
    final_res = list(filter(None.__ne__, reslist))[0]
    print(final_res)
