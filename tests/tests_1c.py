import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_single_positive():
    assert max_subarray_sum([5]) == 5

def test_single_negative():
    assert max_subarray_sum([-55]) == -55
    
def test_all_positive():
    assert max_subarray_sum([1, 2, 3, 4]) == 10
    assert max_subarray_sum([10, 5, 15, 20, 30]) == 80
    
def test_all_negative():
    assert max_subarray_sum([-1, -2, -3, -4]) == -1
    assert max_subarray_sum([-10, -5, -15, -20, -30]) == -5
    
def test_mixed_numbers():
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert max_subarray_sum([5,4,-1,7,8]) == 23
    
def test_empty_list():
    with pytest.raises(ValueError, match="Input list cannot be empty."):
        max_subarray_sum([])

def test_contains_zero():
    assert max_subarray_sum([0,0,0,0]) == 0