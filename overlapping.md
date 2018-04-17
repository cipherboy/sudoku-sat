# Overlapping Sudoku

This repository has recently been extended to support overlapping Sudoku due
to CTF problems in the BSidesIowa / SecDSM 2018 [CTF](https://bsidesiowa.secdsm.org).

Some manual work is still required to build an overlapping Sudoku instance. To
begin, a regular 9x9 Sudoku board is indexed as follows:

       0 1 2 3 4 5 6 7 8
       - - - - - - - - -
    0 |     |     |     | 0
    1 |     |     |     | 1
    2 |     |     |     | 2
       - - - - - - - - -
    3 |     |     |     | 3
    4 |     |     |     | 4
    5 |     |     |     | 5
       - - - - - - - - -
    6 |     |     |     | 6
    7 |     |     |     | 7
    8 |     |     |     | 8
       - - - - - - - - -
       0 1 2 3 4 5 6 7 8

Where the coordinates `(0, 0)` describe the top left cell, `(1, 0)` describe
the cell to the immediate right of it, `(0, 1)` below it, etc.

First, determine how many overlapping Sudoku instances there are. In the
case of the `sudoku-overlap` example, there are two, in `sudoku-samurai`
example, there are five overlapping grids. Edit `gen.py` to have the
`prefixes` variable reflect the correct number of boards, and assign
unique prefixes to each. Then run `gen.py` in the directory to generate
the main Sudoku constraints.

For each Sudoku instance, edit the `grid` variable in `build.py` to
contain the initial numbers given in the problem; any space that is empty,
use a `0` in the grid. Run `build.py` with an argument of the prefix of
the Sudoku instance that this set of initial constraints belongs to.

Then, generate constraints for combining each grid. The arguments to
`combine.py` are: `size p1 p1x_min p1x_max p1y_min p1y_max p2 p2x_min p2y_min`,
where `size` is the size of the Sudoku grid (9x9 usually), `p1` is the first
board's prefix, `p1x_min` is the minimum x coordinate of the overlapping
section, `p1x_max` is the maximum x coordinate of the overlapping section,
`p1y_min` and `p1y_max` are the same as the previous two except for the `y`
coordinate, `p2` is the prefix of the second Sudoku grid, `p2x_min` and
`p2y_min` are the minimum values of the overlapping region on the second grid.
This is as follows:

             p1  p1
             min max
             - - -
    p1y_min |     | p2y_min
            |     |
    p1y_max |     | ...
             - - -
             p2  ...
             min

For each overlapping region, generate combining constraints. Then, create a
file called `98-combine.txt` with the contents:

    combine := AND(p1p2combine, ...);

where `p1` and `p2` are the prefixes used for all grids. For example, the
`98-combine.txt` from `sudoku-samurai` is:

    combine := AND(s1s3combine, s2s3combine, s3s4combine, s3s5combine);

To build and run the SAT instance, use the `run.sh` script. Note that you'll
need [bc2cnf](https://users.ics.aalto.fi/tjunttil/circuits/) from circuits
installed, and [CryptoMiniSat](https://github.com/msoos/cryptominisat).
To display the resulting grids, edit `display.py` to have the same prefixes
as `gen.py`, and run `display.py size /path/to/problem.sol`, where `size` is
the size of the puzzle (9 in the case of a 9x9 grid).

