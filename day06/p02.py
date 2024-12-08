#!/usr/bin/env python

import sys
import time

class Exit(BaseException): pass
class Loop(BaseException): pass

class Map:
    def __init__(self, starting_layout):
        self.starting_layout = starting_layout
        self.guard_heading = 'n'
        self.guard_unique_positions = set(())
        self.layout = self.parse_layout()

        self.moves = {
            'n': lambda x, y: (x, y - 1),
            'e': lambda x, y: (x + 1, y),
            's': lambda x, y: (x, y + 1),
            'w': lambda x, y: (x - 1, y)
        }
        self.turn = {'n': 'e', 'e': 's', 's': 'w', 'w': 'n'}
        self.guard_glyph = {'n': '^', 'e': '>', 's': 'v', 'w': '<'}

    def parse_layout(self):
        layout_matrix = []
        self.num_rows = len(self.starting_layout)
        for i in range(self.num_rows):
            row = list(self.starting_layout[i].rstrip())
            self.num_cols = len(row)
            try:
                self.guard_pos = (row.index('^'), i)
            except ValueError:
                pass
            layout_matrix.append(row)
        self.guard_unique_positions.add((self.guard_pos, self.guard_heading))
        return layout_matrix

    def __str__(self):
        string_layout = ''
        for row in self.layout:
            row = ''.join(row) + '\n'
            string_layout += row
        return string_layout

    def run(self):
        while True:
            try:
                self.move()
            except Exit:
                break

    def get_square_ahead(self):
        square_ahead = self.moves[self.guard_heading](self.guard_pos[0], self.guard_pos[1])
        return square_ahead

    def move(self):
        next_square = self.get_square_ahead()

        if -1 in next_square:
            raise Exit
        try:
            ahead = self.layout[next_square[1]][next_square[0]]
        except IndexError:
            raise Exit

        if ahead == '.':
            loop_detector = len(self.guard_unique_positions)
            self.layout[self.guard_pos[1]][self.guard_pos[0]] = '.'
            self.layout[next_square[1]][next_square[0]] = self.guard_glyph[self.guard_heading]
            self.guard_pos = next_square
            self.guard_unique_positions.add((self.guard_pos, self.guard_heading))
            if len(self.guard_unique_positions) == loop_detector:
                raise Loop

        else:
            self.guard_heading = self.turn[self.guard_heading]
            self.layout[self.guard_pos[1]][self.guard_pos[0]] = self.guard_glyph[self.guard_heading]

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as ifh:
        original_map = ifh.readlines()

    loops = 0

    # Count the columns and rows
    layout_matrix = []
    num_rows = len(original_map)
    for i in range(num_rows):
        row = list(original_map[i].rstrip())
        num_cols = len(row)
        layout_matrix.append(row)

    # Now simulate every possible obstacle
    for y in range(num_rows):
        for x in range(num_cols):
            # Turn it back into the original format so we can run the simulation
            modified_map = []
            for row in layout_matrix:
                string_row = ''.join(row) + '\n'
                modified_map.append(string_row)
            m = Map(modified_map)
            print(f'{y}/{num_rows},{x}/{num_cols}')
            if m.layout[y][x] != '#':
                m.layout[y][x] = '#'
            else:
                continue
            try:
                m.run()
            except Loop:
                loops += 1
            print(loops)
    print(f'{loops} configurations create a loop.')
