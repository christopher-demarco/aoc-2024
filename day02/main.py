#!/usr/bin/env python

# import os.path
# print(os.path.curdir)
# import sys; sys.exit()

def inc(a, b):
    return  0 < b - a < 4

def dec(a, b):
    return 0 < a - b < 4

def test_levels(b, levels):
    cmp = None
    while levels:
        a = b
        b = int(levels.pop(0))

        if not cmp:
            if a < b: cmp = inc
            else: cmp = dec

        if not cmp(a, b):
            return False
        else:
            continue
    return True

safe_levels = 0

with open('input.dat', 'r') as ifh:
    for line in ifh.readlines():
        levels = line.rstrip().split()

        b = int(levels.pop(0))
        if test_levels(b, levels):
            print(f'{line.rstrip()} is safe.')
            safe_levels += 1
print(safe_levels)
