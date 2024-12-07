#!/usr/bin/env python

import sys

funcs = {
    'mul': lambda a, b: a * b
}

def run(inst):
    func, args = inst.split('(')
    a, b = args.split(',')
    b = b.strip(')')
    return funcs[func](int(a), int(b))

with open(sys.argv[1], 'r') as ifh:
    print(run('mul(21,2)'))
    # for line in ifh.readlines():
        # while line:
        #     inst = line.pop(0)
