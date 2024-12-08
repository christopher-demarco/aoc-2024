#!/usr/bin/env python

import sys

class Exit(BaseException): pass

class Map:
    def __init__(self, starting_layout):
        self.starting_layout = starting_layout.split('\n')
        self.guard_unique_squares = set(())
        self.layout = self.parse_layout()
        self.guard_heading = 'n'

        self.moves = {
            'n': lambda x, y: (x, y - 1),
            'e': lambda x, y: (x + 1, y),
            's': lambda x, y: (x, y + 1),
            'w': lambda x, y: (x - 1, y)
        }
        self.turn = {'n': 'e', 'e': 's', 's': 'w', 'w': 'n'}
        self.guard_glyph = {'n': '^', 'e': '>', 's': 'v', 'w': '<'}
        print(self)

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
        self.guard_unique_squares.add(self.guard_pos)
        return layout_matrix

    def __str__(self):
        print(f'{self.guard_pos} ({len(self.guard_unique_squares)})')
        # print(self.guard_unique_squares)
        string_layout = ''
        for row in self.layout:
            row = ''.join(row) + '\n'
            string_layout += row
        return string_layout

    def run(self):
        while True:
            try:
                self.move()
                # print(self)
                print(len(self.guard_unique_squares))
            except Exit:
                print(self)
                print(f'Guard exited with heading {self.guard_heading} from {self.guard_pos}!')
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
            self.layout[self.guard_pos[1]][self.guard_pos[0]] = '.'
            self.layout[next_square[1]][next_square[0]] = self.guard_glyph[self.guard_heading]
            self.guard_pos = next_square
            self.guard_unique_squares.add(self.guard_pos)

        else:
            assert(ahead == '#')
            self.guard_heading = self.turn[self.guard_heading]
            self.layout[self.guard_pos[1]][self.guard_pos[0]] = self.guard_glyph[self.guard_heading]
        # input()

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as ifh:
        m = Map(ifh.read())

    m.run()
    print(f'{len(m.guard_unique_squares)} unique squares visited')
