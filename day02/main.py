#!/usr/bin/env python

# import os.path
# print(os.path.curdir)
# import sys; sys.exit()

def inc(a, b):
    return  0 < b - a < 4

def dec(a, b):
    return 0 < a - b < 4

safe_levels = 0

with open('input.dat', 'r') as ifh:
    for line in ifh.readlines():
        levels = line.rstrip().split()

        cmp = None
        b = int(levels.pop(0))

        while levels:
            a = b
            b = int(levels.pop(0))

            if not cmp:
                if a < b: cmp = inc
                else: cmp = dec

            if not cmp(a, b):
                break
        else:
            print(f'{line.rstrip()} is safe.')
            safe_levels += 1
print(safe_levels)
