
import pytest

from main import LargestNonPurchasable

def test_non_coprime_numbers():
        find = LargestNonPurchasable([6, 9]) 
        assert find.find_largest_number() == -1 # GCD is 3, not coprime

def test_empty_input():
    with pytest.raises(ValueError, match="Input list cannot be empty or single int."):
        find = LargestNonPurchasable([])
        find.find_largest_number()

def test_coprime_numbers():
    find = LargestNonPurchasable([5, 14]) 
    assert find.find_largest_number() == 51  # Coprime numbers 5 and 14

def test_duplicate_numbers():
    find = LargestNonPurchasable([5, 14, 14])
    assert find.find_largest_number() == 51
    
def test_mixed_small_and_large_numbers():
    find = LargestNonPurchasable([2, 5, 19])
    assert find.find_largest_number() == 3