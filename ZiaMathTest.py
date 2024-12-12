from mpmath import mp

def print_pi_to_n_digits(n):

    # Set precision to n decimal places

    mp.dps = n + 1  # Adding 1 to account for the "3." before the decimals

    # Return pi to n decimal places as a string

    return str(mp.pi)
