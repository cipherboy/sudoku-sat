#!/usr/bin/env python3

import math
import sys

import cmsh


def build_grid(model, width):
    pos_grid = {}
    box_grid = {}
    row_grid = {}
    column_grid = {}
    all_squares = []

    bits = math.ceil(math.log(width, 2))
    boxes = math.sqrt(width)
    if math.ceil(boxes) != math.floor(boxes):
        raise ValueError("Width must be a square: %d" % width)
    boxes = int(boxes)

    for row in range(0, width):
        if row not in row_grid:
            row_grid[row] = [None]*width
        r_box = row//boxes

        for column in range(0, width):
            if column not in column_grid:
                column_grid[column] = [None]*width
            c_box = column//boxes
            if (r_box, c_box) not in box_grid:
                box_grid[(r_box, c_box)] = [None]*width

            i_box = (boxes * (row % boxes)) + (column % boxes)

            square = model.vector(bits)
            pos_grid[(row, column)] = square
            box_grid[(r_box, c_box)][i_box] = square
            row_grid[row][column] = square
            column_grid[column][row] = square
            all_squares.append(square)

    grid = {}
    grid['pos'] = pos_grid
    grid['box'] = box_grid
    grid['row'] = row_grid
    grid['col'] = column_grid
    grid['all'] = all_squares

    return grid


def build_constraints(model, grid, width):
    constraints = True

    for key in grid['pos']:
        item = grid['pos'][key]
        item_range = (1 <= item) & (item <= width)
        constraints = constraints & item_range

    for grid_key in ['box', 'row', 'col']:
        for key in grid[grid_key]:
            items = grid[grid_key][key]
            for value in range(1, width+1):
                one_value = []
                for item in items:
                    one_value.append(item == value)

                vec_one_value = model.to_vector(one_value)
                constraints = constraints & (vec_one_value.bit_sum() == 1)

    return constraints



def main():
    width = int(sys.argv[1])

    model = cmsh.Model()
    grid = build_grid(model, width)
    consts = build_constraints(model, grid, width)

    for constraint in sys.argv[2:]:
        assert '=' in constraint
        assert constraint.count('=') == 1

        split_equals = constraint.split('=')
        pos = split_equals[0]
        value = int(split_equals[1])

        assert ',' in pos
        assert pos.count(',') == 1
        split_comma = pos.split(',')
        row = int(split_comma[0])
        column = int(split_comma[1])

        assert 1 <= row <= width
        assert 1 <= column <= width
        assert 1 <= value <= width

        consts = consts & (grid['pos'][(row-1, column-1)] == value)

    model.add_assert(consts)
    assert model.solve()

    negated = False
    for x in range(0, width):
        row = []
        for y in range(0, width):
            row.append(int(grid['pos'][(x, y)]))
            negation = grid['pos'][(x, y)] != int(grid['pos'][(x, y)])
            negated = negated | negation
        print(row)

    model.add_assert(negated)
    assert not model.solve()


if __name__ == "__main__":
    main()
