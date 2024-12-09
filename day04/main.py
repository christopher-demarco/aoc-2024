#!/usr/bin/env python

import itertools
import sys

def create_matrix(input):
    matrix = []
    lines = input.split('\n')
    for line in lines:
        matrix.append(list(line))
    return matrix

def stringify_matrix(matrix):
    string = ''
    for line in matrix:
        string += ''.join(line) + '\n'
    return string

# def e(x, y, i):
#     v = list(
#         itertools.zip_longest(
#             range(x, y+n),
#             (x,),
#             row
#             ))
#     return v

# directions = [e,]

# def find_in_matrix(target, matrix):
#     len_target = len(target)
#     matches = 0
#     rows = len(matrix)
#     cols = len(matrix[0])
#     for row in rows:
#         for col in cols:
#             for dir in directions:
#                 if dir(row, col, len_target) == target:
#                     matches += 1

def e(y,x,i):
    return list(itertools.zip_longest((y,), range(x,x+i), fillvalue=y))
def s(y,x,i):
    return list(itertools.zip_longest((range(y,y+i)), (x,), fillvalue=x))

def get_vector(matrix, vector):
    try:
        return [matrix[y][x] for y, x in vector]
    except IndexError:
        return None

def stringify_char_array(array):
    return ''.join(array)

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as ifh:
        m = create_matrix(ifh.read())
        print(s(9,1,2))
        print(get_vector(m, s(9,2,2)))
