from itertools import groupby
from multiprocessing import Pool

password_range = range(158126, 624574)


def window(lst, n=2):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def check_if_triple(password):
    groups = [len(list(v)) for k, v in groupby(password)]
    return 2 in groups


def check_two_digits_similar(password):
    password = str(password)
    prev_digit = float("-inf")
    if check_if_triple(password):
        for digit_pair in window(password, 2):
            d1 = eval(digit_pair[0])
            d2 = eval(digit_pair[1])
            pair_value = d1 <= d2
            if pair_value and d1 >= prev_digit:
                prev_digit = d2
            else:
                return False
    else:
        return False

    return True


if __name__ == "__main__":

    with Pool(4) as pool:
        val = pool.map(check_two_digits_similar, password_range)

    print(f"Valid passwords: {sum(val)}")
