factors = []

def prime_factors(number, factors):
    """Accepts a number as a first argument and as a result completes the list of prime factors.
    For the function to work properly, enter [] as the second attribute"""
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

# checking how it works
print(prime_factors(3958159172, []))

if __name__ == '__main__':
    print('PyCharm')
