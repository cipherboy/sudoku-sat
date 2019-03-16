# sudoku-sat

Tools to solve Sudoku with SAT

## Current Instructions

### Dependencies

Requires [cmsh](https://github.com/cipherboy/cmsh), `pycryptosat`, and Python 3.

### Running

Call `sudoku-sat.py` with the desired width and any constraints:

    $ ./sudoku-sat.py 9 3,1=5 6,1=8 9,1=7 5,2=9 8,2=2 2,3=4 3,3=1 6,3=5 1,4=8 7,4=5 2,5=7 4,5=6 6,5=2 8,5=9 3,6=9 9,6=2 4,7=7 7,7=9 8,7=3 2,8=6 5,8=4 1,9=4 4,9=9 7,9=8
    [2, 3, 7, 8, 1, 6, 5, 9, 4]
    [9, 8, 4, 2, 7, 5, 1, 6, 3]
    [5, 6, 1, 4, 3, 9, 2, 8, 7]
    [3, 4, 2, 1, 6, 8, 7, 5, 9]
    [1, 9, 6, 7, 5, 3, 8, 4, 2]
    [8, 7, 5, 9, 2, 4, 6, 3, 1]
    [6, 1, 3, 5, 4, 7, 9, 2, 8]
    [4, 2, 8, 6, 9, 1, 3, 7, 5]
    [7, 5, 9, 3, 8, 2, 4, 1, 6]

## Legacy Instructions

### Dependencies

Requires [bcsat](https://users.ics.aalto.fi/tjunttil/bcsat/), python, and
any sat solver.

### Running

First edit `build.py` to include the grid you are trying to solve. Currently
this is the same grid as in ./samples/10-16x16.txt. This will print out a set
of constraints mapping to the grid. Redirect this to a file, e.g.,
`10-input.txt`.

Then run `gen.py <size>` where <size> is the size of the sudoku grid. This will
generate the constraint set for the general rules of sudoku.

Use `cat *.txt > problem.bc` to build a valid BC circuit for use with bc2cnf.

Use `bc2cnf -nosimplify -nocoi problem.bc problem.cnf` to convert the
instance to normal form. This can then be used with any SAT solver.

Use `merge.py problem.cnf problem.out > problem.sol` to merge the input
with the SAT solver to create a solution.

Use `display.py <size> problem.sol` to print out the solved Sudoku grid. If
any grid squares are missing, they will be displayed as zero.
