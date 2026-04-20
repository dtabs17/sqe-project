import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

from app import is_palindrome, has_pair_with_sum, reverse_list, is_palindrome_ignore_case, move_zeroes

def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("madam") == True

def test_has_pair_with_sum():
    assert has_pair_with_sum([1, 2, 3, 4, 5], 9) == True
    assert has_pair_with_sum([1, 2, 3, 4, 5], 10) == False

def test_reverse_list():
    assert reverse_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert reverse_list([1]) == [1]

def test_is_palindrome_ignore_case():
    assert is_palindrome_ignore_case("Racecar") == True
    assert is_palindrome_ignore_case("Hello") == False

def test_move_zeroes():
    assert move_zeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    assert move_zeroes([0, 0, 1]) == [1, 0, 0]