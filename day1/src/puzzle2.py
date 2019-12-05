from day1.src.util import np, load_input, calculate_fuel

INPUT_FILE = "input_p2.txt"


def calculate_rec_fuel(mass):
    fn = calculate_fuel(mass)
    if fn <= 0:
        return 0
    else:
        return fn + calculate_rec_fuel(fn)


if __name__ == "__main__":
    masses = load_input(INPUT_FILE)
    print(f"Calculating the fuel needed for {masses.size} modules")
    calc_vec = np.vectorize(calculate_rec_fuel)
    res = calc_vec(masses)
    print(f"Total fuel needed is {np.sum(res)}")
