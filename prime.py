factors = []


def generate_prime_factors(number, factors):
    """Accepts a number and generates prime factors for this number"""
    # function raises an error whenever typed value is not an int
    if type(number) is not int:
        raise ValueError
    else:
        # function appends factor to the list of factors if it can be divided evenly with no remainder
        i = 2
        while i <= number:
            if (number % i) == 0:
                factors.append(i)
                # function assigns a decreased value to a number by dividing itself with the current iterator:
                number /= i
            else:
                # for values higher than 2, iterate i by 1 each time
                i += 1

        return factors


if __name__ == '__main__':
    print('PyCharm')
