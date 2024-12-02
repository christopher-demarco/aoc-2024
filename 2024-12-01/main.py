#!/usr/bin/env python

ll = []; rl = []; sim = 0

with open('input.dat', 'r') as ifh:
    for line in ifh.readlines():
        l, r = line.rstrip().split('   ')
        l = int(l); r = int(r)
        ll.append(l); rl.append(r)
ll.sort(); rl.sort()

distance = 0; similarity = 0
for i in range(len(ll)):
    l = ll[i]; r = rl[i]
    distance += abs(r - l)
    if r in ll:
        similarity += r

print(f'distance is {distance}')
print(f'similarity is {similarity}')
