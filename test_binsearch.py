
from pytest import raises
from binsearch import binary_search
# >>> input = list(range(10))

#     >>> binary_search([5], 4)
#     -1
#     >>> import numpy as np
#     >>> binary_search([1,2,np.inf], 2)
#     1
#     >>> binary_search([1,2,np.inf], np.inf)
#     2
#     >>> binary_search(input, 5, 1,3)
#     -1
#     >>> binary_search(input, 2, 1,3)
#     2
#     >>> binary_search(input, 2, 3, 1)
#     -1
#     >>> binary_search(input, 2, 2, 2)
#     2
#     >>> binary_search(input, 5, 2, 2)
#     -1
#     """
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