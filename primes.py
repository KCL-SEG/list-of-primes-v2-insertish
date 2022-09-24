"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def primes(number_of_primes):
    list = []

    # do not allow non-integer input
    if not isinstance(number_of_primes, int):
        raise TypeError("expected integer")

    # do not allow zero or negative inputs
    if number_of_primes <= 0:
        raise ValueError

    # keep track of current value
    value = 2

    # keep going until we have enough primes
    while len(list) < number_of_primes:
        # a prime is divisible by 1 or itself (ignore these)
        # so we want to test if non-prime and fail fast
        prime = True
        for i in range(2, value - 1):
            # check if divisible by i
            if value % i == 0:
                prime = False
                break

        # if prime, add to list
        if prime:
            list.append(value)

        # go to the next value
        value += 1

    return list
