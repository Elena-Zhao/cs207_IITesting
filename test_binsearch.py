
from pytest import raises
from binsearch import binary_search
import numpy as np

input = list(range(10))

def test_normal_case():
    assert binary_search(list(range(10)), 5) == 5

def test_float():
    assert binary_search(list(range(10)), 4.5) == -1

def test_out_of_bound():
    assert binary_search(list(range(10)), 10) == -1
    
def test_single_element():
    assert binary_search([5], 5) == 0
        
def test_single_element_out():
    assert binary_search([5], 4) == -1
    
def test_inf():
    assert binary_search([1,2,np.inf], 2) == 1

def test_inf_2():
    assert binary_search([1,2,np.inf], np.inf) == 2

def test_boundary_1():
    assert binary_search(input, 5, 1, 3) == -1

def test_boundary_2():
    assert binary_search(input, 2, 1, 3) == 2

def test_reversed_index():
    assert binary_search(input, 2, 3, 1) == -1

def test_same_index():
    assert binary_search(input, 2, 2, 2) == 2
    
def test_same_index_2():
    assert binary_search(input, 5, 2, 2) == -1

def test_None():
    with raises(TypeError):
        binary_search([2,3,1, None], None)
        
def test_None_2():
    with raises(TypeError):
        binary_search([2,3, None, 5], 5)

def test_None_3():
    assert binary_search([2,3,5, None], 2) ==0
    
def test_unsorted():
    assert binary_search([2,3,5, 0, 10], 3) ==1

def test_unsorted_2():
    assert binary_search([2,3,5, 0, 10], 10) == 4
    
def test_unsorted_3():
    assert binary_search([2,3,5, 0, -1], -1) == -1
    
def test_string():
    with raises(TypeError):
        binary_search([2,3, 'a', 5], 'a')
        
def test_string_2():
     with raises(TypeError):
        binary_search([2,3, 'a', 5], 5)
        
def test_string_3():
    assert binary_search([2,3, 'a', 5], 2) == 0

def test_duplicate():
    assert binary_search([-1,2,3, 5, 5,5, 6], 5) == 3
    
def test_overflow():
    with raises(OverflowError):
        binary_search(range(100000000000000000000000), 5)

def test_float():
    assert binary_search([1,2,3,5.0], 5)== 3