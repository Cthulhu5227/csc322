#### Group Members in Alphabetical Order:
Jasper St. John - V00968351
Jett Schreiber - V00990582
Justin Oliveros - V00945335
Rahul Sachdeva - V00969722

#### The 3 Executables in Submission:
1. kenken2smt.py - Takes input from STDIN in the format specifed on www.kenkenpuzzle.com and returns a SMT-LIB file, which is formated to be compatable with the mathsat smt solver.

2. smt2kenken.py - Takes the output given by the mathsat smt solver from STDIN and returns an output to STDOUT that is a string of the answers to the corresponding KenKen puzzle of the file fed into mathsat.

3. pp.py - Takes in an argument of either "puzzle_num"-solution.txt or "puzzle_num"-puzzle.txt and returns a string of either a completed on uncompleted, respectivly, KenKen puzzle to STDOUT formatted to look like an actual KenKen puzzle.

#### Shell Commands for Executing Submitted Executables:

**Executing kenken2smt.py and smt2kenken.py:**
  ./kenken2smt.py <puzzle.txt >puzzle.smt
  mathsat <puzzle.smt >model.smt
  ./smt2kenken.py <model.smt >solution.txt

**Exectuing pp.py to display puzzle with/without solution:**
  ./pp.py <puzzle.txt
  or
  ./pp.py <solution.txt
  
Note: for pp.py, puzzle.txt and solution.txt must contain the "#kenken" headerline indicating the puzzle_num and whether or not it is the solution file. The directory must also contain the "fetch.sh" file which was provided with the submission


