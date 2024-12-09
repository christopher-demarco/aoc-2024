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

def n(y,x,i):
    return list(itertools.zip_longest((range(y,y-i,-1)), (x,), fillvalue=x))
def ne(y,x,i):
    return list(itertools.zip_longest((range(y,y-i,-1)), range(x,x+i)))
def e(y,x,i):
    return list(itertools.zip_longest((y,), range(x,x+i), fillvalue=y))
def se(y,x,i):
    return list(itertools.zip_longest((range(y,y+i)), range(x,x+i)))
def s(y,x,i):
    return list(itertools.zip_longest((range(y,y+i)), (x,), fillvalue=x))
def sw(y,x,i):
    return list(itertools.zip_longest((range(y,y+i)), range(x,x-i,-1)))
def w(y,x,i):
    return list(itertools.zip_longest((y,), range(x,x-i,-1), fillvalue=y))
def nw(y,x,i):
    return list(itertools.zip_longest((range(y,y-i,-1)), range(x,x-i,-1)))

directions = [n,ne,e,se,s,sw,w,nw]

def get_vector(matrix, vector):
    try:
        vector_chars = [matrix[y][x] for y, x in vector if y>=0 and x>=0]
    except IndexError:
        return '' # this is eventually going to bite me
    return vector_chars

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
                bare_vector = dir(y, x, len_target)
                word_vector = get_vector(matrix, bare_vector)
                word = stringify_char_array(word_vector)
                print(y, x, dir, bare_vector, word, word == target)
                if word == target:
                    matches += 1
    return matches

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as ifh:
        m = create_matrix(ifh.read())
        print(f'Found {find_in_matrix('XMAS', m)} matches.')
