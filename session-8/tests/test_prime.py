from prime import is_prime
import pytest

def test_prime_numbers():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True
    assert is_prime(11) == True
    assert is_prime(13) == True

def test_non_prime_numbers():
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(6) == False
    assert is_prime(9) == False
    assert is_prime(15) == False

def test_large_prime():
    assert is_prime(97) == True

def test_large_non_prime():
    assert is_prime(100) == False



def test_negative_number():
    with pytest.raises(TypeError):
        is_prime(-5)

def test_float_number():
    with pytest.raises(TypeError):
        is_prime(3.14)

@pytest.mark.parametrize("n, expected", [
    (2, True),
    (3, True),
    (4, False),
    (13, True),
    (20, False),
    (1, False),
    (0, False)
])
def test_is_prime_valid_cases(n, expected):
    assert is_prime(n) == expected


@pytest.mark.parametrize("n", [-1, -10, 3.14, "5", None])
def test_is_prime_invalid_inputs(n):
    with pytest.raises(TypeError):
        is_prime(n)


@pytest.mark.parametrize("n", ["7", "11"])
def test_is_prime_string_conversion(n):
    assert is_prime(n) is True

@pytest.mark.parametrize("n", ["not_a_number", "twelve"])
def test_is_prime_string_invalid(n):
    with pytest.raises(ValueError):
        is_prime(n)
