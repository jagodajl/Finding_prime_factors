import pytest

import prime


def test_integer():
    factors = []
    value_types = ["lol123", 3.14, 89.1j]

    for value in value_types:
        with pytest.raises(ValueError):
            prime.prime_factors(value, factors)


# the following tests check various parameters
def test_param_1():
    factors = []
    value = 1
    assert len(prime.prime_factors(value, factors)) == 0


def test_param_2():
    factors = []
    value = 2
    output_list = prime.prime_factors(value, factors)

    assert len(output_list) == 1 and output_list[0] == 2


def test_param_3():
    factors = []
    value = 3
    output_list = prime.prime_factors(value, factors)
    assert len(output_list) == 1 and output_list[0] == 3


def test_param_4():
    factors = []
    value = 4
    output_list = prime.prime_factors(value, factors)
    assert len(output_list) == 2 and output_list[0] == 2 and output_list[1] == 2


def test_param_6():
    factors = []
    value = 6
    output_list = prime.prime_factors(value, factors)
    assert len(output_list) == 2 and output_list[0] == 2 and output_list[1] == 3


def test_param_8():
    factors = []
    value = 8
    output_list = prime.prime_factors(value, factors)
    assert len(output_list) == 3 and output_list[0] == 2 and output_list[1] == 2 and output_list[2] == 2

def test_param_9():
    factors = []
    value = 9
    output_list = prime.prime_factors(value, factors)
    # Assert only 2 values - [2, 3]:
    assert len(output_list) == 2 and output_list[0] == 3 and output_list[1] == 3