import pytest

import prime


def test_integer():
    factors = []
    value_types = ["lol123", 3.14, 89.1j]

    for value in value_types:
        with pytest.raises(ValueError):
            prime.generate_prime_factors(value, factors)


def test_param_one():
    factors = []
    value = 1
    assert len(prime.generate_prime_factors(value, factors)) == 0


def test_param_two():
    factors = []
    value = 2
    output_list = prime.generate_prime_factors(value, factors)

    assert len(output_list) == 1 and output_list[0] == 2
