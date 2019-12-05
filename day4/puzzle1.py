password_range = range(158126, 624574)


def pair_window(lst):
    for i in range(0, len(lst), 2):
        yield lst[i : i + 2]


def check_adjacent_double(curr_password):
    for ind in range(len(curr_password) - 1):
        if curr_password[ind] is curr_password[ind + 1]:
            return True
    return False


def check_two_digits_similar(curr_password):
    prev_digit = float("-inf")
    dyn_check = check_adjacent_double(curr_password)
    for digit_pair in pair_window(curr_password):
        d1 = eval(digit_pair[0])
        d2 = eval(digit_pair[1])
        pair_value = d2 >= d1
        if pair_value and d1 >= prev_digit and dyn_check:
            prev_digit = d2
        else:
            return False

    return True


if __name__ == "__main__":
    cnt = 0
    for password in password_range:
        if len(str(password)) == 6:
            val = check_two_digits_similar(str(password))
            if val:
                cnt += 1
    print(f"Valid Passwords: {cnt}")
