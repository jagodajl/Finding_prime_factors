factors = []


def generate_prime_factors(number, factors):
    """Accepts a number and generates prime factors for this number"""
    # function raises an error whenever typed value is not an int
    if type(number) is not int:
        raise ValueError
    else:
        # function appends factor to the list of factors if it can be divided evenly with no remainder
        i = 2
        if (number % i) == 0:
            factors.append(i)

        return factors


if __name__ == '__main__':
    print('PyCharm')
