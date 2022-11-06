import pytest
import prime


def test_integer():
    factors = []
    value_types = ["lol123", 3.14, 89.1j]

    for value in value_types:
        with pytest.raises(ValueError):
            prime.generate_prime_factors(value, factors)


