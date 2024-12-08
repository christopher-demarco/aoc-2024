#!/usr/bin/env python

import sys

class Map:
    def __init__(self, starting_layout):
        self.starting_layout = starting_layout.split('\n')
        self.layout = self.parse_layout()
        self.guard_moves = 1

    def parse_layout(self):
        layout_matrix = []
        self.num_rows = len(self.starting_layout)
        for i in range(self.num_rows):
            row = list(self.starting_layout[i])
            self.num_cols = len(row)
            try:
                self.guard_pos = (row.index('^'), i)
            except ValueError:
                pass
            layout_matrix.append(row)
        return layout_matrix

    def __str__(self):
        string_layout = ''
        for row in self.layout:
            row = ''.join(row) + '\n'
            string_layout += row
        return string_layout

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as ifh:
        m = Map(ifh.read())

    # print(m)
    # print(m.guard_pos)
