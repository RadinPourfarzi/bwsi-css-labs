import pytest
from labs.lab_1.lab_1d import two_sum

def test_pair_not_at_start():
    assert two_sum([3, 2, 4], 6) == [1, 2]

def test_duplicate_values():
    assert two_sum([3, 3], 6) == [0, 1]

def test_negative_numbers():
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]

def test_mixed_positive_and_negative():
    assert two_sum([10, -2, 8, 5], 6) == [1, 2]

def test_zeroes():
    assert two_sum([0, 4, 3, 0], 0) == [0, 3]

def test_no_solution_returns_empty_list():
    assert two_sum([1, 2, 3], 10) == []
    
def test_empty_list():
    with pytest.raises(ValueError, match="Input list cannot be empty."):
        two_sum([], 67)