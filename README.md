# sudoku-sat

Tools to solve Sudoku with SAT

# Dependencies 

Requires [bcsat](https://users.ics.aalto.fi/tjunttil/bcsat/), python, and
any sat solver. 

# Running

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
