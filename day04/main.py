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

def e(y,x,i):
    return list(itertools.zip_longest((y,), range(x,x+i), fillvalue=y))
def s(y,x,i):
    return list(itertools.zip_longest((range(y,y+i)), (x,), fillvalue=x))

directions = [e,s]

def get_vector(matrix, vector):
    try:
        return [matrix[y][x] for y, x in vector]
    except IndexError:
        return ''

def stringify_char_array(array):
    return ''.join(array)

def find_in_matrix(target, matrix):
    len_target = len(target)
    matches = 0
    rows = len(matrix)
    cols = len(matrix[0])
    for y in range(rows):
        for x in range(cols):
            for dir in directions:
                dirword = stringify_char_array(
                    get_vector(
                        matrix, dir(y, x, len_target)))
                print(y, x, dir, dirword)
                if dirword == target:
                    matches += 1
    return matches

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as ifh:
        m = create_matrix(ifh.read())
        print(f'Found {find_in_matrix('XMAS', m)} matches.')