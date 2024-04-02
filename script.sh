#!/bin/bash

# Assuming your puzzle files are in a folder named "puzzles"
PUZZLE_FOLDER="7/7/a/easy"
SOLUTIONS_FOLDER="solutions"  # Define the solutions folder

# Create the solutions folder if it doesn't exist
mkdir -p "$SOLUTIONS_FOLDER"

# Iterate over each puzzle file in the folder
for puzzle_file in "$PUZZLE_FOLDER"/*-puzzle.txt; do
    echo "Processing $puzzle_file..."

    # Generate the SMT file for the puzzle
    ./kenken2smt.py < "$puzzle_file" > "puzzle.smt"

    # Define the solution file name
    solution_file="${SOLUTIONS_FOLDER}/$(basename "${puzzle_file%-puzzle.txt}")_solutioneasy.smt"

    # Solve the puzzle using the SMT solver (mathsat in this case)
    mathsat < "puzzle.smt" > "$solution_file"

done