#!/usr/bin/env python

import re
import sys

funcs = {
    'mul': lambda a, b: a * b
}

def run(inst):
    func, args = inst.split('(')
    a, b = args.split(',')
    b = b.strip(')')
    return funcs[func](int(a), int(b))

total = 0

rex = re.compile('mul\\(\\d{1,3},\\d{1,3}\\)')

with open(sys.argv[1], 'r') as ifh:
    for line in ifh.readlines():
        for inst in rex.findall(line):
            ret = run(inst)
            total += ret

print(total)
