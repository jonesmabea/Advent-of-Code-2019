import numpy as np
from pathlib import Path

CWD = Path(__file__).resolve().parent


def load_input(input_fp: str):
    abs_path = CWD / input_fp
    return np.loadtxt(abs_path).reshape(-1)


def calculate_fuel(mass):
    return np.subtract(np.floor_divide(mass, 3), 2.0)
