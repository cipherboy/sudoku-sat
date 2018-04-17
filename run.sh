cat ./*.txt | ~/tools/bc2cnf -nocoi -nots -nosimplify > problem.cnf
~/tools/cryptominisat5 problem.cnf > problem.out
echo $?
python3 ../merge.py problem.cnf problem.out > problem.sol
