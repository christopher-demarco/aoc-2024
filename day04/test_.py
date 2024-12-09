import pytest

# yes, many of these tests are not clean and/or not unit tests.
# no, santa claus will bring me presents anyway.

import main

def test_e():
    assert main.e(0, 5, 3) == [(0,5), (0,6), (0,7)]

def test_s():
    assert main.s(3,9,4) == [(3,9),(4,9),(5,9),(6,9)]

with open('example.dat', 'r') as ifh:
    example_raw = ifh.read()
m = main.create_matrix(example_raw)

def test_get_vector():
    assert main.get_vector(m, main.s(9,0,2)) == None
    assert main.get_vector(m, main.s(3,9,4)) == ['X','M','A','S']

def test_stringify_char_array():
    assert main.stringify_char_array(main.get_vector(m, main.e(0,5,4))) \
        == 'XMAS'
