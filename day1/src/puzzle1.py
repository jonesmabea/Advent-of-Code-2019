from day1.src.util import np, load_input, calculate_fuel

INPUT_FILE = "input_p1.txt"

if __name__ == "__main__":
    masses = load_input(INPUT_FILE)
    print(f"Calculating the fuel needed for {masses.size} modules")
    calc_vec = np.vectorize(calculate_fuel)
    print(f"Total fuel needed is {np.sum(calc_vec(masses))}")
